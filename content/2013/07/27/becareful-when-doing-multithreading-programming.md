---
author: chengbo
comments: true
date: 2013-07-27 16:00:00+00:00
layout: post
title: 多线程写代码的时候要注意安全
categories:
- Programming
tags:
- Programming
- DotNet
- Multithreading
---

今天在做项目时候，发现获取当前登录user信息的rest service，偶尔会报错

    An item with the same key has already been added.

只是偶尔报错，大部分时间是正常的，很奇怪。查了半天才查出原因，记录下来：

打开service代码，如下

```csharp
public static class UserInfoProcess
{
  private static DataAccessDataContext db = new DataAccessDataContext();

  public static EmployeeInfo GetEmployeeInfoById(string employeeId)
  {
    return db.EmployeeInfos.SingleOrDefault(c => c.EmployeeId == employeeId);
  }
}
```

注意，这里的`DataContext`是static的，这里有个问题等会儿说。

查一下MSDN：

[http://msdn.microsoft.com/en-us/library/system.data.linq.datacontext.aspx](http://msdn.microsoft.com/en-us/library/system.data.linq.datacontext.aspx)

Thread Safety
________________________________________

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

MSDN说，`DataContext`只保证它static member的线程安全，而instance member则不保证。

那么什么叫线程安全呢，我觉得简单的说，就是多个线程同时访问一个object或者method的时候，内部的值要处理正确。

上面的service代码，调用了`DataContext`的`EmployeeInfos`属性，这个属性是instance member，所以它的线程安全得不到保证。

线程不安全，是怎么体现的呢？我用reflector里反编译了`EmployeeInfos`属性，下面摘一点重要的出来

```csharp
private ITable GetTable(MetaTable metaTable)
{
  ITable table;
  if (!this.tables.TryGetValue(metaTable, out table))
  {
    ValidateTable(metaTable);
    table = (ITable) Activator.CreateInstance(typeof(Table<>).MakeGenericType(new Type[] { metaTable.RowType.Type }), BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Instance, null, new object[] { this, metaTable }, null);
    this.tables.Add(metaTable, table);
  }
  return table;
}
```

这个方法中，先看看tables这个dictionary里有没有对应的key，没有就反射create一个，再把它加到dictionary里。

如果只有一个线程，那么这里永远不会有问题，但是，rest service是一个多线程的环境。每一个request进来，都是一个线程，他们共享的是同一个`DataContext`（因为上面的service代码中，`DataContext`定义成static了），两个线程有一定的几率同时add一个key（这里没有lock，有lock，就可以线程安全了），导致开头说的那个错误。

所以，解决方法找到了：

1. 把这个代码加上lock的机制，但是由于这是.Net Framework的代码，我们改不了，所以只能

2. 这里`DataContext`不定义成static，换成instance的，每个线程访问自己独有的`DataContext`

PS：说句题外话，换成instance后，每个请求都要反射，可见Linq to sql性能不怎么样
