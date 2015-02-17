---
author: chengbo
comments: true
date: 2012-04-20 06:15:59+00:00
layout: post
title: 使用Gitolite来对Git的repository实现权限控制
categories:
- Linux
tags:
- Git
- Gitolite
- Linux
---

我们项目组打算从svn向git迁移，前几天我搭建了git环境，把代码从svn转移过来，然后所有成员都通过server上的git账号来做pull和push，一切都安置妥当，没有问题。但是后来其它项目组也打算使用这个git server，那么问题来了，之前那种授权的方式肯定是不够的，因为只要能连上server，那么他对这个server上所有的repository都有完全的读写权限，这显然是不可接受的。

所以打算使用Gitolite这个组件来做权限控制，搜索了下，找到的文章貌似都是老版本的，所以有了写这篇文章的想法。

Gitolite其实也是一个git repository，首先在server上安装好后，在client上把server上的repository clone下来，在本地做一些更改，再push回server，server端的hooks会根据push上来的配置来更新权限。

接下来，介绍下安装和配置步骤

### 准备工作

如果你之前是用git账号来做权限控制的话，记得把`/etc/passwd`里git用户的shell换回`/bin/bash`，然后把`~git/.ssh/authorized_key`里不再需要的key移除。

用`ssh-kengen`生成一对key，比如your-name和your-name.pub（下文均以此为例）

拷贝私钥到本用户的.ssh文件夹中
    
    mv your-name ~/.ssh/

拷贝公钥到git server上
    
    scp you-name.pub git@your.server.name.or.ip.address:~


为了以后方便，这里可以做一个server别名，指定连接所需的用户名，server的地址、端口以及私钥

    vim ~/.ssh/config

输入以下内容
    
    host githost
    user your-name
    hostname your.server.name.or.ip.address
    port 22
    identityfile ~/.ssh/your-name

### 安装Gitolite

登录git server
    
    ssh git@your.server.name.or.ip.address

下载最新的Gitolite
    
    git clone git://github.com/sitaramc/gitolite

安装，这里说明下，安装方式有3种，区别在与指定生成`gitolite`可执行文件的路径，这里采用Gitolite作者推荐的第二种，也就是把文件生成到`$HOME/bin`中，这样可以在接下来的bash中直接执行`gitolite`命令而不用指定路径(如果你的`~/bin`目录不存在记得先`mkdir ~/bin`)
    
    gitolite/install -ln

设置，由于是第一次运行这个命令，所以这里指定的key是拥有Gitolite管理员权限的
    
    gitolite setup -pk your-name.pub

此命令会在你的`~/repositories/`目录生成两个repository：gitolite-admin.git和testing.git

### 配置权限

退到你的workstation上
    
    exit

clone刚才生成的gitolite-admin.git

    git clone githost:gitolite-admin

注意这里用的是刚才准备好的server别名来连接的，其中最重要的区别是使用your-name.pub这个key，并且没有采用绝对路径来指定想要clone的repository，而是直接使用名称，并且这个名称也没有包括.git这个后缀。这一点很重要，因为这是用Gitolite的机制来clone，如果你跳过它直接使用git来，那么它的一些功能就无法实现了。以后clone, push其它需要受Gitolite权限控制的repository都必须这样做。

clone完后会有个新的目录`gitolite-admin`，里面有两个文件夹`conf`和`keydir`，第一个目录中包含的是配置文件，里面就是记录权限配置的地方，第二个目录中则包含所有用户的pub key。

现在我们打开配置文件，按照我们的权限配置需要进行设置
    
    vim gitolite-admin/conf/gitolite.conf

我期望的配置如下，你也可以根据你的需要做更改
    
    @repos_a @proj1 @proj2
    @repos_b @proj3 @proj4 @proj5
    
    @team_a @user1 @user2
    @team_b @user3 @user4
    
    repo gitolite-admin
    RW+ = your-name
    
    repo @repos_a
    RW+ = @team_a
    R = @all
    
    repo @repos_b
    RW+ = @team_b

这个配置很简单，首先定义了两个repository group，再又定义了两个user group，group的好处就是以后添加repository和user的时候，不需要再单独配置，只需加入到对应的group中即可。
	
  * 添加全新的repository，在上面提到的gitolite.conf文件中配置好对应的名称和权限，再push到server即可，server会自动帮你创建一个empty的bare repository。
  * 如果你已经有一个repository，想把它加进来的话，那就把它拷贝到git server上的`~/repositories`文件夹里，记得文件夹名要以.git结尾，并且这个repository一定要是bare的，（你可以通过拷贝repository里的.git文件夹，然后运行`git config --bool core.bare true`，也可以运行`git clone --bare your-repository`来得到bare repository）。这种方式还有一个额外的操作就是在server上运行一次`gitolite setup`。
  * 移除repository，在配置文件中移除对应的repo，然后push，接着再删除server上对应的文件夹即可。
  * 添加user，把pub key拷贝到`keydir`文件夹里
  * 删除user，一样，移除`keydir`里对应的pub key

注意，上面说的操作，都必须在clone的gitolite-admin里做更改，然后push，千万别在server上自己来，那样是没用的，因为这些权限配置、repository管理都有一些额外的操作，gitolite-admin会帮你搞定一切。

把你的更改push回server上，试试clone，pull，push，看看权限是否正确。比如
    
    git clone githost:proj3

更多的内容，可以参考[官方文档](http://sitaramc.github.com/gitolite/master-toc.html)

本文由Roy最初发表于：[http://blog.chengbo.net/2012/04/20/use-gitolite-to-manage-git-repositories.html](http://blog.chengbo.net/2012/04/20/use-gitolite-to-manage-git-repositories.html)，你可以在保持文章完整和保留本声明的情况下转帖、分发和印刷等。
