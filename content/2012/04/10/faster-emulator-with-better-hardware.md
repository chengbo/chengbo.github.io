---
author: chengbo
comments: true
date: 2012-04-10 15:18:02+00:00
layout: post
title: 更快的，更好的支持硬件的模拟器
categories:
- Android翻译
tags:
- Android
- 模拟器
---

原文：[http://android-developers.blogspot.com/2012/04/faster-emulator-with-better-hardware.html](http://android-developers.blogspot.com/2012/04/faster-emulator-with-better-hardware.html)

_[This post is by Xavier Ducrohet and Reto Meier of the Android engineering team. — Tim Bray.]_

Android模拟器是开发和测试Android程序的一个关键工具。目前Android设备的功能以及多样性发展的日益迅猛，模拟器要跟上步伐十分的困难。

今天我们激动的宣布，模拟器做了一些十分显著的改进，包括激动人心的性能提升，众多硬件特性，尤其是传感器和多点触控的支持。


### 加入GPU支持


今天我们发布的系统镜像内置了GPU支持（Android 4.0.3 r2）。Android日益依赖GPU来提高性能，所以新模拟器的差异十分显著。在下面的视频中（需翻墙才能看）模拟器依旧翻译着ARM指令（运行模拟器的宿主系统一般是x86平台，此镜像是ARM平台的，所以中间存在着ARM->x86指令的转换。之前没有GPU支持，运行如此高分辨率的模拟器并不流畅）；GPU可以让性能提升不少。



一个额外的红利，我们现在已经支持OpenGL ES 2.0了，所以你的OpenGL游戏可以在模拟器中运行了。

请注意的是，目前有很多种的GPU，我们并没有用所有GPU对这个beta版的模拟器做测试，所以，如果你有什么意见或者遇到了什么问题，请[联系我们](http://code.google.com/p/android/issues/entry?template=Tools%20GPU%20bug%20report)。


### 模拟更多的硬件特性


移动设备的硬件特性是一个开发平台的重要组成部分，所以我们也高兴的宣布，除了去年加入的摄像头支持，现在还可以使用一个绑定的Android设备来支持传感器和多点触控了。

我们还在为模拟器支持更多的硬件特性，包括蓝牙和NFC（近距离无线通信），而努力。


### 优化的CPU性能


我们同样也优化了Android模拟器的CPU性能。硬件浮点运算操作在冰淇淋三明治版本(Android 4.0)之上的版本中有效，它让模拟CPU操作大概快了2倍。

上一周，我们发布了包括x86系统镜像和主机驱动程序的Android开发工具r17版本，可以让模拟器使用x86指令执行，大大提高了执行效率。

下面这个视频显示了两个CPU相关的程序，一个有虚化（virtualization），一个没有，在两个运行着相同系统镜像的模拟器上运行的情况。（同样需要翻墙）




### 构建一个现代化的模拟器


因为Android平台允许应用程序和系统组件之间的深层相互操作，所以我们必须提供一个有着完整系统镜像的模拟器。我们的模拟器虚拟了一个完整的设备：硬件，内核，底层系统库和应用框架。

当然，系统一般被虚拟为ARM CPU的设备；之前，我们用软件来虚拟这些指令，它一直工作的不错，直到包括更多动画和更加复杂的Android 3.0的到来。

我们缺少的是Android x86的支持，和上周r17版本的SDK工具中的GPU支持。把模拟器的OpenGL ES 2.0指令传给宿主操作系统，转换成标准的OpenGL 2.0，然后用宿主GPU来执行，这样模拟器就支持GPU了。


### 总结


Android生态系统有着很多的来自不同厂商的设备。开发人员需要一个不用买设备就可以测试程序的途径。同时一个快速的，更真实的模拟器有着极大的帮助。

我们希望这些新的优化能够让模拟器在你的开发和测试过程中更加有用，同时期盼能进一步的为你优化它。

本文由Roy最初发表于：[http://blog.chengbo.net/2012/04/10/faster-emulator-with-better-hardware.html](http://blog.chengbo.net/2012/04/10/faster-emulator-with-better-hardware.html)，你可以在保持文章完整和保留本声明的情况下转帖、分发和印刷等。
