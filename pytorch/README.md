# Image classification models on PyTorch

[![PyPI](https://img.shields.io/pypi/v/pytorchcv.svg)](https://pypi.python.org/pypi/pytorchcv)
[![Downloads](https://pepy.tech/badge/pytorchcv)](https://pepy.tech/project/pytorchcv)

This is a collection of image classification models. Many of them are pretrained on ImageNet-1K and CIFAR-10/100
datasets and loaded automatically during use. All pretrained models require the same ordinary normalization.
Scripts for training/evaluating/converting models are in the [`imgclsmob`](https://github.com/osmr/imgclsmob) repo.

## List of implemented models

- AlexNet (['One weird trick for parallelizing convolutional neural networks'](https://arxiv.org/abs/1404.5997))
- ZFNet (['Visualizing and Understanding Convolutional Networks'](https://arxiv.org/abs/1311.2901))
- VGG/BN-VGG (['Very Deep Convolutional Networks for Large-Scale Image Recognition'](https://arxiv.org/abs/1409.1556))
- BN-Inception (['Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift'](https://arxiv.org/abs/1502.03167))
- ResNet (['Deep Residual Learning for Image Recognition'](https://arxiv.org/abs/1512.03385))
- PreResNet (['Identity Mappings in Deep Residual Networks'](https://arxiv.org/abs/1603.05027))
- ResNeXt (['Aggregated Residual Transformations for Deep Neural Networks'](http://arxiv.org/abs/1611.05431))
- SENet/SE-ResNet/SE-PreResNet/SE-ResNeXt (['Squeeze-and-Excitation Networks'](https://arxiv.org/abs/1709.01507))
- IBN-ResNet/IBN-ResNeXt/IBN-DenseNet (['Two at Once: Enhancing Learning and Generalization Capacities via IBN-Net'](https://arxiv.org/abs/1807.09441))
- AirNet/AirNeXt (['Attention Inspiring Receptive-Fields Network for Learning Invariant Representations'](https://ieeexplore.ieee.org/document/8510896))
- BAM-ResNet (['BAM: Bottleneck Attention Module'](https://arxiv.org/abs/1807.06514))
- CBAM-ResNet (['CBAM: Convolutional Block Attention Module'](https://arxiv.org/abs/1807.06521))
- ResAttNet (['Residual Attention Network for Image Classification'](https://arxiv.org/abs/1704.06904))
- PyramidNet (['Deep Pyramidal Residual Networks'](https://arxiv.org/abs/1610.02915))
- DiracNetV2 (['DiracNets: Training Very Deep Neural Networks Without Skip-Connections'](https://arxiv.org/abs/1706.00388))
- ShaResNet (['ShaResNet: reducing residual network parameter number by sharing weights'](https://arxiv.org/abs/1702.08782))
- DenseNet (['Densely Connected Convolutional Networks'](https://arxiv.org/abs/1608.06993))
- CondenseNet (['CondenseNet: An Efficient DenseNet using Learned Group Convolutions'](https://arxiv.org/abs/1711.09224))
- SparseNet (['Sparsely Aggregated Convolutional Networks'](https://arxiv.org/abs/1801.05895))
- PeleeNet (['Pelee: A Real-Time Object Detection System on Mobile Devices'](https://arxiv.org/abs/1804.06882))
- WRN (['Wide Residual Networks'](https://arxiv.org/abs/1605.07146))
- DRN-C/DRN-D (['Dilated Residual Networks'](https://arxiv.org/abs/1705.09914))
- DPN (['Dual Path Networks'](https://arxiv.org/abs/1707.01629))
- DarkNet Ref/Tiny/19 (['Darknet: Open source neural networks in c'](https://github.com/pjreddie/darknet))
- DarkNet-53 (['YOLOv3: An Incremental Improvement'](https://arxiv.org/abs/1804.02767))
- ChannelNet (['ChannelNets: Compact and Efficient Convolutional Neural Networks via Channel-Wise Convolutions'](https://arxiv.org/abs/1809.01330))
- iSQRT-COV-ResNet (['Towards Faster Training of Global Covariance Pooling Networks by Iterative Matrix Square Root Normalization'](https://arxiv.org/abs/1712.01034))
- i-RevNet (['i-RevNet: Deep Invertible Networks'](https://arxiv.org/abs/1802.07088))
- DLA (['Deep Layer Aggregation'](https://arxiv.org/abs/1707.06484))
- MSDNet (['Multi-Scale Dense Networks for Resource Efficient Image Classification'](https://arxiv.org/abs/1703.09844))
- FishNet (['FishNet: A Versatile Backbone for Image, Region, and Pixel Level Prediction'](http://papers.nips.cc/paper/7356-fishnet-a-versatile-backbone-for-image-region-and-pixel-level-prediction.pdf))
- ESPNetv2 (['ESPNetv2: A Light-weight, Power Efficient, and General Purpose Convolutional Neural Network'](https://arxiv.org/abs/1811.11431))
- X-DenseNet (['Deep Expander Networks: Efficient Deep Networks from Graph Theory'](https://arxiv.org/abs/1711.08757))
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
- DARTS (['DARTS: Differentiable Architecture Search'](https://arxiv.org/abs/1806.09055))
- Xception (['Xception: Deep Learning with Depthwise Separable Convolutions'](https://arxiv.org/abs/1610.02357))
- InceptionV3 (['Rethinking the Inception Architecture for Computer Vision'](https://arxiv.org/abs/1512.00567))
- InceptionV4/InceptionResNetV2 (['Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning'](https://arxiv.org/abs/1602.07261))
- PolyNet (['PolyNet: A Pursuit of Structural Diversity in Very Deep Networks'](https://arxiv.org/abs/1611.05725))
- NASNet (['Learning Transferable Architectures for Scalable Image Recognition'](https://arxiv.org/abs/1707.07012))
- PNASNet (['Progressive Neural Architecture Search'](https://arxiv.org/abs/1712.00559))
- NIN (['Network In Network'](https://arxiv.org/abs/1312.4400))
- RoR-3 (['Residual Networks of Residual Networks: Multilevel Residual Networks'](https://arxiv.org/abs/1608.02908))
- RiR (['Resnet in Resnet: Generalizing Residual Architectures'](https://arxiv.org/abs/1603.08029))
- ResDrop-ResNet (['Deep Networks with Stochastic Depth'](https://arxiv.org/abs/1603.09382))
- Shake-Shake-ResNet (['Shake-Shake regularization'](https://arxiv.org/abs/1705.07485))
- ShakeDrop-ResNet (['ShakeDrop Regularization for Deep Residual Learning'](https://arxiv.org/abs/1802.02375))
- FractalNet (['FractalNet: Ultra-Deep Neural Networks without Residuals'](https://arxiv.org/abs/1605.07648))

## Installation

To use the models in your project, simply install the `pytorchcv` package with `torch` (>=0.4.1 is recommended):
```
pip install pytorchcv torch>=0.4.0
```
To enable/disable different hardware supports such as GPUs, check out PyTorch installation [instructions](https://pytorch.org).

## Usage

Example of using a pretrained ResNet-18 model:
```
from pytorchcv.model_provider import get_model as ptcv_get_model
import torch
from torch.autograd import Variable

net = ptcv_get_model("resnet18", pretrained=True)
x = Variable(torch.randn(1, 3, 224, 224))
y = net(x)
```

## Pretrained models

### Imagenet-1K

Some remarks:
- Top1/Top5 are the standard 1-crop Top-1/Top-5 errors (in percents) on the validation subset of the ImageNet-1K dataset.
- FLOPs/2 is the number of FLOPs divided by two to be similar to the number of MACs.
- Remark `Converted from GL model` means that the model was trained on `MXNet/Gluon` and then converted to PyTorch.
- You may notice that quality estimations are quite different from ones for the corresponding models in other frameworks. This
is due to the fact that the quality is estimated on the standard TorchVision stack of image transformations. Using
OpenCV `Resize` transformation instead of PIL one quality evaluation results will be similar to ones for the Gluon models.

| Model | Top1 | Top5 | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | ---: | --- |
| AlexNet | 43.48 | 20.93 | 61,100,840 | 714.83M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.108/alexnet-2093-6429d865.pth.log)) |
| VGG-11 | 30.98 | 11.37 | 132,863,336 | 7,615.87M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg11-1137-8a64fe7a.pth.log)) |
| VGG-13 | 30.07 | 10.75 | 133,047,848 | 11,317.65M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg13-1075-24178cab.pth.log)) |
| VGG-16 | 27.15 | 8.92 | 138,357,544 | 15,480.10M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg16-0892-10f44f68.pth.log)) |
| VGG-19 | 26.19 | 8.39 | 143,667,240 | 19,642.55M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg19-0839-d4e69a0d.pth.log)) |
| BN-VGG-11b | 29.63 | 10.19 | 132,868,840 | 7,630.72M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg11b-1019-98d7e914.pth.log)) |
| BN-VGG-13b | 28.41 | 9.63 | 133,053,736 | 11,342.14M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg13b-0963-cf9352f4.pth.log)) |
| BN-VGG-16b | 27.19 | 8.74 | 138,365,992 | 15,507.20M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg16b-0874-af4f2d0b.pth.log)) |
| BN-VGG-19b | 26.06 | 8.40 | 143,678,248 | 19,672.26M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg19b-0840-b6919f7f.pth.log)) |
| BN-Inception | 25.39 | 8.04 | 11,295,240 | 2,048.06M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.139/bninception-0804-99ff8708.pth.log)) |
| ResNet-10 | 34.69 | 14.36 | 5,418,792 | 894.04M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.248/resnet10-1436-67d9a618.pth.log)) |
| ResNet-12 | 36.18 | 14.80 | 5,492,776 | 1,126.25M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.30/resnet12-1480-c2263f73.pth.log)) |
| ResNet-14 | 33.17 | 12.71 | 5,788,200 | 1,357.94M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.40/resnet14-1271-568c392e.pth.log)) |
| ResNet-16 | 30.90 | 11.38 | 6,968,872 | 1,589.34M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.41/resnet16-1138-3a5aa7c0.pth.log)) |
| ResNet-18 x0.25 | 49.50 | 24.83 | 831,096 | 137.32M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.47/resnet18_wd4-2483-6ef2515c.pth.log)) |
| ResNet-18 x0.5 | 37.04 | 15.38 | 3,055,880 | 486.49M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.46/resnet18_wd2-1538-671466b5.pth.log)) |
| ResNet-18 x0.75 | 33.61 | 12.85 | 6,675,352 | 1,047.53M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.18/resnet18_w3d4-1285-94713e0e.pth.log)) |
| ResNet-18 | 28.53 | 9.82 | 11,689,512 | 1,820.41M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.153/resnet18-0982-0126861b.pth.log)) |
| ResNet-34 | 25.66 | 8.18 | 21,797,672 | 3,672.68M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.1/resnet34-0818-6f947d40.pth.log)) |
| ResNet-50 | 22.96 | 6.58 | 25,557,032 | 3,877.95M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.147/resnet50-0658-828686d7.pth.log)) |
| ResNet-50b | 22.61 | 6.45 | 25,557,032 | 4,110.48M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.146/resnet50b-0645-a53df64c.pth.log)) |
| ResNet-101 | 21.90 | 6.22 | 44,549,160 | 7,597.95M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.1/resnet101-0622-ab0cf005.pth.log)) |
| ResNet-101b | 20.88 | 5.61 | 44,549,160 | 7,830.48M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.145/resnet101b-0561-9fbf0696.pth.log)) |
| ResNet-152 | 21.01 | 5.50 | 60,192,808 | 11,321.85M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.144/resnet152-0550-800b2cb1.pth.log)) |
| ResNet-152b | 20.56 | 5.34 | 60,192,808 | 11,554.38M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.143/resnet152b-0534-e02a8bf7.pth.log)) |
| PreResNet-10 | 35.11 | 14.21 | 5,417,128 | 894.19M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.249/preresnet10-1421-b3973cd4.pth.log)) |
| PreResNet-18 | 28.43 | 9.72 | 11,687,848 | 1,820.56M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.140/preresnet18-0972-5651bc2d.pth.log)) |
| PreResNet-34 | 26.23 | 8.41 | 21,796,008 | 3,672.83M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet34-0841-b4dd761f.pth.log)) |
| PreResNet-50 | 23.70 | 6.85 | 25,549,480 | 3,875.44M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet50-0685-d81a7aca.pth.log)) |
| PreResNet-50b | 23.33 | 6.87 | 25,549,480 | 4,107.97M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet50b-0687-65be98fb.pth.log)) |
| PreResNet-101 | 21.74 | 5.91 | 44,541,608 | 7,595.44M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet101-0591-4bacff79.pth.log)) |
| PreResNet-101b | 21.95 | 6.03 | 44,541,608 | 7,827.97M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet101b-0603-b1e37a09.pth.log)) |
| PreResNet-152 | 20.94 | 5.55 | 60,185,256 | 11,319.34M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.14/preresnet152-0555-c842a030.pth.log)) |
| PreResNet-152b | 21.34 | 5.91 | 60,185,256 | 11,551.87M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet152b-0591-2c91ab2c.pth.log)) |
| PreResNet-200b | 21.33 | 5.88 | 64,666,280 | 15,068.63M | From [tornadomeet/ResNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.45/preresnet200b-0588-f7104ff3.pth.log)) |
| PreResNet-269b | 20.92 | 5.81 | 102,065,832 | 20,101.11M | From [soeaver/mxnet-model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.239/preresnet269b-0581-1a7878bb.pth.log)) |
| ResNeXt-101 (32x4d) | 21.81 | 6.11 | 44,177,704 | 8,003.45M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.10/resnext101_32x4d-0611-cf962440.pth.log)) |
| ResNeXt-101 (64x4d) | 21.04 | 5.75 | 83,455,272 | 15,500.27M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.10/resnext101_64x4d-0575-651abd02.pth.log)) |
| SE-ResNet-50 | 22.47 | 6.40 | 28,088,024 | 3,880.49M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet50-0640-8820f2af.pth.log)) |
| SE-ResNet-101 | 21.88 | 5.89 | 49,326,872 | 7,602.76M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet101-0589-5e6e831b.pth.log)) |
| SE-ResNet-152 | 21.48 | 5.76 | 66,821,848 | 11,328.52M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet152-0576-814cf72e.pth.log)) |
| SE-ResNeXt-50 (32x4d) | 21.00 | 5.54 | 27,559,896 | 4,258.40M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.12/seresnext50_32x4d-0554-99e0e9aa.pth.log)) |
| SE-ResNeXt-101 (32x4d) | 19.96 | 5.05 | 48,955,416 | 8,008.26M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.12/seresnext101_32x4d-0505-0924f0a2.pth.log)) |
| SENet-154 | 18.62 | 4.61 | 115,088,984 | 20,745.78M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.13/senet154-0461-6512228c.pth.log)) |
| IBN-ResNet-50 | 22.76 | 6.41 | 25,557,032 | 4,110.48M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnet50-0641-e48a1fe5.pth.log)) |
| IBN-ResNet-101 | 21.29 | 5.61 | 44,549,160 | 7,830.48M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnet101-0561-5279c78a.pth.log)) |
| IBN(b)-ResNet-50 | 23.64 | 6.86 | 25,558,568 | 4,112.89M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibnb_resnet50-0686-e138995e.pth.log)) |
| IBN-ResNeXt-101 (32x4d) | 20.88 | 5.42 | 44,177,704 | 8,003.45M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnext101_32x4d-0542-b5233c66.pth.log)) |
| IBN-DenseNet-121 | 24.47 | 7.25 | 7,978,856 | 2,872.13M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_densenet121-0725-b90b0615.pth.log)) |
| IBN-DenseNet-169 | 23.25 | 6.51 | 14,149,480 | 3,403.89M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_densenet169-0651-96dd755e.pth.log)) |
| AirNet50-1x64d (r=2) | 21.84 | 5.90 | 27,425,864 | 4,772.11M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnet50_1x64d_r2-0590-3ec42212.pth.log)) |
| AirNet50-1x64d (r=16) | 22.11 | 6.19 | 25,714,952 | 4,399.97M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnet50_1x64d_r16-0619-090179e7.pth.log)) |
| AirNeXt50-32x4d (r=2) | 20.87 | 5.51 | 27,604,296 | 5,339.58M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnext50_32x4d_r2-0551-c68156e5.pth.log)) |
| BAM-ResNet-50 | 23.14 | 6.58 | 25,915,099 | 4,196.09M | From [Jongchan/attention-module] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.124/bam_resnet50-0658-96a37c82.pth.log)) |
| CBAM-ResNet-50 | 22.38 | 6.05 | 28,089,624 | 4,116.97M | From [Jongchan/attention-module] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.125/cbam_resnet50-0605-a1172fe6.pth.log)) |
| PyramidNet-101 (a=360) | 21.98 | 6.20 | 42,455,070 | 8,743.54M | From [dyhan0920/Pyramid...PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.104/pyramidnet101_a360-0620-3a24427b.pth.log)) |
| DiracNetV2-18 | 31.47 | 11.70 | 11,511,784 | 1,796.62M | From [szagoruyko/diracnets] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.111/diracnet18v2-1170-e0673770.pth.log)) |
| DiracNetV2-34 | 28.75 | 9.93 | 21,616,232 | 3,646.93M | From [szagoruyko/diracnets] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.111/diracnet34v2-0993-a6a661c0.pth.log)) |
| DenseNet-121 | 25.57 | 8.03 | 7,978,856 | 2,872.13M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet121-0803-f994107a.pth.log)) |
| DenseNet-161 | 22.86 | 6.44 | 28,681,000 | 7,793.16M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet161-0644-c0fb22c8.pth.log)) |
| DenseNet-169 | 24.40 | 7.19 | 14,149,480 | 3,403.89M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet169-0719-27139105.pth.log)) |
| DenseNet-201 | 23.10 | 6.63 | 20,013,928 | 4,347.15M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet201-0663-71ece4ad.pth.log)) |
| CondenseNet-74 (C=G=4) | 26.25 | 8.28 | 4,773,944 | 546.06M | From [ShichenLiu/CondenseNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.4/condensenet74_c4_g4-0828-5ba55049.pth.log)) |
| CondenseNet-74 (C=G=8) | 28.93 | 10.06 | 2,935,416 | 291.52M | From [ShichenLiu/CondenseNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.4/condensenet74_c8_g8-1006-3574d874.pth.log)) |
| PeleeNet | 31.81 | 11.51 | 2,802,248 | 514.87M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.141/peleenet-1151-9c47b802.pth.log)) |
| WRN-50-2 | 22.53 | 6.41 | 68,849,128 | 11,405.42M | From [szagoruyko/functional-zoo] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.113/wrn50_2-0641-83897ab9.pth.log)) |
| DRN-C-26 | 24.86 | 7.55 | 21,126,584 | 16,993.90M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc26-0755-35405bd5.pth.log)) |
| DRN-C-42 | 22.94 | 6.57 | 31,234,744 | 25,093.75M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc42-0657-7c99c460.pth.log)) |
| DRN-C-58 | 21.73 | 6.01 | 40,542,008 | 32,489.94M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc58-0601-70ec1f56.pth.log)) |
| DRN-D-22 | 25.80 | 8.23 | 16,393,752 | 13,051.33M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd22-0823-5c2c6a0c.pth.log)) |
| DRN-D-38 | 23.79 | 6.95 | 26,501,912 | 21,151.19M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd38-0695-4630f0fb.pth.log)) |
| DRN-D-54 | 21.22 | 5.86 | 35,809,176 | 28,547.38M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd54-0586-bfdc1f88.pth.log)) |
| DRN-D-105 | 20.62 | 5.48 | 54,801,304 | 43,442.43M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd105-0548-a643f4dc.pth.log)) |
| DPN-68 | 24.17 | 7.27 | 12,611,602 | 2,351.84M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn68-0727-43849233.pth.log)) |
| DPN-98 | 20.81 | 5.53 | 61,570,728 | 11,716.51M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn98-0553-52c55969.pth.log)) |
| DPN-131 | 20.54 | 5.48 | 79,254,504 | 16,076.15M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn131-0548-0c53e5b3.pth.log)) |
| DarkNet Tiny | 40.74 | 17.84 | 1,042,104 | 500.85M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.69/darknet_tiny-1784-4561e1ad.pth.log)) |
| DarkNet Ref | 38.58 | 17.18 | 7,319,416 | 367.59M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.64/darknet_ref-1718-034595b4.pth.log)) |
| DarkNet-53 | 21.75 | 5.64 | 41,609,928 | 7,133.86M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.150/darknet53-0564-b36bef6b.pth.log)) |
| i-RevNet-301 | 25.98 | 8.41 | 125,120,356 | 14,453.87M | From [jhjacobsen/pytorch-i-revnet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.251/irevnet301-0841-95dc8d94.pth.log)) |
| DLA-34 | 25.36 | 7.94 | 15,742,104 | 3,071.37M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla34-0794-04698d78.pth.log)) |
| DLA-46-C | 35.12 | 13.71 | 1,301,400 | 585.45M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla46c-1371-cc919179.pth.log)) |
| DLA-X-46-C | 34.02 | 13.02 | 1,068,440 | 546.72M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla46xc-1302-1161f37b.pth.log)) |
| DLA-60 | 22.98 | 6.69 | 22,036,632 | 4,255.49M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60-0669-b2cd6e51.pth.log)) |
| DLA-X-60 | 21.76 | 5.98 | 17,352,344 | 3,543.68M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60x-0598-88547d3f.pth.log)) |
| DLA-X-60-C | 32.09 | 11.57 | 1,319,832 | 596.06M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60xc-1157-c413bb80.pth.log)) |
| DLA-102 | 21.97 | 6.05 | 33,268,888 | 7,190.95M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102-0605-11df1322.pth.log)) |
| DLA-X-102 | 21.49 | 5.77 | 26,309,272 | 5,884.94M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102x-0577-58331655.pth.log)) |
| DLA-X2-102 | 20.55 | 5.36 | 41,282,200 | 9,340.61M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102x2-0536-07936111.pth.log)) |
| DLA-169 | 21.29 | 5.66 | 53,389,720 | 11,593.20M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla169-0566-ae0c6a82.pth.log)) |
| FishNet-150 | 21.97 | 6.04 | 24,959,400 | 6,435.05M | From [kevin-ssy/FishNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.168/fishnet150-0604-f5af4873.pth.log)) |
| ESPNetv2 x0.5 | 42.32 | 20.15 | 1,241,332 | 35.36M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_wd2-2015-d234781f.pth.log)) |
| ESPNetv2 x1.0 | 33.92 | 13.45 | 1,670,072 | 98.09M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w1-1345-550d5422.pth.log)) |
| ESPNetv2 x1.25 | 32.06 | 12.18 | 1,965,440 | 138.18M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w5d4-1218-85d97b2b.pth.log)) |
| ESPNetv2 x1.5 | 30.83 | 11.29 | 2,314,856 | 185.77M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w3d2-1129-3bbb49ad.pth.log)) |
| ESPNetv2 x2.0 | 27.94 | 9.61 | 3,498,136 | 306.93M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w2-0961-13ba0f72.pth.log)) |
| SqueezeNet v1.0 | 39.29 | 17.66 | 1,248,424 | 823.67M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.128/squeezenet_v1_0-1766-afdbcf1a.pth.log)) |
| SqueezeNet v1.1 | 39.31 | 17.72 | 1,235,496 | 352.02M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.88/squeezenet_v1_1-1772-25b77bc3.pth.log)) |
| SqueezeResNet v1.0 | 39.77 | 18.09 | 1,248,424 | 823.67M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.178/squeezeresnet_v1_0-1809-25bfc02e.pth.log)) |
| SqueezeResNet v1.1 | 40.09 | 18.21 | 1,235,496 | 352.02M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.70/squeezeresnet_v1_1-1821-c27ed88f.pth.log)) |
| 1.0-SqNxt-23 | 42.51 | 19.06 | 724,056 | 287.28M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.171/sqnxt23_w1-1906-97b74e0c.pth.log)) |
| 1.0-SqNxt-23v5 | 40.77 | 17.85 | 921,816 | 285.82M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.172/sqnxt23v5_w1-1785-2fe3ad67.pth.log)) |
| 1.5-SqNxt-23 | 34.89 | 13.50 | 1,511,824 | 552.39M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.210/sqnxt23_w3d2-1350-c2f21bce.pth.log)) |
| 1.5-SqNxt-23v5 | 33.81 | 13.01 | 1,953,616 | 550.97M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.212/sqnxt23v5_w3d2-1301-c244844b.pth.log)) |
| 2.0-SqNxt-23 | 30.62 | 11.00 | 2,583,752 | 898.48M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.240/sqnxt23_w2-1100-b9bb7302.pth.log)) |
| 2.0-SqNxt-23v5 | 29.63 | 10.66 | 3,366,344 | 897.60M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.216/sqnxt23v5_w2-1066-229b0d3d.pth.log)) |
| ShuffleNet x0.25 (g=1) | 62.44 | 37.29 | 209,746 | 12.35M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.134/shufflenet_g1_wd4-3729-47dbd0f2.pth.log)) |
| ShuffleNet x0.25 (g=3) | 61.74 | 36.53 | 305,902 | 13.09M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.135/shufflenet_g3_wd4-3653-6abdd65e.pth.log)) |
| ShuffleNet x0.5 (g=1) | 46.59 | 22.61 | 534,484 | 41.16M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.174/shufflenet_g1_wd2-2261-dae4bdad.pth.log)) |
| ShuffleNet x0.5 (g=3) | 44.16 | 20.80 | 718,324 | 41.70M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.167/shufflenet_g3_wd2-2080-ccaacfc8.pth.log)) |
| ShuffleNet x0.75 (g=1) | 39.58 | 17.11 | 975,214 | 86.42M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.218/shufflenet_g1_w3d4-1711-161cd24a.pth.log)) |
| ShuffleNet x0.75 (g=3) | 38.20 | 16.50 | 1,238,266 | 85.82M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.219/shufflenet_g3_w3d4-1650-3f3b0aef.pth.log)) |
| ShuffleNet x1.0 (g=1) | 34.93 | 13.89 | 1,531,936 | 148.13M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.223/shufflenet_g1_w1-1389-4cfb65a3.pth.log)) |
| ShuffleNet x1.0 (g=2) | 34.25 | 13.63 | 1,733,848 | 147.60M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.241/shufflenet_g2_w1-1363-07256203.pth.log)) |
| ShuffleNet x1.0 (g=3) | 34.39 | 13.48 | 1,865,728 | 145.46M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.244/shufflenet_g3_w1-1348-ce54f64e.pth.log)) |
| ShuffleNet x1.0 (g=4) | 34.19 | 13.35 | 1,968,344 | 143.33M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.245/shufflenet_g4_w1-1335-e2415f82.pth.log)) |
| ShuffleNet x1.0 (g=8) | 34.06 | 13.42 | 2,434,768 | 150.76M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.250/shufflenet_g8_w1-1342-9a979b36.pth.log)) |
| ShuffleNetV2 x0.5 | 40.99 | 18.65 | 1,366,792 | 43.31M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.90/shufflenetv2_wd2-1865-9c22238b.pth.log)) |
| ShuffleNetV2 x1.0 | 31.44 | 11.63 | 2,278,604 | 149.72M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.133/shufflenetv2_w1-1163-c71dfb7a.pth.log)) |
| ShuffleNetV2 x1.5 | 32.82 | 12.69 | 4,406,098 | 320.77M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.65/shufflenetv2_w3d2-1269-536ad5b1.pth.log)) |
| ShuffleNetV2 x2.0 | 32.45 | 12.49 | 7,601,686 | 595.84M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.84/shufflenetv2_w2-1249-b9f9e84c.pth.log)) |
| ShuffleNetV2b x0.5 | 40.29 | 18.22 | 1,366,792 | 43.31M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.157/shufflenetv2b_wd2-1822-01d18d6f.pth.log)) |
| ShuffleNetV2b x1.0 | 30.62 | 11.25 | 2,279,760 | 150.62M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.161/shufflenetv2b_w1-1125-6a5d3dc4.pth.log)) |
| ShuffleNetV2b x1.5 | 27.31 | 9.11 | 4,410,194 | 323.98M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.203/shufflenetv2b_w3d2-0911-f2106fee.pth.log)) |
| ShuffleNetV2b x2.0 | 25.58 | 8.34 | 7,611,290 | 603.37M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.242/shufflenetv2b_w2-0834-cb36b92c.pth.log)) |
| 108-MENet-8x1 (g=3) | 43.94 | 20.76 | 654,516 | 42.68M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.89/menet108_8x1_g3-2076-6acc82e4.pth.log)) |
| 128-MENet-8x1 (g=4) | 42.43 | 19.59 | 750,796 | 45.98M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.103/menet128_8x1_g4-1959-48fa80fc.pth.log)) |
| 160-MENet-8x1 (g=8) | 43.84 | 20.84 | 850,120 | 45.63M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.154/menet160_8x1_g8-2084-0f4fce43.pth.log)) |
| 228-MENet-12x1 (g=3) | 34.11 | 13.16 | 1,806,568 | 152.93M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.131/menet228_12x1_g3-1316-5b670c42.pth.log)) |
| 256-MENet-12x1 (g=4) | 32.65 | 12.52 | 1,888,240 | 150.65M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.152/menet256_12x1_g4-1252-14c6c86d.pth.log)) |
| 348-MENet-12x1 (g=3) | 28.24 | 9.58 | 3,368,128 | 312.00M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.173/menet348_12x1_g3-0958-ad50f635.pth.log)) |
| 352-MENet-12x1 (g=8) | 31.56 | 12.00 | 2,272,872 | 157.35M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.198/menet352_12x1_g8-1200-4ee200c5.pth.log)) |
| 456-MENet-24x1 (g=3) | 25.32 | 7.99 | 5,304,784 | 567.90M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.237/menet456_24x1_g3-0799-826c0022.pth.log)) |
| MobileNet x0.25 | 46.26 | 22.49 | 470,072 | 44.09M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.62/mobilenet_wd4-2249-1ad5e8fe.pth.log)) |
| MobileNet x0.5 | 34.15 | 13.55 | 1,331,592 | 155.42M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.156/mobilenet_wd2-1355-41a21242.pth.log)) |
| MobileNet x0.75 | 30.14 | 10.76 | 2,585,560 | 333.99M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.130/mobilenet_w3d4-1076-d801bcae.pth.log)) |
| MobileNet x1.0 | 26.61 | 8.95 | 4,231,976 | 579.80M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.155/mobilenet_w1-0895-7e1d739f.pth.log)) |
| FD-MobileNet x0.25 | 55.86 | 30.98 | 383,160 | 12.95M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.177/fdmobilenet_wd4-3098-2b22b709.pth.log)) |
| FD-MobileNet x0.5 | 43.13 | 20.15 | 993,928 | 41.84M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.83/fdmobilenet_wd2-2015-414dbeed.pth.log)) |
| FD-MobileNet x0.75 | 38.42 | 16.41 | 1,833,304 | 86.68M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.159/fdmobilenet_w3d4-1641-5561d58a.pth.log)) |
| FD-MobileNet x1.0 | 34.23 | 13.38 | 2,901,288 | 147.46M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.162/fdmobilenet_w1-1338-9d026c04.pth.log)) |
| MobileNetV2 x0.25 | 48.34 | 24.51 | 1,516,392 | 34.24M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.137/mobilenetv2_wd4-2451-05e1e3a2.pth.log)) |
| MobileNetV2 x0.5 | 35.98 | 14.93 | 1,964,736 | 100.13M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.170/mobilenetv2_wd2-1493-b82d79f6.pth.log)) |
| MobileNetV2 x0.75 | 30.17 | 10.82 | 2,627,592 | 198.50M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.230/mobilenetv2_w3d4-1082-8656de5a.pth.log)) |
| MobileNetV2 x1.0 | 26.97 | 8.87 | 3,504,960 | 329.36M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.213/mobilenetv2_w1-0887-13a021bc.pth.log)) |
| IGCV3 x0.25 | 53.70 | 28.71 | 1,534,020 | 41.29M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.142/igcv3_wd4-2871-c9f28301.pth.log)) |
| IGCV3 x0.5 | 39.75 | 17.32 | 1,985,528 | 111.12M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.132/igcv3_wd2-1732-8c504f44.pth.log)) |
| IGCV3 x0.75 | 31.05 | 11.40 | 2,638,084 | 210.95M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.207/igcv3_w3d4-1140-63f43cf8.pth.log)) |
| IGCV3 x1.0 | 27.91 | 9.20 | 3,491,688 | 340.79M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.243/igcv3_w1-0920-12385791.pth.log)) |
| MnasNet | 31.58 | 11.74 | 4,308,816 | 317.67M | From [zeusees/Mnasnet...Model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.117/mnasnet-1174-e8ec017c.pth.log)) |
| DARTS | 26.70 | 8.74 | 4,718,752 | 539.86M | From [quark0/darts] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.118/darts-0874-74f0c7b6.pth.log)) |
| Xception | 20.97 | 5.49 | 22,855,952 | 8,403.63M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.115/xception-0549-e4f0232c.pth.log)) |
| InceptionV3 | 21.12 | 5.65 | 23,834,568 | 5,743.06M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.92/inceptionv3-0565-cf406180.pth.log)) |
| InceptionV4 | 20.64 | 5.29 | 42,679,816 | 12,304.93M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.105/inceptionv4-0529-5cb7b4e4.pth.log)) |
| InceptionResNetV2 | 19.93 | 4.90 | 55,843,464 | 13,188.64M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.107/inceptionresnetv2-0490-1d1b4d18.pth.log)) |
| PolyNet | 19.10 | 4.52 | 95,366,600 | 34,821.34M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.96/polynet-0452-6a1b295d.pth.log)) |
| NASNet-A 4@1056 | 25.68 | 8.16 | 5,289,978 | 584.90M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.97/nasnet_4a1056-0816-d21bbaf5.pth.log)) |
| NASNet-A 6@4032 | 18.14 | 4.21 | 88,753,150 | 23,976.44M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.101/nasnet_6a4032-0421-f354d28f.pth.log)) |
| PNASNet-5-Large | 17.88 | 4.28 | 86,057,668 | 25,140.77M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.114/pnasnet5large-0428-65de46eb.pth.log)) |

