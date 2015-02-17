---
author: chengbo
comments: true
date: 2007-01-18 11:09:30+00:00
layout: post
title: MT3.34发布了
---

Movable Type 3.34 发布了，强烈建议大家都升级：
	
  * 修复了重要的[XSS缺陷](http://www.sixapart.com/movabletype/beta/distros/MT-3.34-beta-Release-Notes.html)
  * 免费，推荐所有用户都升级
  * 更简单的启用FastCGI方式以获得[15倍的性能提升](http://www.sixapart.com/developers/product_documentation/movable_type/fastcgi_benchmarks_for_movable.html)

在3.34之前，用户若要启用FastCGI，则要手动更改一些MT的源代码，现在3.34把这些改动已经集成进3.34版本中了，用户不需再做任何操作，程序会根据服务器的环境自动启用FastCGI。

FastCGI有什么好处？

以FastCGI方式运行Movable Type仍然是可选的，为何要如此强烈的推荐用户升级呢？以下是以FastCGI方式运行MT的几个重要理由：

  * **提升应用程序性能** – FastCGI能提升15倍的性能，性能提升如此之大是因为程序会被缓存在内存中，减少了页面加载和数据库访问时间。
  * **提升评论系统性能** – Movable Type会把所有的评论都存入数据库以便用户自己去决定要不要审批这些评论。因此处理评论的时间是提升性能的一个重要因素。	
  * **提升程序可靠性** – MT应用程序中加载一个页面需要更少的资源，减少了网络流量和数据库负载，服务器的资源可以更多的留给其它程序或组件使用。
  * **提升系统在Spam攻击下的恢复力** – 当blog遭受spam的攻击时，系统会加载很多资源。系统会把所有的评论都保留下来以便用户区分这到底是不是spam。在FaseCGI方式下，MT在内存中运行而降低了网络流量和数据库负载，因而评论的处理速度会被很快。

说了那么多理由，其实就一句话，FastCGI可以把程序缓存起来，这样程序运行速度就会快会多。就像你的电脑，内存多了，速度自然就快了。

更多资源：
	
  * [Movable Type/FastCGI 安装指南](http://www.lifewiki.net/sixapart/HostingMTUnderFastCGI)
  * [Movable Type 和 FastCGI 基准](http://www.sixapart.com/developers/product_documentation/movable_type/fastcgi_benchmarks_for_movable.html)
  * [FastCGI 主页](http://www.fastcgi.com/)
  * 推荐的FastCGI实现方式
  * [fcgid](http://fastcgi.coremail.cn/)
  * [mod_fastcgi](http://www.fastcgi.com/mod_fastcgi/docs/mod_fastcgi.html)
