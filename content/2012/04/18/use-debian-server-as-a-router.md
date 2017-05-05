---
author: chengbo
comments: true
date: 2012-04-18 05:30:29+00:00
layout: post
title: 用Debian当路由，来解决BT造成的网络慢的问题
categories:
- Linux
tags:
- ADSL
- Debian
- Linux
- 路由
---

自从[@TimothyYe](http://www.weibo.com/timothyye) 童鞋介绍偶加入HDC后，为了快点完成新人作业，也为了满足我不折腾不舒服斯基的欲望，哥配了一台凌动小PC，Intel ATOM D525NW的主板，集成了CPU和显卡，加上小机箱总共700元。到手后，插上我Thinkpad拆下来的2根1G内存和另外一台闲置N久的台式机160G SATA硬盘，装了个Debian，就可以用了。

装上transmission后，全速挂BT无压力，比那些直接路由或者1、200的NAS给力多了。哥还继续在上面折腾了Git，emule，动态DNS等，远远没有把2G内存榨干，当然这里都说远了，继续回来。

我家使用的是电信ADSL，一个宽带无线路由，手机，notebook，iPad，PC，xbox等（哥真败家。。。），路由拨号连入Internet，然后通过WIFI把其它设备连入LAN，共享外网连接。这个配置在我挂PT之前一直工作正常，可是当我把BT开着，就算上传和下载速度都为0，LAN中的其它设备访问Internet的速度一样很慢，很慢。

分析了下，估计是我那100元的低端无线路由无法支撑如此多的连接会话造成的，简单直接的办法就是升级路由，于是开始上网查高端路由，不查不知道，一查才知道这东西好贵，便宜的怕是不能解决问题，贵的哥又承受不了。纠结了N久，最后发现，何不把我那台Debian来做路由呢？

马上在淘宝买了根20元的USB有线网卡，收到后插入Debian上，这东西不像Windows和MAC可以自动识别出来然后提示你安装驱动，要自己去折腾，而且附送的光盘上也没有Linux的驱动，看来，要找Google了。

### 安装配置USB网卡

在Debian上运行
    
    $ lsusb

Bus 005 Device 002: ID 0fe6:9700 Kontron (Industrial Computer Source / ICS Advent) DM9601 Fast Ethernet Adapter

从上得知，USB网卡是DM9601这个型号的

    $ /sbin/ifconfig

只有lo和eth0，新加的网卡没有识别

以DM9601为关键字，Google，找到了[这里](http://www.davicom.com.tw/page1.aspx?no=209814)，下载解压好linux的驱动后，编译出错，好像是头文件不对，哥不会写驱动啊，只有继续Google，发现DM9601的驱动已经集成在新版的内核里了，但是我试了下，用不了，不知道什么原因。继续Google，又找到了[这里](http://ceyes.blog.51cto.com/2377614/808386)，根据上面的说明，下载了qf9700的驱动，编译，成功，生成文件qf9700.ko。

安装刚才编译好的驱动
    
    # cp qf9700.ko /lib/modules/`uname -r`/kernel/drivers/net/usb
    # cd /lib/modules/`uname -r`/kernel/drivers/net/usb
    # modprobe usbnet
    # insmod qf9700.ko
    # ifconfig eth1 up

配置好驱动后再运行
    
    $ /sbin/ifconfig

多了一个eth1了，到现在新网卡已经可以使用了。

### 安装配置ADSL拨号相关软件

把原先连接无线宽带路由和猫的网线拔掉，接在猫和Debian的USB网卡上
安装拨号软件
    
    # apt-get install pppoe pppoeconf

成功后运行
    
    # pppoeconf

会弹出一个窗口，自动检测连接ADSL的网卡，然后照提示输入你的用户名，密码，其它的可以用默认值。

运行
    
    # pon dsl-provider

就可以拨号了，过后再`ifconfig`一下，会发现多了个ppp0。`poff`命令可以关闭ppp0连接。另外，我发现多次拨号可以有多个ppp，比如ppp1，而且IP还不一样，不知道这样是否可以让带宽double，待测试。

此时Debian可以上网了，但是LAN中的其它设备还不行。

### 设置LAN路由

设置Debian连接LAN的网卡配置
    
    # vim /etc/network/interfaces

> allow-hotplug eth0
iface eth0 inet static
address 192.168.3.3
netmask 255.255.255.0
network 192.168.3.0
broadcast 192.168.3.255
gateway 192.168.3.3

由于所有的无线设备都是有无线宽带路由来DHCP的，所以登录无线宽带路由，把配置改下：

> range 192.168.3.100-192.168.3.200
netmask 255.255.255.0
gateway 192.168.3.3
dns 8.8.8.8 or 4.4.4.4

DNS没有用电信分配给我的，是因为不想看电信强行插入的广告

设置NAT
    
    # echo "1" > /proc/sys/net/ipv4/ip_forward
    # /sbin/iptables -t nat -A POSTROUTING -o ppp0 -s 192.168.3.0/24 -j MASQUERADE

至此LAN中的其它设备也可以上网了，如果还不行的话，检查下你的配置是否正确，然后再看看路由表，把错误的路由改掉。

最后，我家网络的结构如下图

[![home network](/static/images/2012/04/home-network.png)](/static/images/2012/04/home-network.png)

// TODO: 此文还需添加Debian重启后自动配置USB网卡，拨号，NAT的内容

本文由Roy最初发表于：[http://blog.chengbo.net/2012/04/18/use-debian-server-as-a-router.html](http://blog.chengbo.net/2012/04/18/use-debian-server-as-a-router.html)，你可以在保持文章完整和保留本声明的情况下转帖、分发和印刷等。
