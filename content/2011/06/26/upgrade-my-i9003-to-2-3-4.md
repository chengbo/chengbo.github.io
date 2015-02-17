---
author: chengbo
comments: true
date: 2011-06-26 14:22:27+00:00
layout: post
title: 升级我的I9003到2.3.4
categories:
- Android
tags:
- Android
---

![](http://static.chengbo.net/images/2011/06/samsung_logo.png)

忍不住手痒，把我的i9003升级到了Gingerbread（Android 2.3.4），在这里把我的升级过程写下来，希望对大家有点帮助。
	
  1. 到[这里](http://forum.xda-developers.com/showthread.php?t=1004647)下载最新的2.3.4的firmware，压缩包的解压密码是samfirmware.com。
  2. 运行Odin3_v1.83.exe。
  3. 选中Re-Partition，Auto Reboot和F. Reset Time三个复选框。
  4. 点击PIT然后选择latona_20110114.pit文件。
  5. 手机关机，然后依次按音量向下键（按住不放），Home（按住不放），电源（按住不放），过几秒手机会显示一个绿色的机器人在挖东西，这就是传说中的挖煤模式，学名download mode。
  6. 用数据线连接手机和电脑，如果需要装驱动请耐心等待驱动安装完毕。然后odin会识别手机的COM，显示在界面上，我的是COM9。
  7. 点击Start按钮。
  8. 完毕后点击Reset按钮，这时程序会自动取消Re-Partition复选框。
  9. 点击BOOTLOADER按钮选择APBOOT_I9003XXKP7_CL280937_REV08_eng_mid_ship.tar；点击PDA按钮选择CODE_I9003XXKP7_CL280937_REV08_eng_mid_ship.tar.md5；点击PHONE按钮选择MODEM_I9003XXKP7_REV_00_CL1021949.tar.md5；点击CSC选择GT-I9003-CSC-MULTI-OXAKP7.tar.md5。
  10. 扣掉电池，按照第5步的方法再次进入挖煤模式。
  11. 点击Start按钮，然后不要动，直到看到绿色的PASS。
  12. 启动手机，此时就可以正常使用了，但是相机还用不了，黑屏，解决方法是按照上面的步骤再刷一次，就可以了。

升级后的一些感受：
	
  * 虽说不是稳定版本，但我觉得还是挺稳定的。
  * 界面有所变化，但是区别不大。
  * ROM很干净，没有太多预装的程序。
  * Local setting里没有中国，但是并不是说不支持访问中文网页，安装中文软件，以及发送接收中文短信，只是说手机的界面是英文的，并且某些显示的风格也是按照英文的文化来的，比如说号码的分段方式。
  * VPN依然不能使用，哎。

2011/7/3 Update:
I9003XXKP7貌似和微信有点冲突，经常在待机情况下无法唤醒机器，只有拔电池重新开机。目前我已刷至最新的I9003XXKP9，再当一次小白鼠。
2011/8/20 Update:
目前最新版是I9003XXKPH。

经过我的测试，**I9003XXKP9已经可以连接VPN了**，哇哈哈哈哈！
