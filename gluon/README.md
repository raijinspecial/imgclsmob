# Image classification models on MXNet/Gluon

[![PyPI](https://img.shields.io/pypi/v/gluoncv2.svg)](https://pypi.python.org/pypi/gluoncv2)
[![Downloads](https://pepy.tech/badge/gluoncv2)](https://pepy.tech/project/gluoncv2)

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
- CRU-Net (['Sharing Residual Units Through Collective Tensor Factorization To Improve Deep Neural Networks'](https://www.ijcai.org/proceedings/2018/88))
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

To use the models in your project, simply install the `gluoncv2` package with `mxnet`:
```
pip install gluoncv2 mxnet>=1.2.1
```
To enable different hardware supports such as GPUs, check out [MXNet variants](https://pypi.org/project/mxnet).
For example, you can install with CUDA-9.2 supported MXNet:
```
pip install gluoncv2 mxnet-cu92>=1.2.1
```

## Usage

Example of using a pretrained ResNet-18 model:
```
from gluoncv2.model_provider import get_model as glcv2_get_model
import mxnet as mx

net = glcv2_get_model("resnet18", pretrained=True)
x = mx.nd.zeros((1, 3, 224, 224), ctx=mx.cpu())
y = net(x)
```

## Pretrained models

### Imagenet-1K

Some remarks:
- Top1/Top5 are the standard 1-crop Top-1/Top-5 errors (in percents) on the validation subset of the ImageNet-1K dataset.
- FLOPs/2 is the number of FLOPs divided by two to be similar to the number of MACs.
- ResNet/PreResNet with b-suffix is a version of the networks with the stride in the second convolution of the
bottleneck block. Respectively a network without b-suffix has the stride in the first convolution.
- ResNet/PreResNet models do not use biases in convolutions at all.
- CondenseNet models are only so-called converted versions.
- ShuffleNetV2 and ShuffleNetV2b are different implementations of the same architecture.

| Model | Top1 | Top5 | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | ---: | --- |
| AlexNet | 44.12 | 21.26 | 61,100,840 | 714.83M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.108/alexnet-2126-9cb87ebd.params.log)) |
| VGG-11 | 31.91 | 11.76 | 132,863,336 | 7,615.87M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg11-1176-95dd287d.params.log)) |
| VGG-13 | 31.06 | 11.12 | 133,047,848 | 11,317.65M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg13-1112-a0db3c6c.params.log)) |
| VGG-16 | 26.78 | 8.69 | 138,357,544 | 15,480.10M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg16-0869-57a2556f.params.log)) |
| VGG-19 | 25.88 | 8.23 | 143,667,240 | 19,642.55M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg19-0823-0e2a1e0a.params.log)) |
| BN-VGG-11b | 30.34 | 10.57 | 132,868,840 | 7,630.72M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg11b-1057-b2d8f382.params.log)) |
| BN-VGG-13b | 29.48 | 10.16 | 133,053,736 | 11,342.14M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg13b-1016-f384ff52.params.log)) |
| BN-VGG-16b | 26.89 | 8.65 | 138,365,992 | 15,507.20M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg16b-0865-b5e33db8.params.log)) |
| BN-VGG-19b | 25.66 | 8.15 | 143,678,248 | 19,672.26M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg19b-0815-3a0e43e6.params.log)) |
| BN-Inception | 25.09 | 7.76 | 11,295,240 | 2,048.06M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.139/bninception-0776-8314001b.params.log)) |
| ResNet-10 | 34.61 | 13.85 | 5,418,792 | 894.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.248/resnet10-1385-a9964274.params.log)) |
| ResNet-12 | 35.86 | 14.46 | 5,492,776 | 1,126.25M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.30/resnet12-1446-9ce715b0.params.log)) |
| ResNet-14 | 32.85 | 12.41 | 5,788,200 | 1,357.94M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.40/resnet14-1241-a8955ff3.params.log)) |
| ResNet-16 | 30.68 | 11.10 | 6,968,872 | 1,589.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.41/resnet16-1110-1be996d1.params.log)) |
| ResNet-18 x0.25 | 49.16 | 24.45 | 831,096 | 137.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.47/resnet18_wd4-2445-28d15cf4.params.log)) |
| ResNet-18 x0.5 | 36.54 | 14.96 | 3,055,880 | 486.49M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.46/resnet18_wd2-1496-d839c509.params.log)) |
| ResNet-18 x0.75 | 33.25 | 12.54 | 6,675,352 | 1,047.53M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.18/resnet18_w3d4-1254-d6548612.params.log)) |
| ResNet-18 | 28.09 | 9.51 | 11,689,512 | 1,820.41M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.153/resnet18-0951-98a2545b.params.log)) |
| ResNet-34 | 25.34 | 7.92 | 21,797,672 | 3,672.68M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.1/resnet34-0792-5b875f49.params.log)) |
| ResNet-50 | 22.65 | 6.41 | 25,557,032 | 3,877.95M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.147/resnet50-0641-1eaa883b.params.log)) |
| ResNet-50b | 22.32 | 6.18 | 25,557,032 | 4,110.48M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.146/resnet50b-0618-8e2541fb.params.log)) |
| ResNet-101 | 21.66 | 5.99 | 44,549,160 | 7,597.95M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.1/resnet101-0599-a6d3a5f4.params.log)) |
| ResNet-101b | 20.79 | 5.39 | 44,549,160 | 7,830.48M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.145/resnet101b-0539-7406d858.params.log)) |
| ResNet-152 | 20.76 | 5.35 | 60,192,808 | 11,321.85M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.144/resnet152-0535-bbdd7ed1.params.log)) |
| ResNet-152b | 20.31 | 5.25 | 60,192,808 | 11,554.38M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.143/resnet152b-0525-6f30d0d9.params.log)) |
| PreResNet-10 | 34.65 | 14.01 | 5,417,128 | 894.19M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.249/preresnet10-1401-2b96c081.params.log)) |
| PreResNet-18 | 28.16 | 9.51 | 11,687,848 | 1,820.56M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.140/preresnet18-0951-71279a0b.params.log)) |
| PreResNet-34 | 25.88 | 8.11 | 21,796,008 | 3,672.83M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet34-0811-f8fe98a2.params.log)) |
| PreResNet-50 | 23.39 | 6.68 | 25,549,480 | 3,875.44M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet50-0668-4940c94b.params.log)) |
| PreResNet-50b | 23.16 | 6.64 | 25,549,480 | 4,107.97M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet50b-0664-2fcfddb1.params.log)) |
| PreResNet-101 | 21.45 | 5.75 | 44,541,608 | 7,595.44M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet101-0575-e2887e53.params.log)) |
| PreResNet-101b | 21.73 | 5.88 | 44,541,608 | 7,827.97M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet101b-0588-1015145a.params.log)) |
| PreResNet-152 | 20.70 | 5.32 | 60,185,256 | 11,319.34M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.14/preresnet152-0532-31505f71.params.log)) |
| PreResNet-152b | 21.00 | 5.75 | 60,185,256 | 11,551.87M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet152b-0575-dc303191.params.log)) |
| PreResNet-200b | 21.10 | 5.64 | 64,666,280 | 15,068.63M | From [tornadomeet/ResNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.45/preresnet200b-0564-38f849a6.params.log)) |
| PreResNet-269b | 20.71 | 5.56 | 102,065,832 | 20,101.11M | From [soeaver/mxnet-model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.239/preresnet269b-0556-f386e3e7.params.log)) |
| ResNeXt-101 (32x4d) | 21.32 | 5.79 | 44,177,704 | 8,003.45M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.10/resnext101_32x4d-0579-9afbfdbc.params.log)) |
| ResNeXt-101 (64x4d) | 20.60 | 5.41 | 83,455,272 | 15,500.27M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.10/resnext101_64x4d-0541-0d4fd87b.params.log)) |
| SE-ResNet-50 | 22.51 | 6.44 | 28,088,024 | 3,880.49M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet50-0644-10954a84.params.log)) |
| SE-ResNet-101 | 21.92 | 5.89 | 49,326,872 | 7,602.76M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet101-0589-4c10238d.params.log)) |
| SE-ResNet-152 | 21.48 | 5.77 | 66,821,848 | 11,328.52M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet152-0577-de6f099d.params.log)) |
| SE-ResNeXt-50 (32x4d) | 21.06 | 5.58 | 27,559,896 | 4,258.40M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.12/seresnext50_32x4d-0558-a49f8fb0.params.log)) |
| SE-ResNeXt-101 (32x4d) | 19.99 | 5.00 | 48,955,416 | 8,008.26M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.12/seresnext101_32x4d-0500-cf161260.params.log)) |
| SENet-154 | 18.84 | 4.65 | 115,088,984 | 20,745.78M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.13/senet154-0465-dd244507.params.log)) |
| IBN-ResNet-50 | 23.56 | 6.68 | 25,557,032 | 4,110.48M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnet50-0668-db527596.params.log)) |
| IBN-ResNet-101 | 21.89 | 5.87 | 44,549,160 | 7,830.48M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnet101-0587-946e7f10.params.log)) |
| IBN(b)-ResNet-50 | 23.91 | 6.97 | 25,558,568 | 4,112.89M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibnb_resnet50-0697-0aea51d2.params.log)) |
| IBN-ResNeXt-101 (32x4d) | 21.43 | 5.62 | 44,177,704 | 8,003.45M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnext101_32x4d-0562-05ddba79.params.log)) |
| IBN-DenseNet-121 | 24.98 | 7.47 | 7,978,856 | 2,872.13M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_densenet121-0747-1434d379.params.log)) |
| IBN-DenseNet-169 | 23.78 | 6.82 | 14,149,480 | 3,403.89M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_densenet169-0682-6d7c48c5.params.log)) |
| AirNet50-1x64d (r=2) | 22.48 | 6.21 | 27,425,864 | 4,772.11M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnet50_1x64d_r2-0621-347358cc.params.log)) |
| AirNet50-1x64d (r=16) | 22.91 | 6.46 | 25,714,952 | 4,399.97M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnet50_1x64d_r16-0646-0b847b99.params.log)) |
| AirNeXt50-32x4d (r=2) | 21.51 | 5.75 | 27,604,296 | 5,339.58M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnext50_32x4d_r2-0575-ab104fb5.params.log)) |
| BAM-ResNet-50 | 23.68 | 6.96 | 25,915,099 | 4,196.09M | From [Jongchan/attention-module] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.124/bam_resnet50-0696-7e573b61.params.log)) |
| CBAM-ResNet-50 | 23.02 | 6.38 | 28,089,624 | 4,116.97M | From [Jongchan/attention-module] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.125/cbam_resnet50-0638-78be5665.params.log)) |
| PyramidNet-101 (a=360) | 22.72 | 6.52 | 42,455,070 | 8,743.54M | From [dyhan0920/Pyramid...PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.104/pyramidnet101_a360-0652-08d5a5d1.params.log)) |
| DiracNetV2-18 | 30.61 | 11.17 | 11,511,784 | 1,796.62M | From [szagoruyko/diracnets] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.111/diracnet18v2-1117-27601f6f.params.log)) |
| DiracNetV2-34 | 27.93 | 9.46 | 21,616,232 | 3,646.93M | From [szagoruyko/diracnets] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.111/diracnet34v2-0946-1faa6f12.params.log)) |
| CRU-Net-56 | 25.72 | 8.25 | 25,609,384 | 5,660.66M | From [cypw/CRU-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.197/crunet56-0825-ad16523b.params.log)) |
| DenseNet-121 | 25.11 | 7.80 | 7,978,856 | 2,872.13M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet121-0780-49b72d04.params.log)) |
| DenseNet-161 | 22.40 | 6.18 | 28,681,000 | 7,793.16M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet161-0618-52e30516.params.log)) |
| DenseNet-169 | 23.89 | 6.89 | 14,149,480 | 3,403.89M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet169-0689-281ec06b.params.log)) |
| DenseNet-201 | 22.71 | 6.36 | 20,013,928 | 4,347.15M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet201-0636-65b5d389.params.log)) |
| CondenseNet-74 (C=G=4) | 26.82 | 8.64 | 4,773,944 | 546.06M | From [ShichenLiu/CondenseNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.4/condensenet74_c4_g4-0864-cde68fa2.params.log)) |
| CondenseNet-74 (C=G=8) | 29.76 | 10.49 | 2,935,416 | 291.52M | From [ShichenLiu/CondenseNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.4/condensenet74_c8_g8-1049-4cf4a08e.params.log)) |
| PeleeNet | 31.71 | 11.25 | 2,802,248 | 514.87M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.141/peleenet-1125-38d4fb24.params.log)) |
| WRN-50-2 | 22.15 | 6.12 | 68,849,128 | 11,405.42M | From [szagoruyko/functional-zoo] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.113/wrn50_2-0612-f8013e68.params.log)) |
| DRN-C-26 | 25.68 | 7.89 | 21,126,584 | 16,993.90M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc26-0789-ee56ffab.params.log)) |
| DRN-C-42 | 23.80 | 6.92 | 31,234,744 | 25,093.75M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc42-0692-f89c26d6.params.log)) |
| DRN-C-58 | 22.35 | 6.27 | 40,542,008 | 32,489.94M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc58-0627-44cbf15c.params.log)) |
| DRN-D-22 | 26.67 | 8.52 | 16,393,752 | 13,051.33M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd22-0852-08574752.params.log)) |
| DRN-D-38 | 24.51 | 7.36 | 26,501,912 | 21,151.19M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd38-0736-c7d53bc0.params.log)) |
| DRN-D-54 | 22.05 | 6.27 | 35,809,176 | 28,547.38M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd54-0627-87d44c87.params.log)) |
| DRN-D-105 | 21.31 | 5.81 | 54,801,304 | 43,442.43M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd105-0581-ab12d662.params.log)) |
| DPN-68 | 23.57 | 7.00 | 12,611,602 | 2,351.84M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn68-0700-3114719d.params.log)) |
| DPN-98 | 20.23 | 5.28 | 61,570,728 | 11,716.51M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn98-0528-fa5d6fca.params.log)) |
| DPN-131 | 20.03 | 5.22 | 79,254,504 | 16,076.15M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn131-0522-35ac2f82.params.log)) |
| DarkNet Tiny | 40.31 | 17.46 | 1,042,104 | 500.85M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.69/darknet_tiny-1746-16501793.params.log)) |
| DarkNet Ref | 38.00 | 16.68 | 7,319,416 | 367.59M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.64/darknet_ref-1668-3011b4e1.params.log)) |
| DarkNet-53 | 21.44 | 5.56 | 41,609,928 | 7,133.86M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.150/darknet53-0556-e9486353.params.log)) |
| i-RevNet-301 | 26.97 | 8.97 | 125,120,356 | 14,453.87M | From [jhjacobsen/pytorch-i-revnet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.251/irevnet301-0897-cef9b5bf.params.log)) |
| DLA-34 | 26.14 | 8.21 | 15,742,104 | 3,071.37M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla34-0821-1127fa0a.params.log)) |
| DLA-46-C | 36.79 | 14.70 | 1,301,400 | 585.45M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla46c-1470-bae8b513.params.log)) |
| DLA-X-46-C | 35.58 | 13.98 | 1,068,440 | 546.72M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla46xc-1398-28deb1fc.params.log)) |
| DLA-60 | 23.84 | 7.08 | 22,036,632 | 4,255.49M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60-0708-954571d6.params.log)) |
| DLA-X-60 | 22.48 | 6.21 | 17,352,344 | 3,543.68M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60x-0621-35774214.params.log)) |
| DLA-X-60-C | 33.52 | 12.41 | 1,319,832 | 596.06M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60xc-1241-338c6241.params.log)) |
| DLA-102 | 22.87 | 6.44 | 33,268,888 | 7,190.95M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102-0644-cadbb1cc.params.log)) |
| DLA-X-102 | 21.97 | 6.02 | 26,309,272 | 5,884.94M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102x-0602-193568a7.params.log)) |
| DLA-X2-102 | 21.12 | 5.53 | 41,282,200 | 9,340.61M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102x2-0553-30c8f409.params.log)) |
| DLA-169 | 21.95 | 5.87 | 53,389,720 | 11,593.20M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla169-0587-4f3e6a6e.params.log)) |
| FishNet-150 | 22.85 | 6.38 | 24,959,400 | 6,435.02M | From [kevin-ssy/FishNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.168/fishnet150-0638-5cbd08ec.params.log)) |
| ESPNetv2 x0.5 | 43.61 | 21.07 | 1,241,332 | 35.36M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_wd2-2107-f2e17f0a.params.log)) |
| ESPNetv2 x1.0 | 35.33 | 14.27 | 1,670,072 | 98.09M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w1-1427-538f31fb.params.log)) |
| ESPNetv2 x1.25 | 33.14 | 12.73 | 1,965,440 | 138.18M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w5d4-1273-b119ad9e.params.log)) |
| ESPNetv2 x1.5 | 32.04 | 11.94 | 2,314,856 | 185.77M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w3d2-1194-3804a850.params.log)) |
| ESPNetv2 x2.0 | 28.91 | 9.94 | 3,498,136 | 306.93M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w2-0994-c212d81a.params.log)) |
| SqueezeNet v1.0 | 38.73 | 17.34 | 1,248,424 | 823.67M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.128/squeezenet_v1_0-1734-e6f8b0e8.params.log)) |
| SqueezeNet v1.1 | 39.09 | 17.39 | 1,235,496 | 352.02M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.88/squeezenet_v1_1-1739-d7a1483a.params.log)) |
| SqueezeResNet v1.0 | 39.32 | 17.67 | 1,248,424 | 823.67M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.178/squeezeresnet_v1_0-1767-66474b9b.params.log)) |
| SqueezeResNet v1.1 | 39.83 | 17.84 | 1,235,496 | 352.02M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.70/squeezeresnet_v1_1-1784-26064b82.params.log)) |
| 1.0-SqNxt-23 | 42.25 | 18.66 | 724,056 | 287.28M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.171/sqnxt23_w1-1866-73b700c4.params.log)) |
| 1.0-SqNxt-23v5 | 40.43 | 17.43 | 921,816 | 285.82M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.172/sqnxt23v5_w1-1743-7a83722e.params.log)) |
| 1.5-SqNxt-23 | 34.46 | 13.21 | 1,511,824 | 552.39M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.210/sqnxt23_w3d2-1321-4d733bcd.params.log)) |
| 1.5-SqNxt-23v5 | 33.48 | 12.68 | 1,953,616 | 550.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.212/sqnxt23v5_w3d2-1268-4f98bbd3.params.log)) |
| 2.0-SqNxt-23 | 30.24 | 10.63 | 2,583,752 | 898.48M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.240/sqnxt23_w2-1063-95d9b55a.params.log)) |
| 2.0-SqNxt-23v5 | 29.27 | 10.24 | 3,366,344 | 897.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.216/sqnxt23v5_w2-1024-707246f3.params.log)) |
| ShuffleNet x0.25 (g=1) | 62.00 | 36.77 | 209,746 | 12.35M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.134/shufflenet_g1_wd4-3677-ee58f368.params.log)) |
| ShuffleNet x0.25 (g=3) | 61.34 | 36.17 | 305,902 | 13.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.135/shufflenet_g3_wd4-3617-bd08e3ed.params.log)) |
| ShuffleNet x0.5 (g=1) | 46.22 | 22.38 | 534,484 | 41.16M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.174/shufflenet_g1_wd2-2238-f77dcd18.params.log)) |
| ShuffleNet x0.5 (g=3) | 43.83 | 20.60 | 718,324 | 41.70M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.167/shufflenet_g3_wd2-2060-ea6737a5.params.log)) |
| ShuffleNet x0.75 (g=1) | 39.25 | 16.75 | 975,214 | 86.42M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.218/shufflenet_g1_w3d4-1675-2f1530aa.params.log)) |
| ShuffleNet x0.75 (g=3) | 37.81 | 16.09 | 1,238,266 | 85.82M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.219/shufflenet_g3_w3d4-1609-e008e926.params.log)) |
| ShuffleNet x1.0 (g=1) | 34.41 | 13.50 | 1,531,936 | 148.13M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.223/shufflenet_g1_w1-1350-01934ee8.params.log)) |
| ShuffleNet x1.0 (g=2) | 33.98 | 13.32 | 1,733,848 | 147.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.241/shufflenet_g2_w1-1332-f5a1479f.params.log)) |
| ShuffleNet x1.0 (g=3) | 33.96 | 13.29 | 1,865,728 | 145.46M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.244/shufflenet_g3_w1-1329-ac58d62c.params.log)) |
| ShuffleNet x1.0 (g=4) | 33.84 | 13.10 | 1,968,344 | 143.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.245/shufflenet_g4_w1-1310-73c039eb.params.log)) |
| ShuffleNet x1.0 (g=8) | 33.65 | 13.19 | 2,434,768 | 150.76M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.250/shufflenet_g8_w1-1319-9a50ddd9.params.log)) |
| ShuffleNetV2 x0.5 | 40.61 | 18.30 | 1,366,792 | 43.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.90/shufflenetv2_wd2-1830-156953de.params.log)) |
| ShuffleNetV2 x1.0 | 30.94 | 11.23 | 2,278,604 | 149.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.133/shufflenetv2_w1-1123-27435039.params.log)) |
| ShuffleNetV2 x1.5 | 32.38 | 12.37 | 4,406,098 | 320.77M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.65/shufflenetv2_w3d2-1237-08c01388.params.log)) |
| ShuffleNetV2 x2.0 | 32.04 | 12.10 | 7,601,686 | 595.84M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.84/shufflenetv2_w2-1210-544b55d9.params.log)) |
| ShuffleNetV2b x0.5 | 39.81 | 17.82 | 1,366,792 | 43.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.157/shufflenetv2b_wd2-1782-845a9c43.params.log)) |
| ShuffleNetV2b x1.0 | 30.39 | 11.01 | 2,279,760 | 150.62M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.161/shufflenetv2b_w1-1101-f679702f.params.log)) |
| ShuffleNetV2b x1.5 | 26.90 | 8.79 | 4,410,194 | 323.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.203/shufflenetv2b_w3d2-0879-4022da3a.params.log)) |
| ShuffleNetV2b x2.0 | 25.20 | 8.10 | 7,611,290 | 603.37M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.242/shufflenetv2b_w2-0810-7429df75.params.log)) |
| 108-MENet-8x1 (g=3) | 43.62 | 20.30 | 654,516 | 42.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.89/menet108_8x1_g3-2030-aa07f925.params.log)) |
| 128-MENet-8x1 (g=4) | 42.10 | 19.13 | 750,796 | 45.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.103/menet128_8x1_g4-1913-0c890a76.params.log)) |
| 128-MENet-8x1 (g=4) | 42.10 | 19.13 | 750,796 | 45.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.103/menet128_8x1_g4-1913-0c890a76.params.log)) |
| 160-MENet-8x1 (g=8) | 43.47 | 20.28 | 850,120 | 45.63M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.154/menet160_8x1_g8-2028-4f28279a.params.log)) |
| 256-MENet-12x1 (g=4) | 32.23 | 12.16 | 1,888,240 | 150.65M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.152/menet256_12x1_g4-1216-7caf63d1.params.log)) |
| 348-MENet-12x1 (g=3) | 27.85 | 9.36 | 3,368,128 | 312.00M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.173/menet348_12x1_g3-0936-62c72b0b.params.log)) |
| 352-MENet-12x1 (g=8) | 31.30 | 11.67 | 2,272,872 | 157.35M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.198/menet352_12x1_g8-1167-5892fea4.params.log)) |
| 456-MENet-24x1 (g=3) | 25.02 | 7.80 | 5,304,784 | 567.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.237/menet456_24x1_g3-0780-7a89b32c.params.log)) |
| MobileNet x0.25 | 45.78 | 22.18 | 470,072 | 44.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.62/mobilenet_wd4-2218-3185cdd2.params.log)) |
| MobileNet x0.5 | 33.94 | 13.30 | 1,331,592 | 155.42M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.156/mobilenet_wd2-1330-94f13ae1.params.log)) |
| MobileNet x0.75 | 29.85 | 10.51 | 2,585,560 | 333.99M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.130/mobilenet_w3d4-1051-6361d4b4.params.log)) |
| MobileNet x1.0 | 26.43 | 8.65 | 4,231,976 | 579.80M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.155/mobilenet_w1-0865-eafd91e9.params.log)) |
| FD-MobileNet x0.25 | 55.44 | 30.53 | 383,160 | 12.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.177/fdmobilenet_wd4-3053-d4f18e5b.params.log)) |
| FD-MobileNet x0.5 | 42.62 | 19.69 | 993,928 | 41.84M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.83/fdmobilenet_wd2-1969-242b9fa8.params.log)) |
| FD-MobileNet x0.75 | 37.91 | 16.01 | 1,833,304 | 86.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.159/fdmobilenet_w3d4-1601-cb10c3e1.params.log)) |
| FD-MobileNet x1.0 | 33.80 | 13.12 | 2,901,288 | 147.46M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.162/fdmobilenet_w1-1312-95fa0092.params.log)) |
| MobileNetV2 x0.25 | 48.08 | 24.12 | 1,516,392 | 34.24M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.137/mobilenetv2_wd4-2412-d92b5b2d.params.log)) |
| MobileNetV2 x0.5 | 35.63 | 14.42 | 1,964,736 | 100.13M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.170/mobilenetv2_wd2-1442-d7c586c7.params.log)) |
| MobileNetV2 x0.75 | 29.78 | 10.44 | 2,627,592 | 198.50M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.230/mobilenetv2_w3d4-1044-768454f4.params.log)) |
| MobileNetV2 x1.0 | 26.77 | 8.64 | 3,504,960 | 329.36M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.213/mobilenetv2_w1-0864-6e58b1cb.params.log)) |
| IGCV3 x0.25 | 53.43 | 28.30 | 1,534,020 | 41.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.142/igcv3_wd4-2830-71abf6e0.params.log)) |
| IGCV3 x0.5 | 39.41 | 17.03 | 1,985,528 | 111.12M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.132/igcv3_wd2-1703-145b7089.params.log)) |
| IGCV3 x0.75 | 30.71 | 10.96 | 2,638,084 | 210.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.207/igcv3_w3d4-1096-3c7c86fc.params.log)) |
| IGCV3 x1.0 | 27.73 | 9.00 | 3,491,688 | 340.79M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.243/igcv3_w1-0900-e2c3da1c.params.log)) |
| MnasNet | 31.32 | 11.44 | 4,308,816 | 317.67M | From [zeusees/Mnasnet...Model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.117/mnasnet-1144-c972fec0.params.log)) |
| DARTS | 27.23 | 8.97 | 4,718,752 | 539.86M | From [quark0/darts] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.118/darts-0897-aafd6452.params.log)) |
| Xception | 20.99 | 5.56 | 22,855,952 | 8,403.63M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.115/xception-0556-bd2c1684.params.log)) |
| InceptionV3 | 21.22 | 5.59 | 23,834,568 | 5,743.06M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.92/inceptionv3-0559-6c087967.params.log)) |
| InceptionV4 | 20.60 | 5.25 | 42,679,816 | 12,304.93M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.105/inceptionv4-0525-f7aa9536.params.log)) |
| InceptionResNetV2 | 19.96 | 4.94 | 55,843,464 | 13,188.64M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.107/inceptionresnetv2-0494-3328f7fa.params.log)) |
| PolyNet | 19.09 | 4.53 | 95,366,600 | 34,821.34M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.96/polynet-0453-74280314.params.log)) |
| NASNet-A 4@1056 | 25.37 | 7.95 | 5,289,978 | 584.90M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.97/nasnet_4a1056-0795-5c78908e.params.log)) |
| NASNet-A 6@4032 | 18.17 | 4.24 | 88,753,150 | 23,976.44M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.101/nasnet_6a4032-0424-73cca5fe.params.log)) |
| PNASNet-5-Large | 17.90 | 4.28 | 86,057,668 | 25,140.77M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.114/pnasnet5large-0428-998a548f.params.log)) |

