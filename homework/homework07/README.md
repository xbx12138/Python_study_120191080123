关于爬虫的相关知识，大家参考我们后续的课程内容
文档：13 网络爬虫
链接：http://note.youdao.com/noteshare?id=a15adcaebaf739f4ebc69f4c574327ee

1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有1000行，注意控制每次读取的行数；

2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库

3  给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
     这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：
![](https://i.loli.net/2021/05/22/G68IYHgFb9sy2vA.png)
  要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
  Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
注意：
获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示
>>> from urllib.parse import quote
>>> quote('2019-04-13 NEWSworthy Clips.mp3')
'2019-04-13%20NEWSworthy%20Clips.mp3'


4 爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
    文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：
![](https://i.loli.net/2021/05/22/jlGIyUicnbk7BCX.png)
  参考文档：https://blog.csdn.net/weixin_43687366/article/details/88877996
   大家看完这篇文档后，再开始动手做这道题；
