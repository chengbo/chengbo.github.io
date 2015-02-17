---
author: chengbo
comments: true
date: 2006-10-16 05:10:16+00:00
layout: post
title: 从Movable Type到wordpress
---

感觉mt在插件、主题的数量和质量还有对中文的支持上都不如wordpress，所以我把MM的博客从movable type转向了wordpress（和老公保持一致）。:-) 转换步骤：

  1. 登录movable type后台管理页面
  2. 在主界面上选择要转换的BLOG
  3. 在左边的菜单里选“IMPORT/EXPORT”
  4. 在顶部选“Export Entries ”
  5. 点击导出按钮
  6. 保存系统生成的txt文件
  7. 登录wordpress管理页面
  8. 在顶部选择“Import”
  9. 选择Movable type
  10. 定位到刚保存的txt文件，再点击“Import”按钮
  11. 选择导入文章的BLOG作者
  12. OK

现在成功的把BLOG转到了wordpress上，但为了与原来的url保持一致，还需要做一些工作： 在Option->Permalinks里选择合适的Structure。 mt在单词中的空格是用"_"来替换的，而wordpress是"-"，所以还要手工填写Post slug，比如原来是"hello world"，现在就要写在"hello_world"（据说有一个插件可以省略这一步，但我试了一下，会出错）
