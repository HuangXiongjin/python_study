

1. 安装Git

   1. 下载

      wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.23.0.tar.gz

   2. 解压 / 归档

      gunzip git-2.23.0.tar.gz
      tar -xvg git-2.23.0.tar
      cd git-2.23.0

   3. 补充相关依赖项

      yum install -y libcurl-devel

   4. 安装前的配置

      ./configure --prefix=/usr/local

   5. 构建和安装

      make && make install

   6. 查看是否安装成功

      git --vetsison

   

2. 版本控制（软件控制管理）

   1900 --- CVS / VSS ——锁定模式

   2000 --- Subversion(SVN) ——合并模式：中央集权型版本控制系统，必须要有版本控制服务器BtiKeeper

   2005 --- Git ——合并模式 ：分布式版本控制系统

3. Git 操作说明

- 初始化版本仓库

  - git init

- 查看仓库状态

  - git status:

- 将文件添加到缓存区（暂存区）

  - git add <filename> 
  - git add . 

- 将文件从缓存区移除

  - git rm --cache  <filename> 

- 用缓存区恢复工作区

  - git restore --staged <filename>

- 将缓存区的内容提交到仓库

  - git config --global user.name "用户名"
  - git config --global user.email "邮箱"
  - git commit -m "提交日志(原因)"

- 查看提交日志

  - git log
  - git reflog (查看详细日志)
  
- 回退版本
  - git reset --hard HEAD^：恢复到上一个版本
  - git reset --hard <commit的版本代码>：恢复到指定版本

- 分支结构：
  - 查看分支：git branch
  - 创建分支：git branch <分支名>
  - 切换分支：git checkout <分支名>
  - 创建分支并切换：git checkout -b <分支名>
  - 删除分支：git branch -d <分支名>
  - 合并分支：git merge <分支名> ——将分支的内容与master分支合并 

- 添加远端仓库到服务器

  - git remote add origin <远端仓库的url>
  - 例如：git remote add origin https://gitee.com/h13114109737/hxj.git

- 添加 / 删除/修改远端仓库

  - git remote get-url origin / git remote -v ：查看远端仓库
  - git remote add origin <远端仓库的url>：添加远端仓库
  - git remote remove origin：删除远端仓库
  - git remote set-url origin <远端仓库的url>：修改远端仓库

- 将代码上推到远端仓库
  
- git push -u origin master
  
- 从远端仓库下拉代码
  
- git pull origin master 
  
- 从服务器（远端仓库）克隆项目到本地
  - git clone <远端仓库的url>  <项目新的名字>

    （不加项目的新名字的话就默认项目名字）

- 配置免密访问（生成密钥对）

  - (1)ssh-keygen -t rsa -b 2048 -C 1975436224@qq.com
  - (2)cat /root/.ssh/id_rsa.pub
  - (3)在远端服务器的仓库中部署SSH公钥就可以实现免密访问了

- windows配置git免密

  1. git config --global --list：如果显示自己仓库的用户名和密码表示已经配置

  2. 如果没有：git config --global user.name "用户名"

     ​				   git  config --global user.emal "邮箱"

  3. ssh-keygen -t rsa -C "邮箱"
  4. 执行完密令以后需要进行3~4次确认：
     1. 确认密钥的保存路径（如果不需要改路径直接回车）
     2. 如果上一步指定的保存路径已有密钥文件，则需要确认是否覆盖（如果之前的密钥不需要直接回车覆盖，需要则手动拷贝到其他目录后再覆盖）
     3. 创建密码（如果不需要直接回车）
     4. 确认密码
  5. 进入到id_rsa.pub文件中将内容复制到仓库的SSH公钥下面的公钥栏保存即可（可能第一次Push还是认证后续不用）

```
1. git clone xxxxxx.git (master不能操作)
2. 建立自己的分支：git checkout -b 分支名
3. 操作完以后合并分支（不能合并到master,一般是dev分支）：git merge dev
```