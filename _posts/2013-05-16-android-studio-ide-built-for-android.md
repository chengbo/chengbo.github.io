---
author: chengbo
comments: true
date: 2013-05-16 23:35:36+00:00
layout: post
title: Android Studio：为Android定制的IDE
categories:
- Android翻译
tags:
- Android
- Android-Studio
- IDE
---

原文：[http://android-developers.blogspot.com/2013/05/android-studio-ide-built-for-android.html](http://android-developers.blogspot.com/2013/05/android-studio-ide-built-for-android.html)

_由 [Xavier Ducrohet](https://plus.google.com/109385828142935151413), Tor Norbye, Katherine Chou发表_


![](http://blog.chengbo.net/wp-content/uploads/2013/05/google-io-lockup-2.png)




![](http://blog.chengbo.net/wp-content/uploads/2013/05/Studio_table.png)


今天在Google I/O上，我们发布了一个专为Android开发者准备的新IDE：Android Studio，它可以免费使用，你现在就可以试试它的早期预览版。

我们与最流行的Java IDE之一，[IntelliJ IDEA 社区版](http://www.jetbrains.com/idea/)，的开发公司[JetBrains](http://www.jetbrains.com)合作，开发了Android Studio。在强大的IntelliJ IDEA 社区版的基础上，我们添加了一系列针对Android开发的功能，可以提高你的工作效率。


### 可扩展的构建工具


我们知道你需要一个适合项目的构建系统，Android Studio的新构建系统基于[Gradle](http://www.gradle.org/)，它不仅提供了灵活、定制化的构建方式，还有依赖管理等更多的特性。

这个新的构建系统不仅可以让你在IDE中构建项目，它同样也支持持续集成服务器。在整个工作流程中，N多杂七杂八的工具旁，你可以更方便的管理你复杂的构建配置项。如想了解更多，请查看[预览版文档](http://tools.android.com/tech-docs/new-build-system/user-guide)。


![](http://blog.chengbo.net/wp-content/uploads/2013/05/laptop600.png)




### 强大的代码编辑


Android Studio包括一个强大的代码编辑器，这个编辑器基于IntelliJ IDEA，提供了诸如智能提示，高级代码重构，深度静态代码分析等功能。

智能提示中的查找内嵌资源，可以让你在编辑后台资源的时候，更快速的阅读资源对应的代码。高级[代码重构](http://www.jetbrains.com/idea/features/refactoring.html)可以让你快速的，放心的优化整个项目中代码。

静态代码分析可以让你更快的定位bug。在由IntelliJ IDEA提供的成千上万inspection的基础上，我们又加了一些定制化的inspection。比如，我们为Android API添加了一些元数据，这些元数据指示哪些方法可以返回null，而哪些方法又不可以；某个方法接受哪些常量值，等等。Android Studio就可以通过它们来分析你的代码，找出潜在的错误。


![](http://blog.chengbo.net/wp-content/uploads/2013/05/ide-refactor.png)




![](http://blog.chengbo.net/wp-content/uploads/2013/05/ide-smart.png)




![](http://blog.chengbo.net/wp-content/uploads/2013/05/ide-resourcelookup2.png)




### 更平滑、更丰富的图形界面


过去几年，我们为ADT添加了一些拖放控件的UI功能，现在我们正在努力为Android Studio移植它们。这个Android Studio版本，你可以在IDE中预览你的布局文件在不同尺寸，语言和版本的设备中的显示效果。下面会展示XML编辑页面中预览不同的配置。


### 方便的使用Google services


我们想让你更方便的在IDE中使用Google Service的强大功能。首先，我们可以让你直接在IDE中将诸如[Google Cloud Messaging](http://developer.android.com/google/gcm/index.html)（GCM）的Google Service集成到App中。

我们还添加了一个名为[ADT Translation Manager Plugin](http://developer.android.com/sdk/installing/installing-adt.html#tmgr)的插件来帮助你本地化你的App。通过这个插件，你可以把字符串导出到Google Play Developer Console中翻译，然后下载并导入这些翻译好的字符串回项目中。


### 开源


下周开始我们的所有开发工作就会开源，到时候你就可以下载之，然后向我们提交你的代码。Android Studio的代码放在[AOSP](https://android.googlesource.com/platform/tools/adt/idea/)中。



### 试用Android Studio并给我们反馈


[开始试用Android Studio](http://developer.android.com/sdk/installing/studio.html) 并给我们反馈吧！它是免费的，并且下载包中包括你所需要的一切：IDE，最新的SDK以及最新的Android平台等。

注意：这只是一个早期预览版，只适合喜欢尝鲜，或想决定Android工具未来发展方向的人。如果你的App有大量用户使用的话，现在还不是时候迁移到新工具上。我们还将继续支持Eclipse作为首要的开发平台。

如果你有任何意见或建议，请通过[Android Studio issue tracker](https://code.google.com/p/android/issues/entry?template=Android%20Studio%20bug&comment=Build:%20AI-130.675642,%2020130514)告诉我们。








[Join the discussion on](https://plus.google.com/108967384991768947849/posts/Sr8LNyHDuax)

[+Android Developers](https://plus.google.com/108967384991768947849/posts/Sr8LNyHDuax/)






[![](https://ssl.gstatic.com/images/icons/gplus-32.png)](https://plus.google.com/108967384991768947849/posts/Sr8LNyHDuax)





本文由Roy最初发表于：[http://blog.chengbo.net/2013/05/17/android-studio-ide-built-for-android.html](http://blog.chengbo.net/2013/05/17/android-studio-ide-built-for-android.html)，你可以在保持文章完整和保留本声明的情况下转帖、分发和印刷等。
