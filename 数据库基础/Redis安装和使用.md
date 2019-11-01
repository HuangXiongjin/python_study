1. Redis (Remote Dictionary Server)的工作模式(优点) ?
   键值对形式存储数据的数据库，放在内存中，单线程+异步I/O(多路I/O复用)的工作模式
2. 应用场景
- 高速缓存服务（用户经常访问的数据从数据库搬到内存中）
- 实时排行榜
- 投票点赞
- 消息队列
3. 源代码构建安装

   1. 可以使用yum来安装，也可以通过Redis(https://redis.io/)官方网站下载源代码构建安装

   ```
   [root@izbp15547sumlsn3rij2lmz ~]# http://download.redis.io/releases/redis-5.0.4.tar.gz
   [root@izbp15547sumlsn3rij2lmz ~]# redis-5.0.4.tar.gz
   [root@izbp15547sumlsn3rij2lmz ~]#tar -xvf redis-5.0.4.tar
   [root@izbp15547sumlsn3rij2lmz ~]# ls
   blog  code  day2      greet.sh  redis-5.0.5  redis.log
   bolg  day   dump.rdb  mysql     redis-5.0.5.tar  redis.error.log
   [root@izbp15547sumlsn3rij2lmz ~]# cd redis-5.0.4
   [root@izbp15547sumlsn3rij2lmz redis-5.0.5]# make && make install
   ```

   2. 进入到redis.conf中指定自己需要的ip和端口

   ```
   [root@izbp15547sumlsn3rij2lmz redis-5.0.5]# vim redis.conf
   
     69 bind 127.0.0.1
     70 
     71 # Protected mode is a layer of security protection, in order to avoid that
     72 # Redis instances left open on the internet are accessed and exploited.
     73 #
     74 # When protected mode is on and if:
     75 #
     76 # 1) The server is not binding explicitly to a set of addresses using the
     77 #    "bind" directive.
     78 # 2) No password is configured.
     79 #
     80 # The server only accepts connections from clients connecting from the
     81 # IPv4 and IPv6 loopback addresses 127.0.0.1 and ::1, and from Unix domain
     82 # sockets.
     83 #
     84 # By default protected mode is enabled. You should disable it only if
     85 # you are sure you want clients from other hosts to connect to Redis
     86 # even if no authentication is configured, nor a specific set of interfaces
     87 # are explicitly listed using the "bind" directive.
     88 protected-mode yes
     89 
     90 # Accept connections on the specified port, default is 6379 (IANA #815344).
     91 # If port 0 is specified Redis will not listen on a TCP socket.
     92 port 6379
     93 
   
   ```

4. 启动服务器(随便一种都行)
- redis-server &
- redis-server  --requirepass <设置密码> > redis.log &  ——可以指定日志文件
- redis-server --port <指定端口号> --requirepass <设置密码> --appendonly yes 
5. 启动Redis客户端

   redis-cli -h 主机IP地址 -p
    主机:端口> auth 密码（心跳检测事件验证是否启动成功ping - pong）
   
   ```
   [root@izbp15547sumlsn3rij2lmz redis-5.0.5]# redis-cli -h 127.0.0.1
   127.0.0.1:6379> ping
   PONG
   [root@izbp15547sumlsn3rij2lmz redis-5.0.5]# redis-cli -h 118.31.103.87
   118.31.103.87:6379> 
   ```
   
6. 命令参考手册（学习网址：http://redisdoc.com/）
- 字符串(srting)
```
set key value - 创建一个字符串类型的键值对
set key value ex 30 - 将键的过期时间设置为30seconds后消失
ttl key - 查看该键何是消失（-1永不超时）
get key - 获取key对应的value
mset a 1 b 3 c 4 - 创建多组键值对
mget a b c - 获取多组键值对的值
dbsize - 查看有几组键值对
del key1 key2 - 删除指定键值对
exists key - 查看是否存在该键值对
setnx / sertex
bgsave - 后台保存
select <数字> - 切换数据库（初始在0，共有16个）
flushdb(flushall) - 删除当前数据库（所有数据库）
incr key - 当键值对的值是数字的时候，可以使用incr让值加一,相当于value += 1操作
desr key - 值减1
incrby key <num> - 指定键值对的值增加多少, value += num
strlen key - 获取键值对的长度
```
- 哈希表(hash)
```
hset <字段名> key1 value1 - 一次创建一个键值对
hset <字段名> key2 value2
hmset <字段名> key1 value1 key2 value2... - 一次性创建多个键值对
hget <字段名> key1 - 获取key对应的value
hmget <字段名> key1 key2.. - 获取多个value
hkeys <字段名> - 获取全部的key
hvals <字段名> - 获取全部value
hgetall <字段名> - 获取全部key和value
```

```
127.0.0.1:6379> hset stu stuid 1001
(integer) 1
127.0.0.1:6379> hset stu name huang
(integer) 1
127.0.0.1:6379> hset stu gender male
(integer) 1
127.0.0.1:6379> hmset stu2 stuid 1002 name xiong gender male bitrh 1996-10-28
OK
127.0.0.1:6379> hget stu
(error) ERR wrong number of arguments for 'hget' command
127.0.0.1:6379> hget stu stuid
"1001"
127.0.0.1:6379> hmget stuid name gender
1) (nil)
2) (nil)
127.0.0.1:6379> hmget stu name gender 
1) "huang"
2) "male"
127.0.0.1:6379> hvals stu
1) "1001"
2) "huang"
3) "male"
127.0.0.1:6379> hgetall stu
1) "stuid"
2) "1001"
3) "name"
4) "huang"
5) "gender"
6) "male"
127.0.0.1:6379> 

```

- 列表（python中的列表一样）
  - lpush key value —— 往列表的左边依次放数据
  - rpush key value —— 往列表的右边依次存放数据
  - lrange key <开始下标> <结束下标> —— 遍历列表中的值
  - lpop key —— 移出列表中左边第一个值
  - rpop key —— 移出列表中右边的第一个值

```
127.0.0.1:6379> lpush numbers 1 2 3 4 5 6 
(integer) 6
127.0.0.1:6379> lrange numbers 0 6
1) "6"
2) "5"
3) "4"
4) "3"
5) "2"
6) "1"
127.0.0.1:6379> lpop numbers 
"6"
127.0.0.1:6379> lpop numbers1
"1"
127.0.0.1:6379> rpop numbers1
"6"
127.0.0.1:6379> 

```

- 集合（set）自动去重
  - sadd key value1 value2... —— 往集合(key)中添加元素
  - srem key value1—— 删除元素
  - smembers key —— 查看集合中的元素
  - scard key —— 查看集合中元素的个数
  - sismember key value —— 查看指定元素是否在集合中，1在0不在
  - spop key <num> —— 随机移除集合中的num个元素
  - sinter key1 key2 —— 求交集
  - sunion key1 key2 —— 求并集
  - sdiff key1 key2 —— 求差集

```
127.0.0.1:6379> sadd set1 1 2 3 4 5 6
(integer) 6
127.0.0.1:6379> smembers set1
1) "1"
2) "2"
3) "3"
4) "4"
5) "5"
6) "6"
127.0.0.1:6379> scard set1
(integer) 6
127.0.0.1:6379> sismembers set1 7
(error) ERR unknown command `sismembers`, with args beginning with: `set1`, `7`, 
127.0.0.1:6379> sismember set1 7
(integer) 0
127.0.0.1:6379> sismember set1 1
(integer) 1
127.0.0.1:6379> 

```

- 有序集合（zset）
  - zadd student 100 zhangsan 88 wangwu 98 zhaoliu —— 创建一个有序集合
  - zrange student 0 -1—— 根据分数升序，0 -1 表示显示全部的记录
  - zrange student 0 -1 wtihtscores —— (withscores)连同结果一并显示
  - zrevrange sorce 0 -1 —— 降序
  - zincrby student 150 wangwu —— 修改wangwu的分数

```
127.0.0.1:6379> zadd student 100 zhangsan 88 wangwu 98 zhaoliu
(integer) 3
127.0.0.1:6379> zrange student 0 -1
1) "san"
2) "zhang"
3) "wangwu"
4) "zhaoliu"
5) "zhangsan"
127.0.0.1:6379> zrange student 0 -1 withscores
1) "san"
2) "34"
3) "zhang"
4) "78"
5) "wangwu"
6) "88"
7) "zhaoliu"
8) "98"
9) "zhangsan"
10) "100" 
127.0.0.1:6379> zadd student 100 zhangsan 88 wangwu 98 zhaoliu
(integer) 3
127.0.0.1:6379> zrange student 0 -1
1) "san"
2) "zhang"
3) "wangwu"
4) "zhaoliu"
5) "zhangsan"
127.0.0.1:6379> zrange student 0 -1 withscores
1) "san"
2) "34"
3) "zhang"
4) "78"
5) "wangwu"
6) "88"
7) "zhaoliu"
8) "98"
9) "zhangsan"
10) "100"
```

