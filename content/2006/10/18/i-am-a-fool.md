---
author: chengbo
comments: true
date: 2006-10-18 13:53:39+00:00
layout: post
title: 我就是一SB
---

对自己很无语，所以写了这样一个标题，我很郁闷我自己为什么同样的错误会犯很多次呢？

昨天完成了DEV的测试，移至QC上再测时却出了问题，最后发现是因为我改过数据库结构，但是却没有改建数据库的脚本，导致QC上的表结构和DEV上的不一致。前不久我就犯过这个错误，这次又来了，虽说leader没说我什么，但是看的出，他对我相当的无语。

想了一下我经常犯的错：

* 异常未记日志，结果出了BUG却找不出问题所在
* 下班不check in代码，结果出现过两次代码丢失，哭
* 字符串比较不考虑大小写不同的情况，结果经常出现一些莫名其妙的BUG
* 改了数据库却不改脚本，结果发布的时候直接把未修改的脚本发布了，后果可想而知
* 脚本经常忘了按规范来写，结果一次又一次的被DBA退回
* 还有一些暂时没想到，不过可以肯定的是，我经常把自己弄的很狼狈。

哎，我做事情太没有条理了，从日常生活习惯就可以看出来，不幸的是，这个坏习惯对于我所从事的职业来说是致命的。如果这个坏习惯一直改不了，我一辈子都只能在coder这个层次里混。庆幸的是，我遇到了一个好脾气的leader，要是其它人，也许我已经死了N遍了……

工作有10个月了，我早已没有当初那种对于工作的新鲜感，每天的生活都很麻木机械，就像一个机器一样不停的做着一些重复的事。近段时间我工作不积极主动，上班时间经常浏览与工作无关的网站，每天就盼望下班，盼望周末，技术书也极少看了，这样下去怎么得了？

我急需心理调节……
