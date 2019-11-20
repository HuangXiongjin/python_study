### 配置全局pip镜像仓库

#### 方法1

1. 在**用户主目录**下创建名为.pip的文件夹（windows开始-运行输入%APPDATA%打开文件夹，没有的话新建pip目录）

2. 在.pip文件夹下创建一个名为pip.conf的文件（Windows环境名字为pip.ini)

3. 在该文件中添加以下代码：
    
    镜像源：
    
    - 阿里云 http://mirrors.aliyun.com/pypi/simple/
    - 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    - 豆瓣(douban) http://pypi.douban.com/simple/
    - 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
    - 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
    
    ```
    [global]
    index-url=https://pypi.doubanio.com/simple
    ```

#### 方法2

直接输入命令配置全局镜像

```
pip config set global.index-url https://pypi.doubanio.com/simple
```

