1. 进入到pycharm的开始界面
2. 依次点击configure -> Setting -> Version Control -> Git -> test ，如果显示git的版本信息则表示已经配置了git，否则在Path to Git executable下选择你所安装的Git目录下找到git.exe
3. 点击Check out from Version Control -> Git；然后把自己服务器端的http或者ssh的地址复制到URL。
4. 进入到项目中后还要配置环境: File -> Settings -> Project intepreter 新建自己的环境,当项目中出现venv这个包和Terminal下出现vnev表示配置成功。
5. 但是py文件中可能存在一些包自己的python库中没有需要下载后才能运行程序，在Terminal(终端)下执行以下的命令即可解决。
- 查看当前以及有的包：pip freeze
- 在项目中存在一个名字叫requirements.txt的文件（公认的ID），里面存放的就是当前项目所需要的所有包的名字。使用下面的命令下载所有的包
  - 生成项目依赖项清单：pip freeze > requirements.txt
  - 根据依赖项清单安装三方库：pip install -r requirements.txt -i https://pypi.doubanio.com/simple






























下载项目需要的配置环境：
pip install -r requirements.txt -i https://pypi.doubanio.com.simple 