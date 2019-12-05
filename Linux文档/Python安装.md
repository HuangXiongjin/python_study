1. CentOS安装文件：

- 包管理工具安装（简单靠谱）
  - yum: yellowdog updater modified
    - yum search <软件包的名字>：查找软件包
    - yum install <软件包的名字>：安装软件包
    - yum upgrade <软件包的名字>:更新软件包
    - yum erase <软件包的名字>：移除软件包
    - yum info <软件包的名字>:查看软件信息
    - yum erase <软件包名字>：卸载软件
  - rpm
    - 安装软件包：rpm -ivh <包名字>.rpm
    - 移除软件包：rpm -e <包名字>
    - 查询软件包：rpm -qa <>

3. 源代码构建安装

   安装Python3.x

- 安装前的依赖项

1. Linux安装Python

- 官方下载Python源代码（https://www.python.org）
  wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
  
- 解压
  - 后缀名为tgz: gunzip <文件名>
  - 后缀名为xz: xz -d <文件名>
  
- 解归档
  
  - 后缀为tar: tar -xvf <归档文件名>
  
- 补充相关依赖项
  
  - yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel libdb4-devel libpcap-devel xz-devel libffi-devel
  
- 安装前的配置
  
  ```
  [root@izbp15547sumlsn3rij2lmz ~]# cd Python-3.7.4
  [root@izbp15547sumlsn3rij2lmz Python-3.7.4]# ./configure --prefix=/usr/local/python37 --enable-optimizations
  ```
  
- 构建和安装
  
  - make && make install
  
- 配置PATH环境变量
  - vim .bash_profile
  - export PATH=$PATH:/usr/local/python37/bin
  
- 重新登录或者使用下面命令激活环境变量
  
  - source .bash_profile

4. 评价Python代码的工具
   - ./configure --prefix=/usr/local/python37 --enable-optimization
   - pip3 install pylint -i wget https://pypi.doubanio.com/simple

