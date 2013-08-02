---
author: chengbo
comments: true
date: 2013-08-02 13:38:00+00:00
layout: post
title: 把blog迁移到jekyll
tags:
- Jekyll
- Wordpress
- Blog
---

[![jekyll](http://jekyllrb.com/img/logo-2x.png)](http://jekyllrb.com/)

自从上次看小舟的blog，说他[抛弃了wordpress](http://xiaozhou.net/bye-wordpress-2013-07-22.html)，我就开始心痒痒了。折腾是我的一大爱好，我用的blog平台，从最开始blogcn，到自建movable type，再到wordpress，现在又到jekyll了。

和wordpress不同的是，jekyll是一个使用ruby开发的静态文件生成程序，理论上它可以用来生成任何类型的网站，更别说blog了。每次内容有更新时，我们就用jekyll按照自定义的格式重新生成一次静态的html，然后再把这些html文件部署到host上，访客就可以看到最新的内容了。

相比于wordpress，jekyll的优势

* 不用数据库，内容是基于文件的
* 页面是预先生成好的静态html，无需动态渲染，因此加载速度快
* 对host要求不高，只需能发布html即可
* 备份方便，因为只是一堆的文件，想怎么备份就怎么备份，打包zip，存git等，悉听尊便

劣势

* 折腾，不适合大众
* 页面内容的展现形式，灵活度大大降低
* 默认主题略显简陋，也没有什么可以拿来就可以用的主题，更别要说美观了
* 发布麻烦，不像wordpress，在后台写完了保存就可以了

本来打算直接host在[github pages](http://pages.github.com/)上的，结果github的jekyll版本是1.0.3，这个版本在分页上有个[重大bug](https://github.com/mojombo/jekyll/issues/1348)，而且[不支持plugins](https://help.github.com/articles/pages-don-t-build-unable-to-run-jekyll#unsafe-plugins)，所以只能部署在自己的vps上了。

花了几天的时间，折腾了不少内容：把文章和图片从wordpress导过来，维持post之前的permalink不变，分页，tag，代码高亮显示等。接下来还有不少可以折腾的空间，比如弄一个git hooks，内容有变化就自动build、发布，写一个responsive的主题，tag cloud，SEO等。很多很多，就怕想不到，这下有意思了。

昨晚，我把域名指向了这个blog，而这，就是我用markdown写的第一篇blog。

再见wordpress，你好jekyll。

最后说一下，这个blog备份在[github](https://github.com/chengbo/chengbo.github.io)上。
