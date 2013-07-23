---
author: chengbo
comments: true
date: 2006-11-30 06:04:40+00:00
layout: post
title: 使用PHPProxy把虚拟空间变成HTTP代理
---

前几日在网上闲逛，看到一个[PHPProxy](http://idea.hosting.lv/a/phpproxy/)，注意它和这个[PHPProxy](http://www.phproxy.com/)不同，前者可以把你的PHP空间变成一个浏览器可直接使用的http 代理，而后者则只是一个表单，你需要在这个表单上提交需要访问资源的url，然后在框架中浏览，个人感觉后者不怎么好用。

代理的好处不言而喻，伟大的GFW让我们无法使用很多国外优秀的资源，通过代理，就相当于有了一个跳板，跳过GFW的拦截，去想去的地方冲浪(越狱?)。

我的blog空间每月的流量几百G，根本用不完，再加上网上找的代理都不是很稳定，今天能用明天说不定就不行了，所以这个东东很适合我，捣鼓了一下，终于成功了，好东西不敢独享，写下安装方法，希望对大家有点帮助。

首先看看http请求的流程可以帮助你正确的使用PHPProxy，如下：

| 1 你的浏览器
| 2 PHPProxy客户端模块(phpproxy.py)
| [3] 可能存在的客户端代理(比如你本来就是使用代理上网的，公司的代理等等)
| 4 PHP空间 + PHPProxy服务端模块(phpproxy.php)
| [5] 可能存在的服务器端代理(比如你的PHP空间也是用代理上网的)
\|/ 6 目标资源

说明：

首先浏览器(1)发送http请求到PHPProxy(2)，phpproxy.py(2)将这个http请求压缩到另一个http请求中，然后以表单参数的形式直接或通过可能存在在代理[3]发送到phpproxy.php(4)，phpproxy(4)收到请求后，解压出原始的http请求，直接或通过可能存在的proxy[5]发送到目标资源(6)。

原理讲完了，再看看具体怎样操作。

安装：

下载[phpproxy-0.6.tar.gz](http://idea.hosting.lv/a/phpproxy/phpproxy-0.6.tar.gz)，解压到server文件夹，打开phpproxy.php，把第7行里的1.2.3.4改成你的IP，这样就只有你才可以使用这个代理，当然也可以在行首加一个"#"字符，没有引号，注释掉第7行，这样所有的IP都具体访问权限了，此时一定要注意保密proxy地址，否则大家都来用这个proxy的话，空间的流量会让你吃不消的。上传整个server文件夹到你的空间中，记下它的路径，如http://blog.chengbo.net/phpproxy/server 。

下载[phpproxy.py.exe-0.6.zip](http://idea.hosting.lv/a/phpproxy/phpproxy.py.exe-0.6.zip)，解压到client文件夹，打开phpproxy.py.conf，定位到19行，把phpproxy的值设置成http://blog.chengbo.net/phpproxy/server。

使用：

运行client文件夹中的phpproxy.py.exe，保持命令窗口一直打开，把浏览器的代理地理设置成127.0.0.1:8080，OK了，试试[http://wordpress.com](http://wordpress.com/)，再用[http://www.google.com](http://www.google.com/)搜索一下敏感词汇，成功了吧？

注意：

不到万不得以，不要用代理上网，否则不只是流量问题，如果GFW把你的空间IP给封了，你就等着哭吧。