### CIFAR-10

Some remarks:
- Testing subset is used for validation purpose.
- `Features` means feature extractor output size.

| Model | Error, % | Features | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: |  ---: | ---: | --- |
| NIN | 7.43 | 192 | 966,986 | 222.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.175/nin_cifar10-0743-9696dc1a.params.log)) |
| ResNet-20 | 5.97 | 64 | 272,474 | 41.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet20_cifar10-0597-13c5ab19.params.log)) |
| ResNet-56 | 4.52 | 64 | 855,770 | 127.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet56_cifar10-0452-a73e63e9.params.log)) |
| ResNet-110 | 3.69 | 64 | 1,730,714 | 255.70M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet110_cifar10-0369-f89f1c4d.params.log)) |
| ResNet-164(BN) | 3.68 | 256 | 1,704,154 | 255.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.179/resnet164bn_cifar10-0368-e7941eee.params.log)) |
| ResNet-1001 | 3.28 | 256 | 10,328,602 | 1,536.40M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.201/resnet1001_cifar10-0328-bb979d53.params.log)) |
| ResNet-1202 | 3.53 | 64 | 19,424,026 | 2,857.17M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.214/resnet1202_cifar10-0353-377510a6.params.log)) |
| PreResNet-20 | 6.51 | 64 | 272,282 | 41.27M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet20_cifar10-0651-daa89573.params.log)) |
| PreResNet-56 | 4.49 | 64 | 855,578 | 127.03M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet56_cifar10-0449-cb37cb9d.params.log)) |
| PreResNet-110 | 3.86 | 64 | 1,730,522 | 255.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet110_cifar10-0386-d6d4b7bd.params.log)) |
| PreResNet-164(BN) | 3.64 | 256 | 1,703,258 | 255.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.196/preresnet164bn_cifar10-0364-7ecf30cb.params.log)) |
| PreResNet-1001 | 2.65 | 256 | 10,327,706 | 1,536.18M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.209/preresnet1001_cifar10-0265-50507ff7.params.log)) |
| PreResNet-1202 | 3.39 | 64 | 19,423,834 | 2,857.14M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.246/preresnet1202_cifar10-0339-942cf6f2.params.log)) |
| ResNeXt-29 (32x4d) | 3.15 | 1024 | 4,775,754 | 780.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.169/resnext29_32x4d_cifar10-0315-c8a1beda.params.log)) |
| ResNeXt-29 (16x64d) | 2.41 | 1024 | 68,155,210 | 10,709.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.176/resnext29_16x64d_cifar10-0241-76b97a4d.params.log)) |
| PyramidNet-110 (a=48) | 3.72 | 64 | 1,772,706 | 408.37M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.184/pyramidnet110_a48_cifar10-0372-35b94d05.params.log)) |
| PyramidNet-110 (a=84) | 2.98 | 100 | 3,904,446 | 778.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.185/pyramidnet110_a84_cifar10-0298-81710d7a.params.log)) |
| PyramidNet-110 (a=270) | 2.51 | 286 | 28,485,477 | 4,730.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.194/pyramidnet110_a270_cifar10-0251-1e769ce5.params.log)) |
| DenseNet-40 (k=12) | 5.61 | 258 | 599,050 | 210.80M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.193/densenet40_k12_cifar10-0561-28dc0035.params.log)) |
| DenseNet-BC-40 (k=12) | 6.43 | 132 | 176,122 | 74.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.231/densenet40_k12_bc_cifar10-0643-7fdeda31.params.log)) |
| DenseNet-BC-40 (k=24) | 4.52 | 264 | 690,346 | 293.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.220/densenet40_k24_bc_cifar10-0452-13fa807e.params.log)) |
| DenseNet-BC-40 (k=36) | 4.04 | 396 | 1,542,682 | 654.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.224/densenet40_k36_bc_cifar10-0404-4c154567.params.log)) |
| DenseNet-100 (k=12) | 3.66 | 678 | 4,068,490 | 1,353.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.205/densenet100_k12_cifar10-0366-4e371ccb.params.log)) |
| DenseNet-BC-100 (k=12) | 4.16 | 342 | 769,162 | 298.45M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.189/densenet100_k12_bc_cifar10-0416-6685d1f4.params.log)) |
| X-DenseNet-BC-40-2 (k=24) | 5.31 | 264 | 690,346 | 293.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.226/xdensenet40_2_k24_bc_cifar10-0531-66c9d384.params.log)) |
| X-DenseNet-BC-40-2 (k=36) | 4.37 | 396 | 1,542,682 | 654.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.233/xdensenet40_2_k36_bc_cifar10-0437-e9bf4192.params.log)) |
| WRN-16-10 | 2.93 | 640 | 17,116,634 | 2,414.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn16_10_cifar10-0293-ecf1c17c.params.log)) |
| WRN-28-10 | 2.39 | 640 | 36,479,194 | 5,246.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn28_10_cifar10-0239-16f3c8a2.params.log)) |
| WRN-40-8 | 2.37 | 512 | 35,748,314 | 5,176.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn40_8_cifar10-0237-3b81d261.params.log)) |
| RoR-3-56 | 5.43 | 64 | 762,746 | 113.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.228/ror3_56_cifar10-0543-ee31a69a.params.log)) |
| RoR-3-110 | 4.35 | 64 | 1,637,690 | 242.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.235/ror3_110_cifar10-0435-03599165.params.log)) |
| Shake-Shake-ResNet-20-2x16d | 5.15 | 64 | 541,082 | 81.78M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.215/shakeshakeresnet20_2x16d_cifar10-0515-a7b8a2f7.params.log)) |
| Shake-Shake-ResNet-26-2x32d | 3.17 | 64 | 2,923,162 | 428.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.217/shakeshakeresnet26_2x32d_cifar10-0317-21e60e62.params.log)) |