### CIFAR-10

| Model | Error, % | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | --- |
| NIN | 7.43 | 966,986 | 222.97M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.175/nin_cifar10-0743-795b0824.pth.log)) |
| ResNet-20 | 5.97 | 272,474 | 41.29M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet20_cifar10-0597-9b0024ac.pth.log)) |
| ResNet-56 | 4.52 | 855,770 | 127.06M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet56_cifar10-0452-628c42a2.pth.log)) |
| ResNet-110 | 3.69 | 1,730,714 | 255.70M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet110_cifar10-0369-4d6ca1fc.pth.log)) |
| ResNet-164(BN) | 3.68 | 1,704,154 | 255.31M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.179/resnet164bn_cifar10-0368-74ae9f4b.pth.log)) |
| ResNet-1001 | 3.28 | 10,328,602 | 1,536.40M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.201/resnet1001_cifar10-0328-77a179e2.pth.log)) |
| ResNet-1202 | 3.53 | 19,424,026 | 2,857.17M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.214/resnet1202_cifar10-0353-1d5a2129.pth.log)) |
| PreResNet-20 | 6.51 | 272,282 | 41.27M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet20_cifar10-0651-76cec68d.pth.log)) |
| PreResNet-56 | 4.49 | 855,578 | 127.03M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet56_cifar10-0449-e9124fcf.pth.log)) |
| PreResNet-110 | 3.86 | 1,730,522 | 255.68M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet110_cifar10-0386-cc08946a.pth.log)) |
| PreResNet-164(BN) | 3.64 | 1,703,258 | 255.08M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.196/preresnet164bn_cifar10-0364-429012d4.pth.log)) |
| PreResNet-1001 | 2.65 | 10,327,706 | 1,536.18M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.209/preresnet1001_cifar10-0265-9fedfe5f.pth.log)) |
| PreResNet-1202 | 3.39 | 19,423,834 | 2,857.14M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.246/preresnet1202_cifar10-0339-6fc686b0.pth.log)) |
| ResNeXt-29 (32x4d) | 3.15 | 4,775,754 | 780.55M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.169/resnext29_32x4d_cifar10-0315-30413525.pth.log)) |
| ResNeXt-29 (16x64d) | 2.41 | 68,155,210 | 10,709.34M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.176/resnext29_16x64d_cifar10-0241-4133d3d0.pth.log)) |
| PyramidNet-110 (a=48) | 3.72 | 1,772,706 | 408.37M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.184/pyramidnet110_a48_cifar10-0372-eb185645.pth.log)) |
| PyramidNet-110 (a=84) | 2.98 | 3,904,446 | 778.15M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.185/pyramidnet110_a84_cifar10-0298-7b835a3c.pth.log)) |
| PyramidNet-110 (a=270) | 2.51 | 28,485,477 | 4,730.60M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.194/pyramidnet110_a270_cifar10-0251-31bdd9d5.pth.log)) |
| DenseNet-40 (k=12) | 5.61 | 599,050 | 210.80M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.193/densenet40_k12_cifar10-0561-8b8e8194.pth.log)) |
| DenseNet-BC-40 (k=12) | 6.43 | 176,122 | 74.89M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.231/densenet40_k12_bc_cifar10-0643-6dc86a2e.pth.log)) |
| DenseNet-BC-40 (k=24) | 4.52 | 690,346 | 293.09M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.220/densenet40_k24_bc_cifar10-0452-669c5255.pth.log)) |
| DenseNet-BC-40 (k=36) | 4.04 | 1,542,682 | 654.60M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.224/densenet40_k36_bc_cifar10-0404-b1a4cc7e.pth.log)) |
| DenseNet-100 (k=12) | 3.66 | 4,068,490 | 1,353.55M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.205/densenet100_k12_cifar10-0366-26089c6e.pth.log)) |
| DenseNet-BC-100 (k=12) | 4.16 | 769,162 | 298.45M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.189/densenet100_k12_bc_cifar10-0416-b9232829.pth.log)) |
| X-DenseNet-BC-40-2 (k=24) | 5.31 | 690,346 | 293.09M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.226/xdensenet40_2_k24_bc_cifar10-0531-b91a9dc3.pth.log)) |
| X-DenseNet-BC-40-2 (k=36) | 4.37 | 1,542,682 | 654.60M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.233/xdensenet40_2_k36_bc_cifar10-0437-ed264a20.pth.log)) |
| WRN-16-10 | 2.93 | 17,116,634 | 2,414.04M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn16_10_cifar10-0293-ce810d8a.pth.log)) |
| WRN-28-10 | 2.39 | 36,479,194 | 5,246.98M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn28_10_cifar10-0239-fe97dcd6.pth.log)) |
| WRN-40-8 | 2.37 | 35,748,314 | 5,176.90M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn40_8_cifar10-0237-8dc84ec7.pth.log)) |
| RoR-3-56 | 5.43 | 762,746 | 113.43M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.228/ror3_56_cifar10-0543-44f0f47d.pth.log)) |
| RoR-3-110 | 4.35 | 1,637,690 | 242.07M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.235/ror3_110_cifar10-0435-fb2a2b04.pth.log)) |
| Shake-Shake-ResNet-20-2x16d | 5.15 | 541,082 | 81.78M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.215/shakeshakeresnet20_2x16d_cifar10-0515-ef71ec0d.pth.log)) |
| Shake-Shake-ResNet-26-2x32d | 3.17 | 2,923,162 | 428.89M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.217/shakeshakeresnet26_2x32d_cifar10-0317-ecd1f833.pth.log)) |

