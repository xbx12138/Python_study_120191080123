1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
    提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)

2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；

3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
        Tom   admin   XXXXX
        Jack  root    XXXXX   

4  (继续上面的练习) 模拟用户登录:
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);

5  通过Python来模拟实现一个txt文件的拷贝过程;
    
6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小

效果如：
![](https://i.loli.net/2021/04/18/G6m4M5YvK3HIVRy.png)
7 使用python代码统计一个文件夹中所有文件的总大小

8 京东二面笔试题
1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

9 从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）