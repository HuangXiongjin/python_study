1. 数据库(Database)的基本理解理念

   - 数据的集散地(仓库)
   - 数据持久化（把数据从内存转移到能够长久存储数据的存储介质中），长久的保存数据.
   - 数据的持久化，不仅仅是为了保存数据，更重要的是管理这些数据，等将来需要这些数据的时候能够按照需求拿到需要的数据。
   - 大多数的数据库都能够保存数据的一致性、完整性并减少数据的冗余

2. 分类

   - 关系型数据库的特点
     
     ```python
     1.理论基础：关系代数 + 集合论
     2.具体表现形式：用二维表来保存数据；行：记录（record）列：字段（field）- 主键列（primary key）
     3.编程语言：SQL（结构化查询语言） 	
     ```
     
   - 关系库数据库的产品
     
     ```python
     1.Oracle - 银行、电子政务、大型电商企业
     2.MySQL - 中小企业 --> MariaDB
     3.DB2 - IBM的产品
     4.SQLServer - (Microsoft)微软的产品
     5.SQLite / PostagreSQL
     ```
     
   - 非关系数据库:MongoDB / Redis / ElasticSearch

     ```python
     No SQL
     No, SQL
     Not Only SQL
     ```

3. 编程语言：SQL(结构化查询语言)
   - DDL：数据定义语言 —— create / drop / alter
   - DML：数据操纵语言 CRUD(增查改删) —— insert / delete / update / select 
   - DCL：数据控制语言 —— grank (授予权限)/ revoke (召回权限)

4. 安装步骤

  ```python
  1. 下载MySQL源安装包: `wget http://dev.mysql.com/get/mysql57-community-		 	release-el7-8.noarch.rpm`  
  2. 安装MySQL源: `yum localinstall mysql57-community-release-el7-8.noarch.rpm`
  3. 安装MySQL:  `yum install mysql-community-server`  
  4. 设置开启启动MySQL服务: `systemctl enable mysqld`  
  5. 启动/重启MySQL服务：systemctl restart mysqld  
  6. 查看MySQL初始密码：grep 'A temporary password' /var/log/mysqld.log  
  7. 更改MySQL密码：mysqladmin -u root -p'旧密码' password '新密码'  
     这里更改密码出了问题，更改失败，这是因为密码太过简单的原因。有两个接解决方法：
  　　　　方法一：把密码设置复杂点（这是最直接的方法）
  　　　　方法二：关闭mysql密码强度验证(validate_password)
  　　　　　　　　编辑配置文件：`vim /etc/my.cnf`， 增加这么一行validate_password=off
  　　　　　　　　编辑后重启mysql服务：`systemctl restart mysqld`  
  　　　　　　　　  　　　　  
  8. 设置mysql能够远程访问:  
     a. 登录进MySQL:  `mysql -uroot -p密码`  
     b. 增加一个用户给予访问权限: `grant all privileges on *.* to 'root'@'ip地址' identified by '密码' with grant option;`  
     c. 刷新权限：`flush privileges;`  
  ```

5. rpm包管理工具安装MySQL

  ```
  必须按顺序安装下面的包以后即可完成MySQL的安装
    	rpm -ivh mysql-community-common-xxx.rpm
      rpm -ivh mysql-community-libs-xxx.rpm
      rpm -ivh mysql-community-client-xxx.rpm
      rpm -ivh mysql-community-server-xxx.rpm
  删除安装的MySQL
  	rpm -qa | grep mysql | xargs rpm -e
  ```

6. 启动MySQL

   - systemctl start mysqld ：d (daemon 守护进程)
   - systemctl stop mysqld 
   - systemctl restart mysqld
   - systemctl status mysqld ：查看状态
   - systemctl enable mysqld ：开机重启

   ```
   开启mysql
   [root ~]# systemctl start mysqld
   
   查看mysql的状态 journalctl -xe 或者 systemctl status mysqld
   [root ~]# systemctl status mysqld
   
   检查网络端口使用情况，MySQL默认使用3306端口
   [root ~]# netstat -ntlp | grep mysql
   
   查找是否有名为mysqld的进程
   [root ~]# pgrep mysql
   
   第一次生成了随机密码，进去root目录下的log查看初始密码:
   [root ~]# cat /var/log/mysqld.log | grep password
   [root ~]# mysql -u root -p 然后输入初始密码
   
   移除安装的mysql
   [root ~]# rpm -qa | grep mysql | xargs rpm -e
   
   修改密码：mysql> alter user 'root'@'localhost' identified by '123456';
   现在可能连接不上因为密码是弱口令不符合内置要求，解决方法重新设置密码为强口令或者修改内置要求如下：
   mysql> set global validate_password_policy=0;
   mysql> set global validate_password_length=6;
   mysql> alter user 'root'@'localhost' identified by '123456';
   [root ~]# mysql -h [主机IP地址] -u 用户名 -p
   ```

7. 图形化的数据库工具

   ```
   MySQL Workbench - 官方
   SQLyog Community - 海豚 (√)
   Toad for MySQL - 蛤蟆
   Navicat for MySQL - 猫 - 商业 (√)
   苹果：Sequel Pro7.图形化工具连接数据库
   ```

8. 图形化界面连接数据库

   8.1 在服务器上打开防火墙（添加3306端口）

   8.2 在MySQL输入下面两条命令

   - 创建一个远程的root用户，给它所有的权限

   ```
   先创建一个远程用户
   mysql> create user 'root'@'%' identified by '123456';
   Query OK, 0 rows affected (0.00 sec)
   
   给他授权
   mysql> grant all privileges on *.* to 'root'@'%' with grant option;
   Query OK, 0 rows affected (0.00 sec)
   
   刷新权限
   mysql> flush privileges;
   
   召回权限(从哪里召回权限)
   mysql> revoke all privileges on *.* from 'root'@'%'
   ```

   8.3 进入图形化界面

   - 点击 ->连接 -> 常规
   - 连接名自主命名
   - 主机名 / IP位地址：服务器的公网IP
   - 端口号：3306
   - 用户名：root
   - 密码：root密码

