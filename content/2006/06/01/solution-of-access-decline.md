---
author: chengbo
comments: true
date: 2006-06-01 17:06:41+00:00
layout: post
title: 双击U盘出现“拒绝访问”的解决方法
---

拿U盘拷了点资料拿到老师的机器上看，回来再把它插到我自己的电脑上，就出问题了。双击U盘图标后，会出现“拒绝访问”的对话框，同学说这是病毒，现在在学校里很流行，只要点右键，选“打开”就可以进去了。听了这话，我就明白了，肯定是病毒在U盘里加了一个Autorun的东东，所以双击会有问题。点右键选“打开”打开U盘后，果然发现了一个autorun.inf的隐藏系统文件和一个RECYCLER文件夹，把它们两个都删了，然后插拔一次U盘，问题就解决了。 得到一个教训，如果不需要拷文件到U盘里，最好打开它的只读开关。