### CIFAR-100

| Model | Error, % | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | --- |
| NIN | 28.39 | 984,356 | 224.08M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.183/nin_cifar100-2839-627a11c0.pth.log)) |
| ResNet-20 | 29.64 | 278,324 | 41.30M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.180/resnet20_cifar100-2964-a5322afe.pth.log)) |
| ResNet-56 | 24.88 | 861,620 | 127.06M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.181/resnet56_cifar100-2488-d65f53b1.pth.log)) |
| ResNet-110 | 22.80 | 1,736,564 | 255.71M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.190/resnet110_cifar100-2280-d8d397a7.pth.log)) |
| ResNet-164(BN) | 20.44 | 1,727,284 | 255.33M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.182/resnet164bn_cifar100-2044-8fa07b72.pth.log)) |
| PreResNet-20 | 30.22 | 278,132 | 41.28M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.187/preresnet20_cifar100-3022-3dbfa6a2.pth.log)) |
| PreResNet-56 | 25.05 | 861,428 | 127.04M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.188/preresnet56_cifar100-2505-ca90a2be.pth.log)) |
| PreResNet-110 | 22.67 | 1,736,372 | 255.68M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.191/preresnet110_cifar100-2267-3954e915.pth.log)) |
| PreResNet-164(BN) | 20.18 | 1,726,388 | 255.10M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.192/preresnet164bn_cifar100-2018-a8e67ca6.pth.log)) |
| ResNeXt-29 (32x4d) | 19.50 | 4,868,004 | 780.64M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.200/resnext29_32x4d_cifar100-1950-13ba13d9.pth.log)) |
| PyramidNet-110 (a=48) | 20.95 | 1,778,556 | 408.38M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.186/pyramidnet110_a48_cifar100-2095-95da1a20.pth.log)) |
| PyramidNet-110 (a=84) | 18.87 | 3,913,536 | 778.16M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.199/pyramidnet110_a84_cifar100-1887-ff711084.pth.log)) |
| DenseNet-40 (k=12) | 24.90 | 622,360 | 210.82M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.195/densenet40_k12_cifar100-2490-d182c224.pth.log)) |
| DenseNet-BC-40 (k=12) | 28.41 | 188,092 | 74.90M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.232/densenet40_k12_bc_cifar100-2841-1e9db765.pth.log)) |
| DenseNet-BC-40 (k=24) | 22.67 | 714,196 | 293.11M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.221/densenet40_k24_bc_cifar100-2267-411719c0.pth.log)) |
| DenseNet-BC-40 (k=36) | 20.50 | 1,578,412 | 654.64M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.225/densenet40_k36_bc_cifar100-2050-cde836fa.pth.log)) |
| DenseNet-100 (k=12) | 19.64 | 4,129,600 | 1,353.62M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.206/densenet100_k12_cifar100-1964-5e10cd83.pth.log)) |
| DenseNet-BC-100 (k=12) | 21.19 | 800,032 | 298.48M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.208/densenet100_k12_bc_cifar100-2119-05a6f027.pth.log)) |
| X-DenseNet-BC-40-2 (k=24) | 23.96 | 714,196 | 293.11M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.227/xdensenet40_2_k24_bc_cifar100-2396-0ce8f78a.pth.log)) |
| X-DenseNet-BC-40-2 (k=36) | 21.65 | 1,578,412 | 654.64M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.234/xdensenet40_2_k36_bc_cifar100-2165-6f68f83d.pth.log)) |
| WRN-16-10 | 18.95 | 17,174,324 | 2,414.09M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.204/wrn16_10_cifar100-1895-bef9809c.pth.log)) |
| RoR-3-56 | 25.49 | 768,596 | 113.43M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.229/ror3_56_cifar100-2549-34be6719.pth.log)) |
| RoR-3-110 | 23.64 | 1,643,540 | 242.08M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.236/ror3_110_cifar100-2364-d599e3a9.pth.log)) |
| Shake-Shake-ResNet-20-2x16d | 29.22 | 546,932 | 81.79M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.247/shakeshakeresnet20_2x16d_cifar100-2922-4d07f142.pth.log)) |
| Shake-Shake-ResNet-26-2x32d | 18.80 | 2,934,772 | 428.90M | Converted from GL model ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.222/shakeshakeresnet26_2x32d_cifar100-1880-b47e371f.pth.log)) |

