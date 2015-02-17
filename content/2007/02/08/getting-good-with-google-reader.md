---
author: chengbo
comments: true
date: 2007-02-08 05:59:54+00:00
layout: post
title: 更好的使用Google Reader
---

![Lifehacker google reader header](http://lifehacker.com/assets/resources/2007/02/Lifehacker%20google%20reader%20header.png)

_作者：Adam Pash_

Google Reader是一个很好的RSS阅读器，但是如果你不花点儿时间去研究它的说明文档的话，你也许不能完全享用到它带给你的强大功能。

今天，我会向你介绍一下Google这款强大的新闻阅读器，我会先重点讲一下它强大而又省时的快捷键，然后再介绍一些我喜欢的周边扩展，这样可以让你尽快上手这款世界上功能最为强大的新闻阅读器。

#### Google Reader和它奇妙的快捷键

首先，因为我是快捷键的超级粉丝，所以我先介绍一下Google Reader自身集成的，功能强大到难以置信的快捷键。我想动画会比较直观一些，所以我把这些快捷键的操作录成了一部短片放在下面：

如果你用过我曾经介绍的[Gmail Macros Greasemonkey脚本](http://lifehacker.com/software/gmail/hack-attack-become-a-gmail-master-161399.php)，那么你肯定会觉得Google Reader透明的快捷窗口和它的简直一模一样。这没什么奇怪的，因为Gmail Macros Greasemonkey脚本的作者就是Google Reader的首席界面设计师。

作为开始，我们来看看我在视频里用过的一些快捷键：

![home.png](http://lifehacker.com/assets/resources/2007/02/home.png)

**静态菜单快捷键：** Google Reader的一些静态菜单（注：非动态生成的，比如你订阅的文章就是系统每次动态生成的），如Home，All Item，Starred Items都有快捷键。按`g + a` (**G**o + **A**ll Items)可以跳转到你订阅的所有文章。 同样，按`g + h` (**g**oes **H**ome)跳转到Home，而按`g + s` (**g**oes to your **S**tarred Items)则跳转到所有加星的文章。

**快速定位你的订阅：**好吧，尽管刚才说的定位快捷键都比较好用，但如果有快捷键可以快速定位到我订阅的种子上就好了。当然有了，你可以按`g + u + Feed标题`来定位到某一个特定的种子。比如，按`g + u + Lifehacker`会将你定位到Lifehacker的种子(假设你已经订阅了它)。

![subscriptions](http://lifehacker.com/assets/resources/2007/02/subscriptions.png)

按`g + u`后，会有一个弹出窗口（注：实际上只是一个动态的div）的来显示你目前订阅的所有种子。系统会根据你的输入内容来筛选这个列表，当有多个候选种子时，最顶部的会被默认选中。这时可以按键盘上的方向键来定位到你想要找的种子，或者继续输入直到只剩最后一个匹配的。

**使用Labels/Tags分类：**如果你平常用label和tag（Google并不确定怎么命名它们，有时叫label，有时又叫tag）来分类你的种子，那么Google Reader很乐意为你效劳。使用label/tag来查找种子，可以按`g + t + tag名`，或`g + l + label名`。我不想把事情讲的很复杂，实际上label和tag在Google Reader里没什么区别，随便哪个都一样。由于在Gmail中使用的是label这种叫法，所以从现在起，我把它们都叫label。

![change folder](http://lifehacker.com/assets/resources/2007/02/change%20folder.png)

**给种子和文章打Label：**每当你新订阅了一个种子，你都可以把它放到一个folder里。本质上来说，把种子放到一个folder中和建立一个label，然后把这个种子里的所有文章都打上这个label没什么区别，因为Google Reader使用的就是folder这种机制来完成筛选操作的。如果你现在有一个叫“productivity”的label/folder，那么就把Lifehacker加到里面吧，这样Lifehacker所有的文章都会被自动打上“productivity”的label。

你还可以为每篇单独的文章添加label。如果你想为一篇文章添加Label，请按`l + label名`或者 `t + tag名`（随便哪一种都可以）。你还可以同时添加多个Label，之间用逗号分开（注，是英文半角逗号，即“,”，而非“，”）。若添加的Label是原来没有的，那么系统会把它添加到你的Label库中；也可以使用库中已经存在的，系统会生成一个下拉列表来显示与你输入最为相近的Label。

![labels and tags](http://lifehacker.com/assets/resources/2007/02/labels%20and%20tags.png)

**快速定位文章:**Google Reader有许多方法可以让你从一篇文章跳转到另一篇文章。如果你使用过Gmail中的快捷键，那么其中有很多对你来说是再熟悉不过的了。你可以：
	
  * 通过按`j` (下) 和 `k` (上)从一篇文章跳转到另一篇文章。
  * 通过按`n` (**n**ext下一个) 和 `p` (**p**revious上一个)从一篇文章跳转到另一篇文章而不需要打开文章的详细内容。如果你选择的是“Expanded view”模式，j/k和n/p的作用相同。
  * 如果你用的是“List View”模式，通过`n` 和 `p`键定位到某篇文章，按回车键或者`o`会打开/关闭此篇文章的详细内容。(顺便说一下，你可以按`1` 或 `2`来切换“Expanded view”和“List View”模式。）
  * 按`s`可以把当前文章加星（**S**tar）或者去掉已经是加星文章的星星。
  * 按`v`可以打开一个新的Tab页/窗口来显示（**V**iew）当前文章在网站上的原文。
  * 按`m`可以把一篇文章标记（**M**ark）为已读。
  * 全屏（f**u**llscreen）显示请按`u`。`u`键可以展开/收拢侧边栏，最大化你的阅读空间。[[Quick Online Tips](http://www.quickonlinetips.com/archives/2007/02/quick-tips-for-google-reader-power-users/)]

**更多快捷键：**上面提及的导航快捷键只是Google Reader提供的所有快捷键中最为实用的一部分，更多快捷键请参见[Google Reader帮助问答](http://www.google.com/help/reader/faq.html#shortcuts).

#### Google Reader周边扩展推荐

除了它与生俱来的漂亮外观和吸引力外，今天有关Google Reader介绍的另一部分，就是它还有相当数量的实用扩展，不管是Google自身还是粉丝们自己开发的。我的最爱有：

![google reader notifier](http://www.lifehacker.com/assets/resources/2006/12/google%20reader%20notifier.png) 
	
  * Google Reader Notifiers: 尽管Google刚刚发布了官方的Reader notifier，但是还是有很多的Reader爱好者维护着他们自己的版本。你可以找到适用于[Windows](http://lifehacker.com/software/google-reader/download-of-the-day-google-reader-notifier-windows-223094.php)，[Mac](http://lifehacker.com/software/google-reader/download-of-the-day-google-reader-notifier-mac-213663.php)，和[Firefox](http://lifehacker.com/software/google-reader/download-of-the-day-google-reader-notifier-firefox-219073.php)的Google Reader Notifier。
  * 使用Google Co-op和[这个Greasemonkey脚本](http://lifehacker.com/software/google-reader/download-of-the-day--google-reader-custom-search-greasemonkey-225612.php)为你订阅的种子创建一个自定义搜索。

![subscribed.png](http://www.lifehacker.com/assets/resources/2006/10/subscribed.png)
	
  * 还是Greasemonkey，[Smart Google Reader subscribe button](http://lifehacker.com/software/google-reader/download-of-the-day-smart-google-reader-subscribe-button-greasemonkey-script-208458.php) (同样是Mihai Parparita开发的)可以让你很容易的订阅一个站点的更新，并且会提示提示你之前是否已经订阅过。如果你订阅了相当多的种子（就像我们一样），它对你相当有用。
  * 将Google Reader集成进Gmail - 还是通过[Greasemonkey脚本](http://lifehacker.com/software/google-reader/integrate-google-reader-with-gmail-via-greasemonkey-207679.php) (Mihai Parparita开发).

有关Google Reader的特性和自定义方法，你有什么高见请在评论中告诉我们。

_**[Adam Pash](http://adampash.org/)**是Lifehacker的高级编辑。他的特写[Hack Attack](http://www.lifehacker.com/software/hack-attack/)将于每周二在Lifehacker上和大家见面。订阅[Hack Attack RSS种子](http://www.lifehacker.com/software/hack-attack/index.xml)以便将来在你的阅读器中浏览此系列的新文章。_

技巧来自[Lifehacker](http://lifehacker.com/software/google-reader/hack-attack-getting-good-with-google-reader-233712.php)
