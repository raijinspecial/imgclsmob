# Large-scale image classification models on Keras

[![PyPI](https://img.shields.io/pypi/v/kerascv.svg)](https://pypi.python.org/pypi/kerascv)
[![Downloads](https://pepy.tech/badge/kerascv)](https://pepy.tech/project/kerascv)

This is a collection of large-scale image classification models. Many of them are pretrained on ImageNet-1K dataset
and loaded automatically during use. All pretrained models require the same ordinary normalization. Scripts for
training/evaluating/converting models are in the [`imgclsmob`](https://github.com/osmr/imgclsmob) repo.

## List of implemented models

- AlexNet (['One weird trick for parallelizing convolutional neural networks'](https://arxiv.org/abs/1404.5997))
- VGG/BN-VGG (['Very Deep Convolutional Networks for Large-Scale Image Recognition'](https://arxiv.org/abs/1409.1556))
- ResNet (['Deep Residual Learning for Image Recognition'](https://arxiv.org/abs/1512.03385))
- PreResNet (['Identity Mappings in Deep Residual Networks'](https://arxiv.org/abs/1603.05027))
- ResNeXt (['Aggregated Residual Transformations for Deep Neural Networks'](http://arxiv.org/abs/1611.05431))
- SENet/SE-ResNet/SE-PreResNet/SE-ResNeXt (['Squeeze-and-Excitation Networks'](https://arxiv.org/abs/1709.01507))
- DenseNet (['Densely Connected Convolutional Networks'](https://arxiv.org/abs/1608.06993))
- DarkNet Ref/Tiny/19 (['Darknet: Open source neural networks in c'](https://github.com/pjreddie/darknet))
- DarkNet-53 (['YOLOv3: An Incremental Improvement'](https://arxiv.org/abs/1804.02767))
- SqueezeNet/SqueezeResNet (['SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size'](https://arxiv.org/abs/1602.07360))
- SqueezeNext (['SqueezeNext: Hardware-Aware Neural Network Design'](https://arxiv.org/abs/1803.10615))
- ShuffleNet (['ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices'](https://arxiv.org/abs/1707.01083))
- ShuffleNetV2 (['ShuffleNet V2: Practical Guidelines for Efficient CNN Architecture Design'](https://arxiv.org/abs/1807.11164))
- MENet (['Merging and Evolution: Improving Convolutional Neural Networks for Mobile Applications'](https://arxiv.org/abs/1803.09127))
- MobileNet (['MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications'](https://arxiv.org/abs/1704.04861))
- FD-MobileNet (['FD-MobileNet: Improved MobileNet with A Fast Downsampling Strategy'](https://arxiv.org/abs/1802.03750))
- MobileNetV2 (['MobileNetV2: Inverted Residuals and Linear Bottlenecks'](https://arxiv.org/abs/1801.04381))
- IGCV3 (['IGCV3: Interleaved Low-Rank Group Convolutions for Efficient Deep Neural Networks'](https://arxiv.org/abs/1806.00178))
- MnasNet (['MnasNet: Platform-Aware Neural Architecture Search for Mobile'](https://arxiv.org/abs/1807.11626))

## Installation

To use the models in your project, simply install the `kerascv` package with desired backend. For example for MXNet backend:
```
pip install mxnet>=1.2.1 keras-mxnet kerascv
```
Or if you prefer TensorFlow backend:
```
pip install tensorflow kerascv
```
To enable/disable different hardware supports, check out installation instruction for the corresponding backend.

After installation check that the `backend` field is set to the correct value in the file `~/.keras/keras.json`. It is
also preferable to set the value of the `image_data_format` field to `channels_first` in the case of using the MXNet backend.  

## Usage

Example of using a pretrained ResNet-18 model (for `channels_first` data format):
```
from kerascv.model_provider import get_model as kecv_get_model
import numpy as np

net = kecv_get_model("resnet18", pretrained=True)
x = np.zeros((1, 3, 224, 224), np.float32)
y = net.predict(x)
```

## Pretrained models

Some remarks:
- All quality values are estimated with MXNet backend.
- Top1/Top5 are the standard 1-crop Top-1/Top-5 errors (in percents) on the validation subset of the ImageNet-1K dataset.
- FLOPs/2 is the number of FLOPs divided by two to be similar to the number of MACs.
- Remark `Converted from GL model` means that the model was trained on `MXNet/Gluon` and then converted to Keras.

| Model | Top1 | Top5 | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | ---: | --- |
| AlexNet | 44.10 | 21.26 | 61,100,840 | 714.83M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.121/alexnet-2126-56fb1c54.h5.log)) |
| VGG-11 | 31.90 | 11.75 | 132,863,336 | 7,615.87M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.122/vgg11-1175-daa3c646.h5.log)) |
| VGG-13 | 31.06 | 11.12 | 133,047,848 | 11,317.65M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.122/vgg13-1112-90b447ec.h5.log)) |
| VGG-16 | 26.78 | 8.69 | 138,357,544 | 15,507.20M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.122/vgg16-0869-13d19be6.h5.log)) |
| VGG-19 | 25.87 | 8.23 | 143,667,240 | 19,642.55M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.122/vgg19-0823-cab851b8.h5.log)) |
| BN-VGG-11b | 30.34 | 10.57 | 132,868,840 | 7,630.72M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.123/bn_vgg11b-1057-8b6a294a.h5.log)) |
| BN-VGG-13b | 29.48 | 10.16 | 133,053,736 | 11,342.14M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.123/bn_vgg13b-1016-b26cafd3.h5.log)) |
| BN-VGG-16b | 26.88 | 8.65 | 138,365,992 | 15,507.20M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.123/bn_vgg16b-0865-2272fdd1.h5.log)) |
| BN-VGG-19b | 25.65 | 8.14 | 143,678,248 | 19,672.26M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.123/bn_vgg19b-0814-852e2ca2.h5.log)) |
| ResNet-10 | 34.59 | 13.85 | 5,418,792 | 894.04M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.248/resnet10-1385-0a7d3ca6.h5.log)) |
| ResNet-12 | 35.86 | 14.45 | 5,492,776 | 1,126.25M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet12-1445-285da75b.h5.log)) |
| ResNet-14 | 32.85 | 12.42 | 5,788,200 | 1,357.94M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet14-1242-e2ffca6e.h5.log)) |
| ResNet-16 | 30.67 | 11.09 | 6,968,872 | 1,589.34M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet16-1109-8f70f97e.h5.log)) |
| ResNet-18 x0.25 | 49.14 | 24.45 | 831,096 | 137.32M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet18_wd4-2445-dd6ba54d.h5.log)) |
| ResNet-18 x0.5 | 36.54 | 14.96 | 3,055,880 | 486.49M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet18_wd2-1496-9bc78e3b.h5.log)) |
| ResNet-18 x0.75 | 33.24 | 12.54 | 6,675,352 | 1,047.53M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet18_w3d4-1254-f6374cc3.h5.log)) |
| ResNet-18 | 28.08 | 9.52 | 11,689,512 | 1,820.41M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.153/resnet18-0952-0817d058.h5.log)) |
| ResNet-34 | 25.32 | 7.92 | 21,797,672 | 3,672.68M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet34-0792-3ea662f5.h5.log)) |
| ResNet-50 | 22.63 | 6.41 | 25,557,032 | 3,877.95M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.147/resnet50-0641-38a4c231.h5.log)) |
| ResNet-50b | 22.31 | 6.18 | 25,557,032 | 4,110.48M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.146/resnet50b-0618-6be0de5f.h5.log)) |
| ResNet-101 | 21.64 | 5.99 | 44,549,160 | 7,597.95M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.49/resnet101-0599-ab428947.h5.log)) |
| ResNet-101b | 20.78 | 5.39 | 44,549,160 | 7,830.48M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.145/resnet101b-0539-2d572d9b.h5.log)) |
| ResNet-152 | 20.74 | 5.35 | 60,192,808 | 11,321.85M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.144/resnet152-0535-43ecb2b0.h5.log)) |
| ResNet-152b | 20.30 | 5.25 | 60,192,808 | 11,554.38M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.143/resnet152b-0525-c34915fe.h5.log)) |
| PreResNet-10 | 34.65 | 14.01 | 5,417,128 | 894.19M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.249/preresnet10-1401-2349a7c8.h5.log)) |
| PreResNet-18 | 28.16 | 9.52 | 11,687,848 | 1,820.56M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.140/preresnet18-0952-b88bf767.h5.log)) |
| PreResNet-34 | 25.86 | 8.11 | 21,796,008 | 3,672.83M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet34-0811-1663d695.h5.log)) |
| PreResNet-50 | 23.38 | 6.68 | 25,549,480 | 3,875.44M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet50-0668-90326d19.h5.log)) |
| PreResNet-50b | 23.14 | 6.63 | 25,549,480 | 4,107.97M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet50b-0663-c30588ee.h5.log)) |
| PreResNet-101 | 21.43 | 5.75 | 44,541,608 | 7,595.44M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet101-0575-5dff088d.h5.log)) |
| PreResNet-101b | 21.71 | 5.88 | 44,541,608 | 7,827.97M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet101b-0588-fad1f60c.h5.log)) |
| PreResNet-152 | 20.69 | 5.31 | 60,185,256 | 11,319.34M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet152-0531-a5ac128d.h5.log)) |
| PreResNet-152b | 20.99 | 5.76 | 60,185,256 | 11,551.87M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet152b-0576-ea9dda1e.h5.log)) |
| PreResNet-200b | 21.09 | 5.64 | 64,666,280 | 15,068.63M | From [tornadomeet/ResNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.50/preresnet200b-0564-9172d4c0.h5.log)) |
| PreResNet-269b | 20.71 | 5.56 | 102,065,832 | 20,101.11M | From [soeaver/mxnet-model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.239/preresnet269b-0556-bdd89388.h5.log)) |
| ResNeXt-101 (32x4d) | 21.30 | 5.78 | 44,177,704 | 8,003.45M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.51/resnext101_32x4d-0578-7623f640.h5.log)) |
| ResNeXt-101 (64x4d) | 20.59 | 5.41 | 83,455,272 | 15,500.27M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.51/resnext101_64x4d-0541-7b58eaae.h5.log)) |
| SE-ResNet-50 | 22.50 | 6.43 | 28,088,024 | 3,880.49M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.52/seresnet50-0643-fabfa406.h5.log)) |
| SE-ResNet-101 | 21.92 | 5.88 | 49,326,872 | 7,602.76M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.52/seresnet101-0588-933d3415.h5.log)) |
| SE-ResNet-152 | 21.46 | 5.77 | 66,821,848 | 11,328.52M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.52/seresnet152-0577-d25ced7d.h5.log)) |
| SE-ResNeXt-50 (32x4d) | 21.05 | 5.57 | 27,559,896 | 4,258.40M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.53/seresnext50_32x4d-0557-997ef4dd.h5.log)) |
| SE-ResNeXt-101 (32x4d) | 19.98 | 4.99 | 48,955,416 | 8,008.26M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.53/seresnext101_32x4d-0499-59e4e584.h5.log)) |
| SENet-154 | 18.83 | 4.65 | 115,088,984 | 20,745.78M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.54/senet154-0465-962aeede.h5.log)) |
| DenseNet-121 | 25.09 | 7.80 | 7,978,856 | 2,872.13M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.55/densenet121-0780-52b0611c.h5.log)) |
| DenseNet-161 | 22.39 | 6.18 | 28,681,000 | 7,793.16M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.55/densenet161-0618-070fcb45.h5.log)) |
| DenseNet-169 | 23.88 | 6.89 | 14,149,480 | 3,403.89M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.55/densenet169-0689-ae41b4a6.h5.log)) |
| DenseNet-201 | 22.69 | 6.35 | 20,013,928 | 4,347.15M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.55/densenet201-0635-cf3afbb2.h5.log)) |
| DarkNet Tiny | 40.31 | 17.46 | 1,042,104 | 500.85M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.69/darknet_tiny-1746-147e949b.h5.log)) |
| DarkNet Ref | 37.99 | 16.68 | 7,319,416 | 367.59M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.64/darknet_ref-1668-2ef080bb.h5.log)) |
| DarkNet-53 | 21.43 | 5.56 | 41,609,928 | 7,133.86M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.150/darknet53-0556-d6c6e7dc.h5.log)) |
| SqueezeNet v1.0 | 39.17 | 17.56 | 1,248,424 | 823.67M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.128/squeezenet_v1_0-1756-a4890923.h5.log)) |
| SqueezeNet v1.1 | 39.08 | 17.39 | 1,235,496 | 352.02M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.88/squeezenet_v1_1-1739-b9a8f9ea.h5.log)) |
| SqueezeResNet v1.0 | 39.40 | 17.80 | 1,248,424 | 823.67M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.178/squeezeresnet_v1_0-1780-fb9a54aa.h5.log)) |
| SqueezeResNet v1.1 | 39.82 | 17.84 | 1,235,496 | 352.02M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.70/squeezeresnet_v1_1-1784-43ee9cbb.h5.log)) |
| 1.0-SqNxt-23 | 42.28 | 18.62 | 724,056 | 287.28M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.171/sqnxt23_w1-1862-cab60636.h5.log)) |
| 1.0-SqNxt-23v5 | 40.38 | 17.57 | 921,816 | 285.82M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.172/sqnxt23v5_w1-1757-96b94e1d.h5.log)) |
| 1.5-SqNxt-23 | 34.59 | 13.30 | 1,511,824 | 552.39M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.210/sqnxt23_w3d2-1330-e52625a0.h5.log)) |
| 1.5-SqNxt-23v5 | 33.56 | 12.84 | 1,953,616 | 550.97M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.212/sqnxt23v5_w3d2-1284-fd150fcc.h5.log)) |
| 2.0-SqNxt-23 | 30.15 | 10.66 | 2,583,752 | 898.48M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.240/sqnxt23_w2-1066-a34e73b9.h5.log)) |
| 2.0-SqNxt-23v5 | 29.40 | 10.28 | 3,366,344 | 897.60M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.216/sqnxt23v5_w2-1028-13c5a598.h5.log)) |
| ShuffleNet x0.25 (g=1) | 62.00 | 36.76 | 209,746 | 12.35M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.134/shufflenet_g1_wd4-3676-cb39b773.h5.log)) |
| ShuffleNet x0.25 (g=3) | 61.32 | 36.15 | 305,902 | 13.09M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.135/shufflenet_g3_wd4-3615-21150468.h5.log)) |
| ShuffleNet x0.5 (g=1) | 46.21 | 22.38 | 534,484 | 41.16M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.174/shufflenet_g1_wd2-2238-76709a36.h5.log)) |
| ShuffleNet x0.5 (g=3) | 43.82 | 20.60 | 718,324 | 41.70M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.167/shufflenet_g3_wd2-2060-173a725c.h5.log)) |
| ShuffleNet x0.75 (g=1) | 39.24 | 16.75 | 975,214 | 86.42M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.218/shufflenet_g1_w3d4-1675-56aa4179.h5.log)) |
| ShuffleNet x0.75 (g=3) | 37.81 | 16.09 | 1,238,266 | 85.82M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.219/shufflenet_g3_w3d4-1609-34e28781.h5.log)) |
| ShuffleNet x1.0 (g=1) | 34.41 | 13.50 | 1,531,936 | 148.13M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.223/shufflenet_g1_w1-1350-f44c8a18.h5.log)) |
| ShuffleNet x1.0 (g=2) | 33.97 | 13.32 | 1,733,848 | 147.60M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.241/shufflenet_g2_w1-1332-8784a32b.h5.log)) |
| ShuffleNet x1.0 (g=3) | 33.96 | 13.29 | 1,865,728 | 145.46M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.244/shufflenet_g3_w1-1329-0e213e76.h5.log)) |
| ShuffleNet x1.0 (g=4) | 33.83 | 13.10 | 1,968,344 | 143.33M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.245/shufflenet_g4_w1-1310-ef2ff63e.h5.log)) |
| ShuffleNet x1.0 (g=8) | 33.64 | 13.20 | 2,434,768 | 150.76M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.250/shufflenet_g8_w1-1320-796314f1.h5.log)) |
| ShuffleNetV2 x0.5 | 40.76 | 18.40 | 1,366,792 | 43.31M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.90/shufflenetv2_wd2-1840-9b4b0964.h5.log)) |
| ShuffleNetV2 x1.0 | 31.02 | 11.33 | 2,278,604 | 149.72M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.133/shufflenetv2_w1-1133-bcba973e.h5.log)) |
| ShuffleNetV2 x1.5 | 32.46 | 12.47 | 4,406,098 | 320.77M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.65/shufflenetv2_w3d2-1247-f7f813b4.h5.log)) |
| ShuffleNetV2 x2.0 | 31.91 | 12.23 | 7,601,686 | 595.84M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.84/shufflenetv2_w2-1223-63291468.h5.log)) |
| ShuffleNetV2b x0.5 | 39.81 | 17.83 | 1,366,792 | 43.31M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.211/shufflenetv2b_wd2-1783-ca8409ae.h5.log)) |
| ShuffleNetV2b x1.0 | 30.38 | 11.01 | 2,279,760 | 150.62M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.211/shufflenetv2b_w1-1101-1caf1b22.h5.log)) |
| ShuffleNetV2b x1.5 | 26.89 | 8.80 | 4,410,194 | 323.98M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.211/shufflenetv2b_w3d2-0880-265c3c7c.h5.log)) |
| ShuffleNetV2b x2.0 | 25.18 | 8.10 | 7,611,290 | 603.37M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.242/shufflenetv2b_w2-0810-2149df38.h5.log)) |
| 108-MENet-8x1 (g=3) | 43.61 | 20.31 | 654,516 | 42.68M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.89/menet108_8x1_g3-2031-a4d43433.h5.log)) |
| 128-MENet-8x1 (g=4) | 42.08 | 19.14 | 750,796 | 45.98M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.103/menet128_8x1_g4-1914-5bb8f228.h5.log)) |
| 160-MENet-8x1 (g=8) | 43.47 | 20.28 | 850,120 | 45.63M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.154/menet160_8x1_g8-2028-09664de9.h5.log)) |
| 228-MENet-12x1 (g=3) | 33.85 | 12.88 | 1,806,568 | 152.93M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.131/menet228_12x1_g3-1288-c2eeac24.h5.log)) |
| 256-MENet-12x1 (g=4) | 32.22 | 12.17 | 1,888,240 | 150.65M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.152/menet256_12x1_g4-1217-b020cc33.h5.log)) |
| 348-MENet-12x1 (g=3) | 27.85 | 9.36 | 3,368,128 | 312.00M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.173/menet348_12x1_g3-0936-6795f007.h5.log)) |
| 352-MENet-12x1 (g=8) | 31.29 | 11.67 | 2,272,872 | 157.35M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.198/menet352_12x1_g8-1167-a9d9412d.h5.log)) |
| 456-MENet-24x1 (g=3) | 25.00 | 7.80 | 5,304,784 | 567.90M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.237/menet456_24x1_g3-0780-6645f594.h5.log)) |
| MobileNet x0.25 | 45.80 | 22.17 | 470,072 | 44.09M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.62/mobilenet_wd4-2217-fb7abda8.h5.log)) |
| MobileNet x0.5 | 33.94 | 13.30 | 1,331,592 | 155.42M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.156/mobilenet_wd2-1330-aa86f355.h5.log)) |
| MobileNet x0.75 | 29.85 | 10.51 | 2,585,560 | 333.99M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.130/mobilenet_w3d4-1051-d200ad45.h5.log)) |
| MobileNet x1.0 | 26.43 | 8.66 | 4,231,976 | 579.80M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.155/mobilenet_w1-0866-9661b555.h5.log)) |
| FD-MobileNet x0.25 | 55.42 | 30.52 | 383,160 | 12.95M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.177/fdmobilenet_wd4-3052-6c219205.h5.log)) |
| FD-MobileNet x0.5 | 42.61 | 19.69 | 993,928 | 41.84M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.83/fdmobilenet_wd2-1969-5678a212.h5.log)) |
| FD-MobileNet x0.75 | 37.90 | 16.01 | 1,833,304 | 86.68M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.159/fdmobilenet_w3d4-1601-2ea5eba9.h5.log)) |
| FD-MobileNet x1.0 | 33.80 | 13.12 | 2,901,288 | 147.46M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.162/fdmobilenet_w1-1312-e11d0dce.h5.log)) |
| MobileNetV2 x0.25 | 48.06 | 24.12 | 1,516,392 | 34.24M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.137/mobilenetv2_wd4-2412-62273372.h5.log)) |
| MobileNetV2 x0.5 | 35.63 | 14.43 | 1,964,736 | 100.13M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.170/mobilenetv2_wd2-1443-c7086bcc.h5.log)) |
| MobileNetV2 x0.75 | 29.76 | 10.44 | 2,627,592 | 198.50M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.230/mobilenetv2_w3d4-1044-29e9923c.h5.log)) |
| MobileNetV2 x1.0 | 26.76 | 8.64 | 3,504,960 | 329.36M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.213/mobilenetv2_w1-0864-5e487e82.h5.log)) |
| IGCV3 x0.25 | 53.41 | 28.29 | 1,534,020 | 41.29M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.142/igcv3_wd4-2829-00072caf.h5.log)) |
| IGCV3 x0.5 | 39.39 | 17.04 | 1,985,528 | 111.12M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.132/igcv3_wd2-1704-b8961ca3.h5.log)) |
| IGCV3 x0.75 | 30.71 | 10.97 | 2,638,084 | 210.95M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.207/igcv3_w3d4-1097-fb365b72.h5.log)) |
| IGCV3 x1.0 | 27.72 | 8.99 | 3,491,688 | 340.79M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.243/igcv3_w1-0899-968237cb.h5.log)) |
| MnasNet | 31.30 | 11.45 | 4,308,816 | 317.67M | From [zeusees/Mnasnet...Model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.117/mnasnet-1145-11b6acf1.h5.log)) |

[dmlc/gluon-cv]: https://github.com/dmlc/gluon-cv
[tornadomeet/ResNet]: https://github.com/tornadomeet/ResNet
[Cadene/pretrained...pytorch]: https://github.com/Cadene/pretrained-models.pytorch
[clavichord93/MENet]: https://github.com/clavichord93/MENet
[zeusees/Mnasnet...Model]: https://github.com/zeusees/Mnasnet-Pretrained-Model
[soeaver/mxnet-model]: https://github.com/soeaver/mxnet-model