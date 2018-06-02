# blogVisitors

## getHtml.py

> 2018年06月02日22:08:35
>
> Request Url : 'http://s04.flagcounter.com/more7/XTPq/'
>
> Page numbers : 18
>
> Data: Date, visitors, flagViews
>
> 使用`正则表达式`获取对于日期下的博客访问量 以及 统计信息页面查看量.
>
> 获取的数据保存至文件中，命名规则为blog_year&month&day 例如 `blog_20180601`
>

## drawPic.py

> 2018年06月02日22:11:57
>
> 读取data文件夹下的数据或者读取之前保存的pickle二进制文件，得到date, visitors, flagViews.
>
> `draw_pic`绘制结果，包括visitors折线图，flagViews折线图，flagViews-visitors = diff折线图.
>
> 当前折线图横坐标为时间，开始日期为2018年12月17日，结束日期为当前时间.
>
> 折线图按照每100天进行分颜色绘制，后续考虑更多数据统计信息的添加.

