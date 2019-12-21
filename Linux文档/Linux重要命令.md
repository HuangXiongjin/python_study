#### 基本命令

- 按一个w再按tab键可以提示w开头的有哪些命令。
- ctrl+a 光标回到行首
- ctrl+e 光标回到行尾
- ctrl+u  删除整行
- ctrl+w  删除一个单词
- ctrl+d 结束输入
- ctrl+z 暂停命令放到后台
- ctrl+c 退出任务
- date 查看当前时间
- init 6~0 ：重启6 关机0
- shutdown 关闭服务器
  - -c  取消关机
  - -r  重启
  - -h  定小时关机

- 链接
  - 软连接 ：ln -s  源路径   目标路径  ——给源路径对应的文件在目标路径下创建一个软链接(可以看成是快捷键)(源路径是绝对路径)
      ```
      ln -s /usr/local/python37/bin/python3.7 /usr/bin/pyhon3
      ```
  - 硬链接 ：ln 源路径  目标路径  ——给源路径对应的文件在目标路径下创建一个硬链接(看成一个数据的多个引用)

  注意: 源文件不存在的时候，软件无效，硬链接变成普通文件

#### 文件操作相关命令

- pwd - print working direcotory —— 打印工作目录
- /root -- 超级管理员用户目录
- /home/** -- 普通用户目录

- ls （list directory contents）—— 列出目录下的内容
- -a : 查看所有的文件（以点开头的是隐藏文件或文件夹）
- -l ：长格式查看
- -R：递归式查看(遇到文件夹要查看文件下的内容)
- <命令>--help ：查看命令的帮助
- man<>
- clear ：清屏
- history ：查看历史命令
  - !<命令编号> : 再次使用该命令
- touch : 创建**空文件或者修改文件**的最后访问时间
- mkdir（make directory）—— 创建**文件夹**
  - -p (--parents) ：在创建文件夹下再创建一个文件夹
  - mkdir -p a/b/c ：按层级依次创建a,b,c三个文件夹
  - mkdir -p a/{b,c} ：先创建a文件夹，再在a文件夹下创建b,c(同层)两个文件夹 
- rmdir (remove empty directory) ：rmdir <文件夹名> --- 删除**空**的文件夹 
- rm(remove): 删除文件或文件夹
  - -i ：交互式删除（interactive）
  - -f ：强制删除（force）porhub
  - -r ：递归式删除(recursive)
  - -rf ：强制删除文件夹
- cp(copy) ： 拷贝文件
  - cp  <文件名>  <文件夹名>：将文件拷贝到文件夹中
  - cp  <文件名1>  <文件名2>： 将文件1拷贝到文件2中，但是会覆盖文件2中的内容
  - -r ：递归式拷贝；
  - cp -r 文件夹1 文件夹2：将文件夹1拷贝到文件夹2中
- cat/tac -- concatenate :连接文件并打印内容
- head/tail：从头查看/从尾查看
- more/less 分页查看
- inconv - 转换文件编码 ：iconv -f gb2312 -t utf-8  qq.html  把文件的编码转换为utf-8

#### vim的使用

- 命令模式：按Esc可以回到命令模式
- 输入模式：按 i 进入输入模式
- 光标移动（在命令模式下）：
  - h j k l -- 左 下 上 右
  - ctrl+e -- 光标向下一行
  - ctrl+y -- 光标向上一行
  - ctrl+f -- 光标向下翻一页
  - ctrl+b -- 光标向上翻一页
  - 0 - 移到开头；＄ - 移到末尾；w - 移动到下一个单词
  - gg - 移到行首 ；G - 移到行尾 ；<num> G - 移到指定的行
- 编辑内容：
  - dd ： 删除当前行，并且缩进
  - <num>dd ： 删除指定行
  - d0 ：删除光标所在的后面所有行
  - d＄：删除光标所在行不缩进
  - dw ：删除当前单词
  - 先按yy在按p ：表示复制行
  - u/ctrl+r/ ：撤销   **.** ：回复撤销
- 保存退出：ZZ
- 末行模式：在命令模式下按冒号
- chmod 修改文件的权限
  - chmod [a, u, g, o] [+, -] [r, w, x]  <文件名> 
    ```
    a:所有，u:自己，g:同组，o:其他
    +：添加， -: 取消
    r:读，w:写，x:执行
    例如：
    [root@izbp15547sumlsn3rij2lmz shell编程]# chmod +x second_shell.sh 
    
    ```
    

