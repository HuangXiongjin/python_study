1. 前端vue打包
vue打包命令：
  
    ```
  npm run build
    ```
  
2. 后端配置
   1. 创建自己的文件夹存放相应的项目内容
      ```
      [root@izbp15547sumlsn3rij2lmz /]# cd /home
      [root@izbp15547sumlsn3rij2lmz home]# mk code conf env logs 
      [root@izbp15547sumlsn3rij2lmz home]# ls
      code  conf  env  logs
      [root@izbp15547sumlsn3rij2lmz home]# 
      ```
      code：存放项目的代码
      
      ​	dist文件夹可直接从前端项目中复制到code文件夹下面
      ```
      [root@izbp15547sumlsn3rij2lmz code]# ls
      axf  dist
      [root@izbp15547sumlsn3rij2lmz code]# 
      ```

      conf：存放项目的nginx配置文件，uwsgi.ini配置文件
   
      ```
      [root@izbp15547sumlsn3rij2lmz conf]# ls
      axfnginx.conf  axfnginx.conf1  axfuwsgi.ini
      [root@izbp15547sumlsn3rij2lmz conf]
      ```
   
      env：存放项目的虚拟环境
   
      ```
      [root@izbp15547sumlsn3rij2lmz ~]# cd /home
      [root@izbp15547sumlsn3rij2lmz home]# cd env
      [root@izbp15547sumlsn3rij2lmz env]# python3 -m venv axfenv
      [root@izbp15547sumlsn3rij2lmz env]# ls
      axfenv
      [root@izbp15547sumlsn3rij2lmz env]# cd axfenv
      [root@izbp15547sumlsn3rij2lmz axfenv]# ls
      bin  include  lib  lib64  pyvenv.cfg
      [root@izbp15547sumlsn3rij2lmz axfenv]# cd bin
      [root@izbp15547sumlsn3rij2lmz bin]# ls
      activate      activate.fish  django-admin.py  easy_install-3.7  pip3    __pycache__  python3
      activate.csh  django-admin   easy_install     pip               pip3.7  python       uwsgi
      [root@izbp15547sumlsn3rij2lmz bin]# source activate
      (axfenv) [root@izbp15547sumlsn3rij2lmz bin]#
      
   # 虚拟环境成功以后，安装项目所需要的包，如果进入了虚拟环境中了可执行以下命令安装
      (axfenv) [root@izbp15547sumlsn3rij2lmz bin]# pip3 install -r requirement.txt
   # 如果不在虚拟环境下可执行以下命令安装
      [root@izbp15547sumlsn3rij2lmz ~]# /home/env/axfenv/bin/pip3 install -r requirement.txt
      ```
      
      logs：存放nginx启动成功和失败的文件；以及uwsgi运行的日志文件
      
```
      [root@izbp15547sumlsn3rij2lmz logs]# ls
      uwsgi.log
      [root@izbp15547sumlsn3rij2lmz logs]# 
      ```
      
   2. 编写自己的项目文件(axf项目为例)
   
      1. 首先配置好自己的的axfnginx.conf文件
      
      ```
      [root@izbp15547sumlsn3rij2lmz ~]# vim /home/conf/axfnginx.conf
        第一种配置方案
        1 upstream backend {
        2     server 118.31.103.87:8000;
        3     server 118.31.103.87:8001;
        4     server 118.31.103.87:8002;
        5 }
        6 
        7 server{
        8     listen 80;
        9     server_name 118.31.103.87;
       10     root /home/code/dist;
       11     index index.html;
       12 
       13     location /api {
       14         proxy_pass http://backend;
       15 
       16     }
       17 }
      ~ 
        正式环境中部署为nginx+uwsgi来部署django项目（推荐使用）
        1 server {
        2     listen 80;
        3     server_name 118.31.103.87;
        4     root /home/code/dist;
        5     index index.html;
        6 
        7     location /api {
        8         include uwsgi_params;
        9         uwsgi_pass 127.0.0.1:8080;
       10     }
       11 
       12 }
       13 
      
      
      ```
      2. 修改总的nginx的配置文件，让总的nginx中的配置文件包含我们自定义项目的配置文件（添加37行的内容）
      
      ```
       33     # Load modular configuration files from the /etc/nginx/conf.d directory.
       34     # See http://nginx.org/en/docs/ngx_core_module.html#include
       35     # for more information.
       36     include /etc/nginx/conf.d/*.conf;
       37     include /home/conf/*.conf;
       38 
       39     server {
       40         listen       80 default_server;
       41         listen       [::]:80 default_server;
       42         server_name  _;
       43         root         /usr/share/nginx/html;
       44 
       45         # Load configuration files for the default server block.
       46         include /etc/nginx/default.d/*.conf;
      ```
      
      3. 整个项目的配置全部完成以后需要重启nginx
      
         nginx的运行命令：
      
         ```
         systemctl start/stop/enable/disable nginx 启动/关闭/设置开机启动/禁止开机启动
         systemctl restart nginx 重启
         systemctl status nginx 查看状态
         
         ```
      
      4. 配置axfuwsgi.ini
      
         1. 安装uwsgi
      
            ```
            [root@izbp15547sumlsn3rij2lmz ~]# /home/env/axfenv/bin/pip3 install uwsgi
            ```
      
         2. 配置axfuwsgi.ini文件
      
            ```
            [uwsgi]
            projectname=axf
            base=/home/code
            # 守护进程
            master=true
            
            # 虚拟环境
            pythonhome = /home/env/axfenv
            
            # 项目地址 chdir = %(base)/%(projectname)
            chdir=/home/code/axf
            
            # 指定python版本
            pythonpath=/home/env/axfenv/bin/python3
            
            # 指定uwsgi文件module = %(projectname).wsgi
            module=axf.wsgi
            
            # 和nginx通信地址:端口
            socket=127.0.0.1:8080
            
            # 日志文件地址
            logto = /home/logs/uwsgi.log
            ```
      
         3. 运行项目
      
            ```
            [root@izbp15547sumlsn3rij2lmz ~]# /home/env/axfenv/bin/python3 uwsgi --ini axfuwsgi.ini
            ```
      
            