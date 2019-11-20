### 下载pymysql包

```
pip install pymysql
```

### settings.py文件配置DATABASE

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'djangodb_01',  			   # 数据库名称
        'USER': 'root',						   # 用户名
        'PASSWORD': '123456',				   # 用户密码
        'HOST': 'localhost',				   # 主机ip
        'PORT': '3306',						   # 端口号
        'TIME_ZONE': 'Asia/Chongqing',		   # 设置时区
        'CHARSET': 'utf8',					   # 指定字符集
    }
}

```

**注意：在设置完时区以后，如果使用pycharm专业版连接数据库的时候出现时区报错，进入到mysql中设置全局时区即可：set global time_zone="+8:00";**

### 配置工程目录中的`__init__.py`文件

```
import pymysql

pymysql.install_as_MySQLdb()
```

### Django模型操作——ORM (对象关系映射)

- 创建一个MTV模型：python manage.py startapp <应用名称>   或者  django-admin startapp <应用名称>

- django默认提供数据表的生成

  - 正向工程：先创建模型，再通过模型的迁移自动生成表（项目规模小，没有专业的DBA）

    ```
    # 生成迁移表
    python manage.py makemigrations <应用名称>
    # 迁移表
    python manage.py migrate
    ```

  - 反向工程：先有数据库的表，再通过检查数据库自动反向生成模型（项目规模大，有专业的DBA）

    ```
    python manage.py inspectdb <应用名称>/models.py
    ```

