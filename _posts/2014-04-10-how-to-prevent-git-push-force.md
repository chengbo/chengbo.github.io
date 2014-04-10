---
author: chengbo
comments: true
date: 2014-04-10 17:04:08+00:00
layout: post
title: rebase之后如何避免使用git push -f来提交代码的规范流程
tags:
- Git
---

这篇blog的内容是我在segmentfault上的一个回答，转帖过来。

提问者提问的大意是，他们团队成员为了提交历史的干净整洁，所以经常会`git rebase`，但是这样在提交代码的时候，就会频繁的发现冲突，只能使用`git push -f`来强制提交，不知道是否合理。

以下是我的回答：

`git rebase`是对commit history的改写。当你要改写的commit history还没有被提交到远程repo的时候，也就是说，**还没有与他人共享之前**，commit history是你私人所有的，那么想怎么改写都可以。

而一旦被提交到远程后，这时如果再改写history，那么势必和他人的history长的就不一样了。`git push`的时候，git会比较commit history，如果不一致，commit动作会被拒绝，唯一的办法就是带上`-f`参数，强制要求commit，这时git会以committer的history覆写远程repo，从而完成代码的提交。虽然代码提交上去了，但是这样可能会造成别人工作成果的丢失，所以使用`-f`参数要慎重。

**楼主遇到的问题，就是改写了公有的commit history造成的。**要解决这个问题，就要从提交流程上做规范。

举个正确流程的栗子：

假设楼主的team中有两个developer：tom和jerry，他们共同使用一个远程repo，并各自clone到自己的机器上，为了简化描述，这里假设只有一个branch：`master`。

这时tom机器的repo有两个branch
`master`, `origin/master`
而jerry的机器上也是有两个branch
`master`, `origin/master`

均如下图所示

![](http://segmentfault.com/img/bVb0wO)

tom和jerry分别各自开发自己的新feature，不断有新的commit提交到他们各自私有的commit history中，所以他们的master指针不断的向前推移，分别指向不同的commit。而又由于他们都没有`git fetch`和`git push`，所以他们的`origin/master`都维持不变。

jerry的repo如下

![](http://segmentfault.com/img/bVb0wQ)

tom的repo如下，注意`T1`和上图的`J1`，分别是两个不同的commit

![](http://segmentfault.com/img/bVb0wR)

这时Tom首先把他的commit提交的远程repo中，那么他本机`origin/master`指针则会前进，和`master`指针保持一致，如下

![](http://segmentfault.com/img/bVb0wT)

远程repo如下

![](http://segmentfault.com/img/bVb0wS)

现在jerry也想把他的commit提交到远程repo上去，运行`git push`，毫无意外的失败了，所以他`git fetch`了一下，把远程repo，也就是之前tom提交的`T1`给拉到了他本机repo中，如下

![](http://segmentfault.com/img/bVb0wU)

commit history出现了分叉，要想把tom之前提交的内容包含到自己的工作中来，有一个方法就是`git merge`，它会自动生成一个commit，既包含tom的提交，也包含jerry的提交，这样就把两个分叉的commit重新又合并在一起。但是这个自动生成的commit会有两个parent，review代码的时候必须要比较两次，很不方便。

jerry为了保证commit history的线性，决定采用另外一种方法，就是`git rebase`。jerry的提交`J1`这时还没有被提交到远程repo上去，也就是他完全私有的一个commit，所以使用`git rebase`改写`J1`的history完全没有问题，改写之后，如下

![](http://segmentfault.com/img/bVb0wV)

注意`J1`被改写到`T1`后面了，变成了`` J1` ``

`git push`后，本机repo

![](http://segmentfault.com/img/bVb0wW)

而远程repo

![](http://segmentfault.com/img/bVb0wX)

异常的轻松，一条直线，没有`-f`

所以，在不用`-f`的前提下，想维持树的整洁，方法就是：在`git push`之前，先`git fetch`，再`git rebase`。

```
git fetch origin master
git rebase origin/master
git push
```

强烈推荐阅读

* [a successful git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
* [Git-分支-分支的衍合](http://git-scm.com/book/zh/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E8%A1%8D%E5%90%88)

