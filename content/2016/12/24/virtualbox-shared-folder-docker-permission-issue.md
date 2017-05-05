---
author: chengbo
comments: true
date: 2016-12-24 23:14:00+00:00
layout: post
title: 虚拟机共享目录引起的权限问题
tags:
- Programming
---

我在写代码的时候，不喜欢在mac上装相关依赖的组件，因为不同项目之间的依赖冲突有点麻烦，而且久而久之会污染我mac环境。所以我有一个VirtualBox，里面弄一个ubuntu的虚拟机，ssh进去安装，这个虚拟机可以随时抛弃，再重新建立。

但同时我又非常喜欢mac的GUI，所以我把开发目录在Host（mac）和Guest（ubuntu）之间建立共享（shared folder）。这样一来，我既可以拥有和生产环境一模一样的开发环境，也可以享受mac极好的GUI体验。

这样的开发方案一直很完美，直到有一天，发现了一个奇怪的问题……

我有一个docker的container运行在ubuntu里，这个container需要一个自定义的conf文件，由volume挂载进去。container启动后会自动往conf文件里添加一些内容。这个conf文件放在shared folder上，再volume进container。

当运行这个container的时候，我发现container在conf要写的内容死活写不进去。可是相同的代码，在mac上直接运行docker，则一切正常。

我花了好几个小时才找到原因：

* ubuntu的conf文件的权限是770
* 这个文件是`root:vboxsf`
* container运行的帐号没权限写vboxsf的文件

那么解决方案就是，把文件改成`yourname:docker`

可是直接用chown，改不了，所以换另外一个办法，不用VirtualBox的自动挂载，自己用命令手动挂

首先找出你的帐号的uid

```bash
$ id -u $whoami
1000
```

再找docker的gid

```bash
$ cut -d: -f3 < <(getent group docker)
999
```

挂上去，这里`dev`是我的挂载名字

```bash
sudo mount -t vboxsf -o remount,gid=999,uid=1000,rw dev /media/sf_dev
999
```

这样重新启动ubuntu后，文件变成`yourname:docker`了，再运行container就没问题了。可是这种挂载方式重启ubuntu会丢，想要一直保持的话，用下面的方法

把下面的内容加到`/etc/modules`里

```
vboxsf
```

把下面的内容加到`/etc/fstab`里

```
dev /media/sf_dev vboxsf gid=999,uid=1000,rw 0 0
```

That is it.
