---
author: chengbo
comments: true
date: 2007-02-14 10:48:16+00:00
layout: post
title: Gmail被封掉时的访问方法
---

我的朋友Mike，他们公司把Gmail封了，所以他问我有没有一种简单的方法可以突破防火墙？我说，其实很简单。

我不明白**为什么**有的公司要把Gmail封掉。我认为人们使用自己私人的Gmail邮箱来转发一些笑话，图片，视频，会比用公司的邮箱要好的多。

你可以通过不同的URL来访问Gmail。公司通常只封了其中的几个。

#### #1: 尝试不同的网址

用 [https://mail.google.com](https://mail.google.com) 代替 [http://mail.google.com](http://mail.google.com)

你还可以试试：

* [http://www.gmail.com](http://www.gmail.com) 或 [https://www.gmail.com](https://www.gmail.com)
* [http://gmail.com](http://gmail.com) 或 [https://gmail.com](https://gmail.com)
* [http://m.gmail.com](http://m.gmail.com) 或 [https://m.gmail.com](https://m.gmail.com)
* [http://googlemail.com](http://googlemail.com) 或 [https://googlemail.com](https://googlemail.com)
* [http://mail.google.com/mail/x/](http://mail.google.com/mail/x/) 或 [https://mail.google.com/mail/x/](https://mail.google.com/mail/x/)

#### #2: 使用电子邮件收发程序连接Gmail（通过POP协议）

如果上面的网址都被封掉了，那么最简单的方法就是**使用电子邮件收发程序**（Microsoft Outlook等）来连接Gmail。使用方法参见[Google帮助中心](http://mail.google.com/support/bin/answer.py?answer=12103)。

![gmailconfig.gif](http://blog.chengbo.net/2007/02/15/gmailconfig.gif)

#### #3: 用Google Desktop来访问Gmail

另一个选择就是安装[Google Desktop](http://desktop.google.com/about.html#whatis)。它可以通过代理访问Gmail。但是不幸的是，Google Desktop也有可能被封了。

![email_listcache.gif](http://blog.chengbo.net/2007/02/15/email_listcache.gif)

#### #4: 用安装了Gmail Lite的Web服务器

如果你还坚定不移地想**访问Gmail**，你还可以试试这个叫[Gmail Lite](http://www.google.ca/search?q=gmail+lite)的程序，它需要安装在你自己的web服务器上。

当然，大部分人都没有服务器，但是如果你继续搜索下去的话，你会找到一些安装了**Gmail Lite**，同时又供任何人使用的服务器。

把搜索到的服务器记下来，以便以后使用。

![gmaillite.png](http://blog.chengbo.net/2007/02/15/gmaillite.png)

注意，这个程序不是Google官方提供的。

#### #5: 向公司的IT行贿

![](http://blog.chengbo.net/2007/02/15/th_3c8284bb.jpg)永远要和IT搞好关系，这样会让你过的更轻松。可以通过下面的方式向他们行贿。

1. 佳肴
2. 美酒
3. 电影 最好是翻印版 - 尽管IT的电影收藏可能比你还多）
4. 动漫
5. 调情
6. [性](http://engtech.wordpress.com/2006/09/28/jeff-atwood-code-monkey-very-simple-man/)

#### 关于更为普遍的代理

如果你想找一个能让你访问任何被封网站的代理时，[这个主题](http://www.digg.com/security/New_proxy_unblocks_myspace_and_gmail)里的一些回复可以给你一点建议。

有一个我非常喜欢的技巧：**让Google来给你当代理**。下面的这些网址通常都是可以访问的：

* 通过**Google翻译** (从English翻译到English)可以上你浏览世界上的所有网页。
* [http://translate.google.com/translate?u=http%3A%2F%2Fblog.chengbo.net&amp;langpair=zh-CN%7Czh-CN&amp;hl=en&amp;ie=UTF8](http://translate.google.com/translate?u=http%3A%2F%2Fblog.chengbo.net&amp;langpair=zh-CN%7Czh-CN&amp;hl=en&amp;ie=UTF8)
* 如果我的站点被封了，把上面的网址加入书签就可以顺利访问了。我还想知道它能不能帮我改正拼写错误？
* 通过**Google Web Toolkit** (改变了网页的显示方式)
* [http://www.google.com/gwt/n](http://www.google.com/gwt/n)
* 通过**Google XHTML** 手机转换器 (改变了网页的显示方式)
* [http://www.google.com/xhtml](http://www.google.com/xhtml)

我希望上面介绍的一些技巧不会对你的工作[productivity（效率）](http://engtech.wordpress.com/tag/productivity)有太大的影响。

#### 相关文章

* 标签为[Articles](http://engtech.wordpress.com/tag/engtecharticles), [How To](http://engtech.wordpress.com/tag/how-to), [Hacks](http://engtech.wordpress.com/tag/hacks), [Gmail](http://engtech.wordpress.com/tag/gmail) 和 [Google](http://engtech.wordpress.com/tag/google)的文章
* [Guide on How to Setup Two or More Gmail Accounts to Use One Account (Create, Forward, Link)](http://engtech.wordpress.com/2006/09/11/guide-on-how-to-setup-two-or-more-gmail-accounts-to-use-one-account-create-forward-link/)
* [The Holy Grail of Synchronization: How to synchronize Microsoft Outlook (multiple locations), Google Calendar, Gmail, iPod, and mobile phone with Funambol / ScheduleWorld](http://engtech.wordpress.com/2006/08/11/the-holy-grail-of-synchronization-how-to-synchronize-microsoft-outlook-multiple-locations-google-calendar-gmail-ipod-and-mobile-phone-with-funambol-scheduleworld/)

#### 代理列表

* [300个代理名单](http://sharjeelsayed.blogspot.com/2006/03/beat-censorship-using-these-proxies.html)
* [Element 14有一个web代理的名单](http://element14.wordpress.com/proxy-lists/)

[原文](http://engtech.wordpress.com/2006/10/04/how-to-access-gmail-when-its-blocked-at-work-or-school/)
