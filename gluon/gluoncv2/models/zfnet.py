"""
    ZFNet, implemented in Gluon.
    Original paper: 'Visualizing and Understanding Convolutional Networks,' https://arxiv.org/abs/1311.2901.
"""

__all__ = ['ZFNet', 'zfnet']

import os
from mxnet import cpu
from mxnet.gluon import nn, HybridBlock


class ZFNetConv(HybridBlock):
    """
    ZFNet specific convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    kernel_size : int or tuple/list of 2 int
        Convolution window size.
    strides : int or tuple/list of 2 int
        Strides of the convolution.
    padding : int or tuple/list of 2 int
        Padding value for convolution layer.
    """

    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                 strides,
                 padding,
                 **kwargs):
        super(ZFNetConv, self).__init__(**kwargs)
        with self.name_scope():
            self.conv = nn.Conv2D(
                channels=out_channels,
                kernel_size=kernel_size,
                strides=strides,
                padding=padding,
                use_bias=True,
                in_channels=in_channels)
            self.activ = nn.Activation('relu')

    def hybrid_forward(self, F, x):
        x = self.conv(x)
        x = self.activ(x)
        return x


class ZFNetReduceBlock(HybridBlock):
    """
    ZFNet reduce block.

    Parameters:
    ----------
    nsize : int, default 5
        Amount of neighbouring channels used for normalization.
    """
    def __init__(self,
                 nsize=5,
                 **kwargs):
        super(ZFNetReduceBlock, self).__init__(**kwargs)
        self.nsize = nsize

        with self.name_scope():
            self.pool = nn.MaxPool2D(
                pool_size=3,
                strides=2,
                padding=1)

    def hybrid_forward(self, F, x):
        x = self.pool(x)
        x = F.LRN(x, nsize=self.nsize, knorm=2.0)
        return x


class ZFNetDense(HybridBlock):
    """
    ZFNet specific dense block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    """

    def __init__(self,
                 in_channels,
                 out_channels,
                 **kwargs):
        super(ZFNetDense, self).__init__(**kwargs)
        with self.name_scope():
            self.fc = nn.Dense(
                units=out_channels,
                weight_initializer="normal",
                in_units=in_channels)
            self.activ = nn.Activation('relu')
            self.dropout = nn.Dropout(rate=0.5)

    def hybrid_forward(self, F, x):
        x = self.fc(x)
        x = self.activ(x)
        x = self.dropout(x)
        return x


class ZFNetOutputBlock(HybridBlock):
    """
    ZFNet specific output block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    classes : int
        Number of classification classes.
    """
    def __init__(self,
                 in_channels,
                 classes,
                 **kwargs):
        super(ZFNetOutputBlock, self).__init__(**kwargs)
        mid_channels = 4096

        with self.name_scope():
            self.fc1 = ZFNetDense(
                in_channels=in_channels,
                out_channels=mid_channels)
            self.fc2 = ZFNetDense(
                in_channels=mid_channels,
                out_channels=mid_channels)
            self.fc3 = nn.Dense(
                units=classes,
                weight_initializer="normal",
                in_units=mid_channels)

    def hybrid_forward(self, F, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


class ZFNet(HybridBlock):
    """
    ZFNet model from 'Visualizing and Understanding Convolutional Networks,' https://arxiv.org/abs/1311.2901.

    Parameters:
    ----------
    channels : list of list of int
        Number of output channels for each unit.
    kernel_sizes : list of list of int
        Convolution window sizes for each unit.
    strides : list of list of int or tuple/list of 2 int
        Strides of the convolution for each unit.
    paddings : list of list of int or tuple/list of 2 int
        Padding value for convolution layer for each unit.
    in_channels : int, default 3
        Number of input channels.
    in_size : tuple of two ints, default (224, 224)
        Spatial size of the expected input image.
    classes : int, default 1000
        Number of classification classes.
    """
    def __init__(self,
                 channels,
                 kernel_sizes,
                 strides,
                 paddings,
                 in_channels=3,
                 in_size=(224, 224),
                 classes=1000,
                 **kwargs):
        super(ZFNet, self).__init__(**kwargs)
        self.in_size = in_size
        self.classes = classes

        with self.name_scope():
            self.features = nn.HybridSequential(prefix='')
            for i, channels_per_stage in enumerate(channels):
                stage = nn.HybridSequential(prefix='stage{}_'.format(i + 1))
                with stage.name_scope():
                    if i != 0:
                        stage.add(ZFNetReduceBlock())
                    for j, out_channels in enumerate(channels_per_stage):
                        stage.add(ZFNetConv(
                            in_channels=in_channels,
                            out_channels=out_channels,
                            kernel_size=kernel_sizes[i][j],
                            strides=strides[i][j],
                            padding=paddings[i][j]))
                        in_channels = out_channels
                self.features.add(stage)
            self.features.add(nn.MaxPool2D(
                pool_size=3,
                strides=2))

            self.output = nn.HybridSequential(prefix='')
            self.output.add(nn.Flatten())
            in_channels = in_channels * 6 * 6
            self.output.add(ZFNetOutputBlock(
                in_channels=in_channels,
                classes=classes))

    def hybrid_forward(self, F, x):
        x = self.features(x)
        x = self.output(x)
        return x


def get_alexnet(model_name=None,
                pretrained=False,
                ctx=cpu(),
                root=os.path.join('~', '.mxnet', 'models'),
                **kwargs):
    """
    Create ZFNet model with specific parameters.

    Parameters:
    ----------
    model_name : str or None, default None
        Model name for loading pretrained model.
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.mxnet/models'
        Location for keeping the model parameters.
    """
    channels = [[96], [256], [384, 384, 256]]
    kernel_sizes = [[7], [5], [3, 3, 3]]
    strides = [[2], [2], [1, 1, 1]]
    paddings = [[1], [0], [1, 1, 1]]

    net = ZFNet(
        channels=channels,
        kernel_sizes=kernel_sizes,
        strides=strides,
        paddings=paddings,
        **kwargs)

    if pretrained:
        if (model_name is None) or (not model_name):
            raise ValueError("Parameter `model_name` should be properly initialized for loading pretrained model.")
        from .model_store import get_model_file
        net.load_parameters(
            filename=get_model_file(
                model_name=model_name,
                local_model_store_dir_path=root),
            ctx=ctx)

    return net


def zfnet(**kwargs):
    """
    ZFNet model from 'Visualizing and Understanding Convolutional Networks,' https://arxiv.org/abs/1311.2901.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.mxnet/models'
        Location for keeping the model parameters.
    """
    return get_alexnet(model_name="zfnet", **kwargs)


def _test():
    import numpy as np
    import mxnet as mx

    pretrained = False

    models = [
        zfnet,
    ]

    for model in models:

        net = model(pretrained=pretrained)

        ctx = mx.cpu()
        if not pretrained:
            net.initialize(ctx=ctx)

        net_params = net.collect_params()
        weight_count = 0
        for param in net_params.values():
            if (param.shape is None) or (not param._differentiable):
                continue
            weight_count += np.prod(param.shape)
        print("m={}, {}".format(model.__name__, weight_count))
        assert (model != zfnet or weight_count == 62357608)

        x = mx.nd.zeros((1, 3, 224, 224), ctx=ctx)
        y = net(x)
        assert (y.shape == (1, 1000))


if __name__ == "__main__":
    _test()
