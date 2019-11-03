1. 别名

- alias - 别名

```
[root ~]# alias ll='ls -l'
[root ~]# ll
total 8752
drwxr-xr-x 7 root root    4096 Sep  6 19:37 blog
drwxr-xr-x 6 root root    4096 Sep 11 11:46 bolg
drwxr-xr-x 4 root root    4096 Sep  8 09:40 code
drwxr-xr-x 3 root root    4096 Sep  6 13:21 day
drwxr-xr-x 6 root root    4096 Sep  6 13:58 day2
-rwxr-xr-x 1 root root      62 Sep  7 10:00 greet.sh
drwxr-xr-x 2 root root    4096 Sep  4 11:06 mysql
drwxrwxr-x 7 root root    4096 Sep  4 10:45 redis-5.0.5
-rw-r--r-- 1 root root 8929280 May 16 00:26 redis-5.0.5.tar
```

- unalias - 取消别名

```
[root ~]# unalias ll
[root ~]# ll
-bash: frm: command not found
```

2. 计划任务

   - 在指定的时间执行命令

     - at ：将任务排队，在指定的时间执行该命令
      ```Linux
      [root ~]# at 5pm+3days
      at> rm -f /root/*.html
      at> <EOT>
      job 1 at Sat Sep  7 10:45:00 2019
      ```

     - atq：查看待执行的任务队列
      ```Linux
      [root ~]# atq
      9       Wed Jun  5 17:00:00 2019 a root
      ```
     - atrm：从对列中删除待执行的任务
      ```
      [root ~]# atrm 9
      ```

   - 计划任务表- crontab
       ```
       [root ~]# crontab -e
        * * * * * echo "hello,world!" >> /root/hello.txt
        59 23 * * * rm -f /root/*.log
       ```
       >说明：输入crontab -e命令会打开vim来编辑Cron表达式并指定触发的任务，上面我们定制了两个计划任务，一个是每分钟向/root目录下的		hello.txt中追加输出hello, world!；另一个是每天23时59分执行删		除/root目录下以log为后缀名的文件。
