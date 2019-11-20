### 模型(models)中的字段属性

|          字段名          |                             解释                             |
| :----------------------: | :----------------------------------------------------------: |
|        AutoField         |                自动增长字段，primary_key=True                |
|       IntegerField       |                           整数字段                           |
|    SmallIntegerField     |                         小整数数字段                         |
| PositiveSmallItegerField |                         正小整数字段                         |
|   PositiveIntegerField   |                          正整数字段                          |
|     BigIntegerField      |                            长整型                            |
|       BooleanField       |                布尔类型，真为True，假为False                 |
|        CharField         |               字符类型，必须提供max_length参数               |
|        TextField         |                           文本类型                           |
|        EmailField        |                   字符串类型，提供验证机制                   |
|        FloatField        |                            浮点型                            |
|        DateField         |                           年-月-日                           |
|      DateTimeField       |                 年-月-日 时:分:秒 毫秒 时区                  |
|        TimeField         |                      时:分:秒 毫秒 时区                      |
|       DecimalField       | 10进制小数，参数：max_digits:小数总长度，decimal_palce:小数位数 |
|        ImageField        |                 存储图片(二进制或者图片路径)                 |

#### 约束定义

- null=True ：不为空

- primary_key ：主键

- max_length ：最大长度

- default ：，默认值

- auto_now_add：字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值。但是之后的save()是可以手动赋值的。也就是新实例化一个model，想手动存其他时间，就需要对该实例save()之后赋值然后再save()

- auto_now：字段保存时会自动保存当前时间，但要注意每次对其实例执行save()的时候都会将当前时间保存，也就是不能再手动给它存非当前时间的值。

  ```
  # 第一种方法：先获取对象，在修改属性，最后保存,s_alter_time会改变
  # objects 管理器， filter()结果为Queryset，first()获取结果中第一个元素
  stu = Student.objects.filter(s_name='李四').first()
  print(stu)
  stu.s_gaoshu = 95
  stu.save()
  
  # 第二种方法：filter().update()，修改时间s_alter_time不会改变
  Student.objects.filter(s_name='刘备').update(s_name='王五')
  
  return HttpResponse('修改数据成功!')
  ```

  

### CRUD操作

- #### 增加数据：对象=模型名（字段名=值） 对象.save()
```
stu = Student(s_name='张飞')
stu.save()
```

- #### 修改数据
```
# 第一种方法：先获取对象，在修改属性，最后保存
stu = Student.objects.filter(s_name='张飞').first()
stu.s_name = '关羽'
stu.save()
# objects-管理器, filter()结果为Queryset, first()获取结果中第一个元素

# 第二种方法：filter().update()
Student.objects.filter(s_name='张飞').update(s_name='关羽')
```
- #### 删除数据
```
 stu = Student.objects.filter(id=1).first()
 stu.delete()
```
- #### 查询数据
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