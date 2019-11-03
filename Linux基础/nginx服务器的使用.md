```python
Web服务器 --- 前面的页面放到服务器上 --> http
流行的三个服务器 --- apache/nginx/iis
下面是nginx服务器的安装及使用
```
1. 在linux系统下安装nginx服务器

- yum search nginx：搜索软件包
- yum info nginx：显示安装包信息 
- yum -y install nginx：安装软件包
  - yum  -y remove nginx：如果想要删除可以使用改命令移除软件包。
- nginx --version：查看是否安装成功，如果显示版本信息表示安装成功。

2. 安装好以后在浏览器的url输入自己服务器的公网IP即可进入到nginx的主页面(index.html)，可以自己用vim index.html 去修改网页内容或者用其他的网页去替换index.html。
3. 可以通过git 将自己windows系统下自己的html工程先push到自己的远程服务器中，然后再通过git将文件clone 到nginx/html中，那么在nginx服务器上就可以显示clone的windows上的html文件：cd /usr/share/html。