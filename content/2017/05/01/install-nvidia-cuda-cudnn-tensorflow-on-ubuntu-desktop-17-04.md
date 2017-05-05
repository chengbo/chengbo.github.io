---
author: chengbo
comments: true
date: 2017-05-01 17:33:00-00:00
layout: post
title: Ubuntu上TensorFlow安装步骤
tags:
- Ubuntu
- TensorFlow
---

深度学习(Deep learning)目前挺火的，我也准备赶一下潮流，提升一下自己。正好长草GTX 1060很久了，一直没买，这次就趁着这次想要学习的机会咬牙割肉买了张，就算半途而废了，也可以玩玩游戏。1070等就不考虑了，钱包不够。

买回来把显卡装上，进Windows 10，装驱动，然后玩了一把星际争霸（一代），居然没感觉比我之前用的Intel HD 4600有什么提升，差评，想退货了（玩笑）。

言归正传，深度学习有不少框架，我随便选了个TensorFlow来入门。根据[安装文档](https://www.tensorflow.org/install/)，一步一步的装好，步骤记录如下：

## 安装Ubuntu

我安装的是最新的Ubuntu Desktop 17.04。[下载](https://www.ubuntu.com/download/desktop)一个ISO文件做成启动U盘，然后跟着提示安装即可。

## 安装NVIDIA驱动

```
# add-apt-repository ppa:graphics-drivers/ppa
# apt update
# apt install nvidia-375
```

## 安装CUDA® Toolkit 8.0
去[NVIDIA网站](https://developer.nvidia.com/cuda-downloads)下载安装包，选择Linux，x86_64，Ubuntu，16.04，deb (local)

```
# dpkg -i /path/to/your/file-just-downloaded.deb
# apt update
# apt install cuda
```

设置环境变量

```
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda
```
也可以把上面的设置放到`~/.profile`里，永久生效。

## 安装cuDNN
去[NVIDIA网站](https://developer.nvidia.com/rdp/cudnn-download)下载安装包，下载前需要登录，如果没有帐号，可以先注册一个，免费的。
选择
Download cuDNN v5.1 (Jan 20, 2017), for CUDA 8.0
cuDNN v5.1 Library for Linux
下载后
```
$ tar -zxvf /path/to/your/file-just-downloaded.tgz
# cp cuda/include/*.h /usr/local/cuda/include
# cp cuda/lib64/* /usr/local/cuda/lib64
```

## 安装libcupti-dev
```
# apt install libcupti-dev
```

## 安装virtualenv
```
# apt install python-pip python-dev python-virtualenv
```

## 安装TensorFlow
```
$ virtualenv --system-site-packages ~/tensorflow
$ cd ~/tensorflow
$ source bin/active
$ pip install tensorflow-gpu
```

## 验证安装
```
$ python
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))
```
如果看到有输出Hello, TensorFlow!，就说明安装成功了。
