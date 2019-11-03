Script path ：选择项目下的manage.py
Parameters 输入：runserver / runserver <指定端口号>
创建新表或者修改表以后要先使用命令`python manage.py makemigration`；在使用python manage.py 
1. 自定义的表的生成（字段修改，字段添加...）
   生成迁移文件：python manage.py makemigrations
    应用迁移文件：python manage.py migrate
2. 模型(models)中的属性
- 字段定义的类型
   - IntegerField：整型
   - ImageField：存储图片(二进制或者图片路径)
   - BooleanField：布尔类型，真为True，假为False
   - CharField：字符串类型
   - FloatField：浮点数类型
   - DecimalField：限制小数位数
   - Datetime：年月日时分秒
   - DateField：年月日
   - TimeField：时分秒
   - TextField：文本类型
- 约束定义
   - null=True
   - primary_key
   - max_length
   - default
   - auto_now_add：当前修改后的时间
   - auto_now：当前时间，修改后不改变


- CRUD
   - 增加数据：对象=模型名（字段名=值） 对象.save()
   ```
   stu = Student(s_name='张飞')
   stu.save()
   ```

   - 修改数据
   ```
   # 第一种方法：先获取对象，在修改属性，最后保存
   stu = Student.objects.filter(s_name='张飞').first()
   stu.s_name = '关羽'
   stu.save()
   # objects-管理器, filter()结果为Queryset, first()获取结果中第一个元素

   # 第二种方法：filter().update()
   Student.objects.filter(s_name='张飞').update(s_name='关羽')
   ```
   - 删除数据
   ```
    stu = Student.objects.filter(id=1).first()
    stu.delete()
   ```
   - 查询数据
   ```
   查询格式：模型名.objects.属性名
   模型名.objects.filter()
   filter(条件)：查询满足条件的所有结果，条件不满足不会报错返回空值
   all()：查询所有的结果
   exclude(条件)：过滤出不满足条件的所有结果
   get(条件)：get中的条件必须成立，否则报错
   order_by(属性)：排序，-属性：降序(desc) 属性：升序(esc)
   filter(属性).exists()：判断是否存在查询的属性值，存在True,不存在False
   模型名.objects.all().values()：获取到的是字典
   模型名.objects.filter(属性).count()：统计结果的个数
   ```
   ```
    # 多条件查询, 且或非
    # and
    # 链式 filter().filter().filter()
    # stus = Student.objects.filter(s_gender=1).filter(s_age__gt=20)
    # print(stus)
    # stus = Student.objects.filter(s_gender=1, s_age__gt=20)
    # print(stus)
    # print('=========Q========')
    # # Q() 作用和and一样
    # stus = Student.objects.filter(Q(s_gender=1), Q(s_age__gt=20))
    # print(stus)
    # print('========或==========')
    # # 或必须讲条件用Q括起来
    # stus = Student.objects.filter(Q(s_gender=1) | Q(s_age__gt=20))
    # print(stus)
    #
    # print('================非====================')
    # # 非 (查询不大于20的)
    # stus = Student.objects.filter(~Q(s_age__gt=20))
    # # stus = Student.objects.filter(s_age__lte=20)
    # # stus = Student.objects.exists(s_age__gt=20)
    # print(stus)

    # 模糊查询
    # contains(包含),类似于like %羽%
    # stus = Student.objects.filter(s_name__contains='羽')
    # print(stus)

    # startswith 查询是否以指定条件开头
    # stus = Student.objects.filter(s_name__startswith='王')
    # print(stus)

    # endswith 查询是否以指定条件结尾
    # stus = Student.objects.filter(s_name__endswith='王')
    # print(stus)

    # 对比两字段的值
    # sql: select * from student where s_gaosu > s_xiandai
    stus = Student.objects.filter(s_gaoshu__gt=F('s_xiandai'))
    print(stus)

    stus = Student.objects.filter(s_gaoshu__gt=F('s_xiandai') - 10)
    print(stus)
   ```