[dmlc/gluon-cv]: https://github.com/dmlc/gluon-cv
[tornadomeet/ResNet]: https://github.com/tornadomeet/ResNet
[Cadene/pretrained...pytorch]: https://github.com/Cadene/pretrained-models.pytorch
[ShichenLiu/CondenseNet]: https://github.com/ShichenLiu/CondenseNet
[clavichord93/MENet]: https://github.com/clavichord93/MENet
[clavichord93/FD-MobileNet]: https://github.com/clavichord93/FD-MobileNet
[tensorpack/tensorpack]: https://github.com/tensorpack/tensorpack
[dyhan0920/Pyramid...PyTorch]: https://github.com/dyhan0920/PyramidNet-PyTorch
[zeusees/Mnasnet...Model]: https://github.com/zeusees/Mnasnet-Pretrained-Model
[szagoruyko/diracnets]: https://github.com/szagoruyko/diracnets
[szagoruyko/functional-zoo]: https://github.com/szagoruyko/functional-zoo
[fyu/drn]: https://github.com/fyu/drn
[quark0/darts]: https://github.com/quark0/darts
[soeaver/AirNet-PyTorch]: https://github.com/soeaver/AirNet-PyTorch
[soeaver/mxnet-model]: https://github.com/soeaver/mxnet-model
[Jongchan/attention-module]: https://github.com/Jongchan/attention-module
[XingangPan/IBN-Net]: https://github.com/XingangPan/IBN-Net
[cypw/CRU-Net]: https://github.com/cypw/CRU-Net
[kevin-ssy/FishNet]: https://github.com/kevin-ssy/FishNet
[ucbdrive/dla]: https://github.com/ucbdrive/dla
[sacmehta/ESPNetv2]: https://github.com/sacmehta/ESPNetv2
[jhjacobsen/pytorch-i-revnet]: https://github.com/jhjacobsen/pytorch-i-revnet