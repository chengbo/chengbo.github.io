---
author: chengbo
comments: true
date: 2012-03-09 07:15:49+00:00
layout: post
title: 当ListView有Header时，onItemClick里的position不正确
categories:
- Android
tags:
- Android
---

今天在做项目的时候，遇到一个问题，记录下来。

当给[ListView][1]加了一个HeaderView后（代码如下），我们发现，[onItemClick][2]方法里的`position`参数的值不是我们所期望的，比如点击ListView的第一行，我们期望的`position`是0，可是实际上却是1，也就是说，它是从Header而不是从第一行开始计数的。

    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState);
    
    	setContentView(R.layout.home);
    
    	mAdapter = new MyAdapter(this);
    
    	mListView = (ListView) findViewById(R.id.list);
    	mListView.addHeaderView(getLayoutInflater().inflate(R.layout.list_header));
    	mListView.setAdapter(mAdapter);
    	mListView.setOnClickListener(this);
    }
    
    @Override
    public void onItemClick(AdapterView<?> parent, View v, int position, long id) {
    	doSomething(mAdapter.getItem(position));
    }


Google了下，发现有个老外issue过一个[bug](http://code.google.com/p/android/issues/detail?id=4197)，和我遇到的问题一样，不过这个bug被RomainGuy reject掉了，理由是，你用错了，请用[getAdapter][3]。这回答的太简洁了，完全没法理解，所以只好又去仔细研究ListView的代码，终于领会他的意思了。把其中[addHeaderView][4]和[setAdapter][5]方法贴下来

    
    /**
     * Add a fixed view to appear at the top of the list. If addHeaderView is
     * called more than once, the views will appear in the order they were
     * added. Views added using this call can take focus if they want.
     * <p>
     * NOTE: Call this before calling setAdapter. This is so ListView can wrap
     * the supplied cursor with one that that will also account for header
     * views.
     *
     * @param v The view to add.
     * @param data Data to associate with this view
     * @param isSelectable whether the item is selectable
     */
    public void addHeaderView(View v, Object data, boolean isSelectable) {
        if (mAdapter != null) {
            throw new IllegalStateException(
                    "Cannot add header view to list -- setAdapter has already been called.");
        }
    
        FixedViewInfo info = new FixedViewInfo();
        info.view = v;
        info.data = data;
        info.isSelectable = isSelectable;
        mHeaderViewInfos.add(info);
    }
    
    /**
     * Sets the data behind this ListView.
     *
     * The adapter passed to this method may be wrapped by a {@link WrapperListAdapter},
     * depending on the ListView features currently in use. For instance, adding
     * headers and/or footers will cause the adapter to be wrapped.
     *
     * @param adapter The ListAdapter which is responsible for maintaining the
     *        data backing this list and for producing a view to represent an
     *        item in that data set.
     *
     * @see #getAdapter()
     */
    @Override
    public void setAdapter(ListAdapter adapter) {
        if (null != mAdapter) {
            mAdapter.unregisterDataSetObserver(mDataSetObserver);
        }
    
        resetList();
        mRecycler.clear();
    
        if (mHeaderViewInfos.size() > 0|| mFooterViewInfos.size() > 0) {
            mAdapter = new HeaderViewListAdapter(mHeaderViewInfos, mFooterViewInfos, adapter);
        } else {
            mAdapter = adapter;
        }
    
        //其它的一些代码这里省略之...
    }


从代码和注释里都可以很清楚的得知，`addHeaderView`一定要在`setAdapter`之前调用，如果不这样做，`addHeaderView`会抛出一个异常。Android为什么要这样？这是因为，在`setAdapter`的时候，会针对我遇到的这种情况（也就是添加Header后`position`不正确的这种情况）做些特殊的处理。`setAdapter`在内部判断了当前ListView是否有Header或者Footer，如果没有，就直接使用参数传进来的adapter；如果有，则用一个decorated的`HeaderViewListAdapter`来替换参数。这个`HeaderViewListAdapter`的使命，就是排除Header和Footer，让`position`（当然也包括[getItem][6], [getItemId][7]）等方法的`position`参数）正确返回。

分析到这里，解决方案就出来了：在`onItemClick`不要直接使用我们声明的adapter，而是用ListView里的那个decorated adapter。获取它的方法就是调用`parent.getAdapter()`。当然，如果ListView没有Header和Footer，直接使用声明的adapter也没有问题，不过为了避免出错，还是统一使用decorated adapter比较好。

把onItemClick改成下面这样，就可以了

    
    @Override
    public void onItemClick(AdapterView<?> parent, View v, int position, long id) {
    	doSomething(parent.getAdapter().getItem(position));
    }


本文由Roy最初发表于：[http://blog.chengbo.net/2012/03/09/onitemclick-return-wrong-position-when-listview-has-headerview.html](http://blog.chengbo.net/2012/03/09/onitemclick-return-wrong-position-when-listview-has-headerview.html)，你可以在保持文章完整和保留本声明的情况下转帖、分发和印刷等。

[1]: http://developer.android.com/reference/android/widget/ListView.html       "ListView"
[2]: http://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener.html#onItemClick(android.widget.AdapterView<?>,%20android.view.View,%20int,%20long)       "onItemClick"
[3]: http://developer.android.com/reference/android/widget/ListView.html#getAdapter()       "getAdapter"
[4]: http://developer.android.com/reference/android/widget/ListView.html#addHeaderView(android.view.View)       "addHeaderView"
[5]: http://developer.android.com/reference/android/widget/ListView.html#setAdapter(android.widget.ListAdapter)       "setAdapter"
[6]: http://developer.android.com/reference/android/widget/Adapter.html#getItem(int)      "getItem"
[7]: http://developer.android.com/reference/android/widget/Adapter.html#getItemId(int)       "getItemId"