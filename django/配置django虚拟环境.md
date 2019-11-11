1. 配置虚拟环境的方法

   方法1：PyCharm中配置虚拟坏境

   方法2：PyCharm终端或者cmd中创建虚拟环境
   ​	进入到要存放环境的文件夹中 ： python -m venv <环境名称>

   方法3：使用virtualenv模块创建：virtualenv <环境名称>

   - 进入到一个现有的虚拟环境下先下载virtulaenv模块

     ```
     (myenv) E:\workspace\myenv\Scripts>pip install virtualenvpip install virtualenv
     ```

   - 查看是否下载成功virtualenv模块

     ```
     (myenv) E:\workspace\myenv\Scripts>virtualenv
     Running virtualenv with interpreter E:\python\python.exe
     You must provide a DEST_DIR
     Usage: virtualenv.py [OPTIONS] DEST_DIR
     
     Options:
       --version             show program's version number and exit
       -h, --help            show this help message and exit
       -v, --verbose         Increase verbosity.
       -q, --quiet           Decrease verbosity.
       -p PYTHON_EXE, --python=PYTHON_EXE
                             The Python interpreter to use, e.g.,
                             --python=python3.5 will use the python3.5 interpreter
                             to create the new environment.  The default is the
                             interpreter that virtualenv was installed with
                             (E:\python\python.exe)
       --clear               Clear out the non-root install and start from scratch.
       --no-site-packages    DEPRECATED. Retained only for backward compatibility.
                             Not having access to global site-packages is now the
                             default behavior.
       --system-site-packages
                             Give the virtual environment access to the global
     ```

   - 使用virtualenv创建新的虚拟环境，注意必须在virtuakenv所在的目录下才能使用virtualenv模块，或者配置环境变量后可以全局使用

     ```
     E:\workspace> virtualenv <自己的环境名称>
     或者：
     E:\workspace> virtualenv -p 指定python版本 --no-site-packages <环境名称>
     ```

   方法4：使用docker

2. 使用虚拟环境

- windows

  - 激活环境：进入到Scripts文件夹中执行activate

    ```
    E:\workspace\env\firstdjango\Scripts>activate
    ```

  - 退出环境：deactivate

    ```
  (firstdjango) E:\workspace\env\firstdjango>deactivate
    E:\workspace\env\firstdjango>
    ```
  

3. 项目

- 安装django：pip install django==2.0.7
- 项目创建：django-admin startproject  <项目名称>
  - `__init__.py`：配置pymysql
  - urls.py：定义路由与视图函数的关联关系
  - settings.py：配置数据库，配置TEMPLATES等
- 应用创建：python manage.py startapp <应用名称>
  - views.py：定义视图函数
  - models.py：定义模型
- 启动方式
  - python manage.py runserver (默认为127.0.0.1:8000)
  - python manage.py runserver port (设置为127.0.0.1:port)
  - python manege.py runserver IP:PORT 自定义启动的IP和PORT

4. 数据库

   1. Django的模型操作 —— ORM框架（对象关系映射）

      - 正向工程：先创建模型，再通过模型的迁移自动生成表（项目规模小，没有专业的DBA）
   
        ~ python manage.py makemigrations <应用名称>
   
        ~ python manage.py  migrate
   
      - 反向工程：先有数据库的表，再通过检查数据库自动反向生成模型（项目规模大，有专业的DBA）
   
        ~ python manage.py inspectdb <应用名称>/models.py
   
   - 在settings.py文件中定义DATABASES的内容
   
   - 在工程目录的`__init__.py文件中配置`
   
     ```
     import pymysql
     pymysql.install_as_MySQLdb()
     ```
   
   - django默认提供数据库表的生成：python manage.py migrate
   
   - 创建一个MVC应用：python manage.py startapp <应用名称>
   
   - 在auth_user表中加入数据（创建超级用户）：python manage.py createsuperuser
   
     