"""
    ZFNet, implemented in PyTorch.
    Original paper: 'Visualizing and Understanding Convolutional Networks,' https://arxiv.org/abs/1311.2901.
"""

__all__ = ['ZFNet', 'zfnet']

import os
import torch.nn as nn
import torch.nn.init as init


class ZFNetConv(nn.Module):
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
    stride : int or tuple/list of 2 int
        Strides of the convolution.
    padding : int or tuple/list of 2 int
        Padding value for convolution layer.
    """

    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                 stride,
                 padding):
        super(ZFNetConv, self).__init__()
        self.conv = nn.Conv2d(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            bias=True)
        self.activ = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.conv(x)
        x = self.activ(x)
        return x


class ZFNetReduceBlock(nn.Module):
    """
    ZFNet reduce block.

    Parameters:
    ----------
    nsize : int, default 5
        Amount of neighbouring channels used for normalization.
    """
    def __init__(self,
                 nsize=5):
        super(ZFNetReduceBlock, self).__init__()
        self.nsize = nsize

        self.pool = nn.MaxPool2d(
            kernel_size=3,
            stride=2,
            padding=1)
        self.norm = nn.LocalResponseNorm(size=nsize, k=2.0)

    def forward(self, x):
        x = self.pool(x)
        x = self.norm(x)
        return x


class ZFNetDense(nn.Module):
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
                 out_channels):
        super(ZFNetDense, self).__init__()
        self.fc = nn.Linear(
            in_features=in_channels,
            out_features=out_channels)
        self.activ = nn.ReLU(inplace=True)
        self.dropout = nn.Dropout(p=0.5)

    def forward(self, x):
        x = self.fc(x)
        x = self.activ(x)
        x = self.dropout(x)
        return x


class ZFNetOutputBlock(nn.Module):
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
                 classes):
        super(ZFNetOutputBlock, self).__init__()
        mid_channels = 4096

        self.fc1 = ZFNetDense(
            in_channels=in_channels,
            out_channels=mid_channels)
        self.fc2 = ZFNetDense(
            in_channels=mid_channels,
            out_channels=mid_channels)
        self.fc3 = nn.Linear(
            in_features=mid_channels,
            out_features=classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


class ZFNet(nn.Module):
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
    num_classes : int, default 1000
        Number of classification classes.
    """
    def __init__(self,
                 channels,
                 kernel_sizes,
                 strides,
                 paddings,
                 in_channels=3,
                 in_size=(224, 224),
                 num_classes=1000):
        super(ZFNet, self).__init__()
        self.in_size = in_size
        self.num_classes = num_classes

        self.features = nn.Sequential()
        for i, channels_per_stage in enumerate(channels):
            stage = nn.Sequential()
            for j, out_channels in enumerate(channels_per_stage):
                if i != 0:
                    stage.add_module("reduce{}".format(i + 1), ZFNetReduceBlock())
                stage.add_module("unit{}".format(j + 1), ZFNetConv(
                    in_channels=in_channels,
                    out_channels=out_channels,
                    kernel_size=kernel_sizes[i][j],
                    stride=strides[i][j],
                    padding=paddings[i][j]))
                in_channels = out_channels
            self.features.add_module("stage{}".format(i + 1), stage)
        self.features.add_module("final_pool", nn.MaxPool2d(
            kernel_size=3,
            stride=2))

        self.output = ZFNetOutputBlock(
            in_channels=(in_channels * 6 * 6),
            classes=num_classes)

        self._init_params()

    def _init_params(self):
        for name, module in self.named_modules():
            if isinstance(module, nn.Conv2d):
                init.kaiming_uniform_(module.weight)
                if module.bias is not None:
                    init.constant_(module.bias, 0)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.output(x)
        return x


def get_alexnet(model_name=None,
                pretrained=False,
                root=os.path.join('~', '.torch', 'models'),
                **kwargs):
    """
    Create ZFNet model with specific parameters.

    Parameters:
    ----------
    model_name : str or None, default None
        Model name for loading pretrained model.
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.torch/models'
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
        from .model_store import download_model
        download_model(
            net=net,
            model_name=model_name,
            local_model_store_dir_path=root)

    return net


def zfnet(**kwargs):
    """
    ZFNet model from 'Visualizing and Understanding Convolutional Networks,' https://arxiv.org/abs/1311.2901.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.torch/models'
        Location for keeping the model parameters.
    """
    return get_alexnet(model_name="zfnet", **kwargs)


def _calc_width(net):
    import numpy as np
    net_params = filter(lambda p: p.requires_grad, net.parameters())
    weight_count = 0
    for param in net_params:
        weight_count += np.prod(param.size())
    return weight_count


def _test():
    import torch
    from torch.autograd import Variable

    pretrained = False

    models = [
        zfnet,
    ]

    for model in models:

        net = model(pretrained=pretrained)

        # net.train()
        net.eval()
        weight_count = _calc_width(net)
        print("m={}, {}".format(model.__name__, weight_count))
        assert (model != zfnet or weight_count == 62357608)

        x = Variable(torch.randn(1, 3, 224, 224))
        y = net(x)
        assert (tuple(y.size()) == (1, 1000))


if __name__ == "__main__":
    _test()