### CIFAR-100

Some remarks:
- Testing subset is used for validation purpose.

| Model | Error, % | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | --- |
| NIN | 28.39 | 984,356 | 224.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.183/nin_cifar100-2839-eed0e9af.params.log)) |
| ResNet-20 | 29.64 | 278,324 | 41.30M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.180/resnet20_cifar100-2964-4e144352.params.log)) |
| ResNet-56 | 24.88 | 861,620 | 127.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.181/resnet56_cifar100-2488-59097710.params.log)) |
| ResNet-110 | 22.80 | 1,736,564 | 255.71M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.190/resnet110_cifar100-2280-6c5fa14b.params.log)) |
| ResNet-164(BN) | 20.44 | 1,727,284 | 255.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.182/resnet164bn_cifar100-2044-c7db7b5e.params.log)) |
| PreResNet-20 | 30.22 | 278,132 | 41.28M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.187/preresnet20_cifar100-3022-37f15365.params.log)) |
| PreResNet-56 | 25.05 | 861,428 | 127.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.188/preresnet56_cifar100-2505-4c39e83f.params.log)) |
| PreResNet-110 | 22.67 | 1,736,372 | 255.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.191/preresnet110_cifar100-2267-18cf4161.params.log)) |
| PreResNet-164(BN) | 20.18 | 1,726,388 | 255.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.192/preresnet164bn_cifar100-2018-a20557c8.params.log)) |
| ResNeXt-29 (32x4d) | 19.50 | 4,868,004 | 780.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.200/resnext29_32x4d_cifar100-1950-5f2eedcd.params.log)) |
| PyramidNet-110 (a=48) | 20.95 | 1,778,556 | 408.38M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.186/pyramidnet110_a48_cifar100-2095-00fd42a0.params.log)) |
| PyramidNet-110 (a=84) | 18.87 | 3,913,536 | 778.16M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.199/pyramidnet110_a84_cifar100-1887-6712d5dc.params.log)) |
| DenseNet-40 (k=12) | 24.90 | 622,360 | 210.82M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.195/densenet40_k12_cifar100-2490-908f02ba.params.log)) |
| DenseNet-BC-40 (k=12) | 28.41 | 188,092 | 74.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.232/densenet40_k12_bc_cifar100-2841-35cd8e6a.params.log)) |
| DenseNet-BC-40 (k=24) | 22.67 | 714,196 | 293.11M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.221/densenet40_k24_bc_cifar100-2267-2c4ef7c4.params.log)) |
| DenseNet-BC-40 (k=36) | 20.50 | 1,578,412 | 654.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.225/densenet40_k36_bc_cifar100-2050-d7275d39.params.log)) |
| DenseNet-100 (k=12) | 19.64 | 4,129,600 | 1,353.62M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.206/densenet100_k12_cifar100-1964-2ed5ec27.params.log)) |
| DenseNet-BC-100 (k=12) | 21.19 | 800,032 | 298.48M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.208/densenet100_k12_bc_cifar100-2119-fbd8a54c.params.log)) |
| X-DenseNet-BC-40-2 (k=24) | 23.96 | 714,196 | 293.11M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.227/xdensenet40_2_k24_bc_cifar100-2396-73d5ba88.params.log)) |
| X-DenseNet-BC-40-2 (k=36) | 21.65 | 1,578,412 | 654.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.234/xdensenet40_2_k36_bc_cifar100-2165-78b6e754.params.log)) |
| WRN-16-10 | 18.95 | 17,174,324 | 2,414.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.204/wrn16_10_cifar100-1895-bcb5c89c.params.log)) |
| RoR-3-56 | 25.49 | 768,596 | 113.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.229/ror3_56_cifar100-2549-43345593.params.log)) |
| RoR-3-110 | 23.64 | 1,643,540 | 242.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.236/ror3_110_cifar100-2364-b8c4d317.params.log)) |
| Shake-Shake-ResNet-20-2x16d | 29.22 | 546,932 | 81.79M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.247/shakeshakeresnet20_2x16d_cifar100-2922-e46e31a7.params.log)) |
| Shake-Shake-ResNet-26-2x32d | 18.80 | 2,934,772 | 428.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.222/shakeshakeresnet26_2x32d_cifar100-1880-bd46a741.params.log)) |

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