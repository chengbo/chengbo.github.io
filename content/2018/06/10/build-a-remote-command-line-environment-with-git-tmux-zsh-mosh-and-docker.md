---
author: chengbo
comments: true
date: 2018-06-10 16:12:22-07:00
layout: post
title: Create a remote command line environment with git vim tmux zsh mosh and docker
tags:
- Git
- Vim
- Tmux
- Zsh
- Mosh
- Docker
---

Sometimes I'm halfway through writing code at the company and it's time to get out of work, the work isn't done and isn't pushed to the remote repository, so it's not convenient if I want to proceed at home. Or at home, I'm writing code on a PC, my kids want to play PC games for a while, it is also troublesome to switch to the Mac to continue my work.

So I came up with an idea to set up a remote working environment on my VPS. No matter where or even with only iPad, as long as there's internet and a SSH client, I can connect to it, proceed to code in the same environment as I left it.

This article is to share my remote text only command line environment created by git tmux zsh mosh and docker, as shown below.

![vim tmux](/static/images/2018/06/vim-tmux.jpg)

## Docker

First of all, this environment should have a great portability. It takes a certain number of steps and time to set up this environment, so if the VPS provider is changed, I don't want to do these repetitive work again. So I created this environment in docker, the steps are written in [Dockerfile](https://github.com/chengbo/remote-dev/blob/master/Dockerfile), you can see more detail information if you are interested.

## Git

Git is of course a must, not only the day-to-day development require it, but some of the tools in this environment need it to get the code to compile/install as well.

## Zsh & Oh My ZSH

Zsh is undoubtedly more advanced than Bash, with [Oh My ZSH](http://ohmyz.sh) is even more powerful，it gives your better auto completion, navigation, git support and themes.

## Vim

The most powerful text editor in the planet. I also have some plugins installed, makes it act like an IDE.

## Tmux

Tmux is a screen multiplexer, similar to [GNU Screen](https://www.gnu.org/software/screen/). It gives you "tabs" for non-Vim related stuff like shell, git, unit test and so on. It also keep sessions when you switching between multiple projects.

## Tig

This is a fantastic text-mode interface for git, it works just like [SourceTree](https://www.sourcetreeapp.com/) on Mac. You can view logs, diff status, and anything you can think of.

It looks like below.

![vim tmux](/static/images/2018/06/tig.jpg)

## Mosh

[Mosh](https://mosh.org) is similar to SSH, and works better on poor network conditions and mobile roaming connections. It has lower latency and keeps connected between different networks. You are gonna love it.

**Ubuntu server**  
Because the true color support is not in latest version 1.3.2, so you have to use below dev version to make Tmux and Vim theme works correctly.
```
sudo add-apt-repository ppa:keithw/mosh-dev
sudo apt update
sudo apt install mosh
```

**Windows & Chromebook Client**  
Install this [Chrome Extension](https://chrome.google.com/webstore/detail/mosh/ooiklbnjmhbcgemelgfhaeaocllobloj).

**Mac client**  
Because the true color support is not in latest version 1.3.2, so you have to use HEAD version to make Tmux and Vim theme work correctly.
```
brew install --HEAD mosh
```

**iPad client**  
Install this [App](https://itunes.apple.com/app/id1156707581).
## Conclusion

All above tools can work without a mouse, more productivity! Some of these tools settings highly depend on my [dotfiles](https://github.com/chengbo/dotfiles).

Although it is built for Python development, you can also change the configuration according to your needs and build your own remote command line environment.
