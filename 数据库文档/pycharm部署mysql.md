```
pymasql获取的数据库连接对象并不是线程安全的（在多线程环境下会出错）如果希望每个线程都持有自己的资源避免因为资源竞争导致的加锁排队，可以使用treading模块的local类来是实现讲资源跟线程绑定，让每个线程持有自己的资源
```



1. 先完成pycharm配置环境的操作(见Linux文件夹中的pycharm环境配置)

2. 准备mysql环境

   - 下载MySQL需要的包：Terminal: pip install pymysql -i https://pypi.doubanio.com/simple
   - 读取并下载依赖项：pip install -r requirements.txt
   - 上传项目之前需要导出依赖项：pip freeze > retuqirements.txt

3. 连接数据库

   ```
   第一步：指定主机、端口、用户名、口令、数据库、字符集创建连接
   第二步：通过连接对象的cursor方法获取游标对象
   第三步：通过游标对象的execute方法向数据库发送SQL
   第四步：所有的操作都成功就提交；出现错误就回滚（撤销）
   第五步：关闭连接释放资源
   ```

4. 增加操作

   ```
   """---author==hxj---"""
   import pymysql

   no = input("部门编号：")
   name = input("部门名称：")
   location = input("部门所在地：")
   conn = pymysql.connect(host='118.31.103.87', port=3306,
                          user='root', password='123456',
                          database='hrs', charset='utf8'
                          )
   try:
       with conn.cursor() as cursor:
           # 这里的%s不是python中的字符串占位符，而是安全的占位符。
           result = cursor.execute('insert into tb_dept values (%s, %s,%s)',(no,name,location))
           result = cursor.execute('delete from tb_dept where dno=%s', (no, ))
           if result == 1:  # result不为空
               print("添加成功！！")
       conn.commit()
   except pymysql.MySQLError as err:
       print(err)
       conn.rollback()
   finally:
       conn.close()
   ```
  
   ```
   """批处理插入，提高效率"""
   import json

   import pymysql
   import requests

   conn = pymysql.connect(host='120.77.222.217', port=3306,
                          user='root', password='123456',
                          database='hrs', charset='utf8')
   try:
       for page in range(1, 11):
           resp = requests.get(f'http://api.tianapi.com/topnews/?key=9aeb28ee8858a167c1755f856f830e22&page={page}&num=10')
           newslist = json.loads(resp.text)['newslist']
           params = []
           for news in newslist:
               params.append((news['title'], news['description'], news['url'], news['source'], news['ctime']))
           with conn.cursor() as cursor:
               # 执行批处理（将多个insert操作合成一条SQL发给数据库）
               cursor.executemany(
                   'insert into tb_news (title, description, url, source, ctime) values (%s, %s, %s, %s, %s)',
                   params
               )
           conn.commit()
   finally:
       conn.close()
   ```

   ​

   5. 删除操作

   ```
    import pymysql

    no = input("要删除的部门编号：")
    conn = pymysql.connect(host='118.31.103.87', port=3306,
                           user='root', password='123456',
                           database='hrs', charset='utf8'
                           )
    try:
        with conn.cursor() as cursor:
            result = cursor.execute('delete from tb_dept where dno=%s', (no, ))
            if result == 1:
                print("删除成功！！")
        conn.commit()
    except pymysql.MySQLError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()
   ```
   
   6.修改（更新）操作

   ```

    import pymysql

    no = input("部门编号：")
    name = input("部门名称：")
    location = input("部门所在地：")
    conn = pymysql.connect(host='118.31.103.87', port=3306,
                           user='root', password='123456',
                           database='hrs', charset='utf8'
                           )
    try:
        with conn.cursor() as cursor:
            # result = cursor.execute('update tb_dept set dname=%s, dloc=%s where dno=%s', (name, location, no))
            cursor.execute( )
            if result == 1:  # result不为空
                print("修改成功！！")
        conn.commit()
    except pymysql.MySQLError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()
   ```

   7.查询操作

- 方法1

   ```
   import pymysql

   conn = pymysql.connect(host='118.31.103.87', port=3306,
                          user='root', password='123456',
                          database='hrs', charset='utf8'
                          )
   try:
       with conn.cursor() as cursor:
           cursor.execute(
               'select dno, dname, dloc from tb_dept'
           )
           # print(cursor.fetchmany(3)) 打印3条记录
           print(cursor.fetchone()) 返回值是一个迭代器，一次打印一条记录
           print(cursor.fetchone())
           for row in cursor.fetchall():
               print(f'{row[0]}\t{row[1]}\t{row[2]}')

   except pymysql.MySQLError as err:
       print(err)
       conn.rollback()

   finally:
       conn.close()
   ```


- 方法2

   ```
        import pymysql

          # 查询到的是一个字典,用字典来显示
        conn = pymysql.connect(host='118.31.103.87', port=3306,
                               user='root', password='123456',
                               database='hrs', charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor
                               )
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    'select dno as no, dname as name, dloc as location from tb_dept'
                )
                for row in cursor.fetchall():
                    print(f'{row["no"]}\t{row["name"]}\t{row["location"]}')
    
        except pymysql.MySQLError as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
   ```
   

- 方法3

   ```
    import pymysql
    
    class Dept:
    
          def __init__(self, no, name, location):
              self.no = no
              self.name = name
              self.location = location
       
          def __str__(self):
              return f'{self.no}\t{self.name}\t{self.location}'
    
      conn = pymysql.connect(host='118.31.103.87', port=3306,
                             user='root', password='123456',
                             database='hrs', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
      try:
          with conn.cursor() as cursor:
              cursor.execute(
                  'select dno as no, dname as name, dloc as location from tb_dept'
              )
              for row in cursor.fetchall():
                  dept = Dept(**row)
                  print(dept)
    
      except pymysql.MySQLError as err:
          print(err)
   ```
