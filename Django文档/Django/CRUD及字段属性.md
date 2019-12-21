### 模型(models)中常用的字段属性

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
  
  return HttpResponse('修改数据成功!'
  ```




### CRUD操作

```
示例：
class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True, null=False)
    s_age = models.IntegerField(default=20)
    s_gender = models.BooleanField(default=1)
    s_create = models.DateTimeField(auto_now_add=True)
    s_alter_time = models.DateTimeField(auto_now_add=True)
    s_gaoshu = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    s_xiandai = models.DecimalField(max_digits=3, decimal_places=1, null=True)

    class Meta:
        db_table = 'student'
```

> **objects：管理器  ； filter()结果为Queryset  ； first()获取结果中第一个元素**



#### 1. 增加数据

> 方法1：对象 = 模型名(字段名=值） 对象.save()
>
> ```
> 需定义def __init__方法：
> stu = Student(s_name='张飞', s_age=20)
> stu.save()
> ```
>
> 方法2：对象 = 模型名
>
> ```
> stu = Student()
> stu.s_name = '张飞'
> stu.s_age = 20
> stu.save()
> ```
>
> 方法3：create()
>
> ```
> Student.objects.create(s_name='张飞, s_age=20)
> ```



#### 2. 删除数据

> 方法1：通过对象删除
>
> ```
> stu = Student.objects.filter(id=1).first()
> stu.delete()
> ```
>
> 方法2：直接通过模型删除
>
> ```
> Student.objects.filter(id=1).delete()
> ```



#### 3. 修改数据

> 方法1：先获取对象再修改属性
>
> ```
> stu = Student.objects.filter(s_name='张飞')
> stu.s_name = '刘备'
> stu.s_age = 21
> stu.save()
> ```
>
> 方法2：update()
>
> ```
> Student.objects.filter(s_name='张飞').update(s_name='刘备', s_age=21)
> ```



#### 4. 查询数据

**基本语法：模型名.objects.属性名**

##### 1. filter(条件)：指定条件查询，条件不满足不会报错回返回None

filter()查询到结果是一个集合不可以直接获取对象的属性，filter().first()查询到的结果是一个对象，可以直接获取对象的属性。

```
>>> stu = Student.objects.filter(s_name='张飞')
>>> print(stu)
<QuerySet [<Student: Student object (2)>]>
>>> print(stu.s_gender)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 's_gender'
>>> stu = Student.objects.filter(s_name='张飞').first()
>>> print(stu)
Student object (2)
>>> print(stu.s_age)
18
>>>
```

##### 2. all()：查询所有的结果

```
>>> Student.objects.all()
<QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student obje
ct (5)>, <Student: Student object (6)>, <Student: Student object (7)>]>

```

##### 3. values()：获取到的值是字典类型

```
# 查询所有字段
>>> Student.objects.values()
<QuerySet [{'id': 1, 's_name': '李四', 's_age': 23, 's_gender': 1, 's_create_time': datetime.datetime(2019, 9, 18, 3, 33, 22, 284923, tzinfo=<DstTzInfo 'Asia
/Chongqing' CST+8:00:00 STD>), 's_alter_time': datetime.datetime(2019, 11, 7, 12, 15, 41, 770025, tzinfo=<DstTzInfo 'Asia/Chongqing' CST+8:00:00 STD>), 's_ga
oshu': Decimal('95.0'), 's_xiandai': Decimal('85.0')}]>

# 指定查询字段
>>> stu = Student.objects.values('s_name')
>>> print(stu)
<QuerySet [{'s_name': '吕布'}, {'s_name': '大乔'}, {'s_name': '小乔'}, {'s_name': '张飞'}, {'s_name': '李四'}, {'s_name': '王五'}, {'s_name': '貂蝉'}]>
```

##### 4. get()：查询单个对象

```
>>> stu = Student.objects.get(s_name='张飞')
>>> print(stu)
Student object (2)
>>>
```

##### 5. exclude(条件)：过滤出不满足条件的所有结果

```
>>> stu = Student.objects.exclude(s_gender='1')
>>> print(stu)
<QuerySet [<Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>]>
>>> stu = Student.objects.exclude(s_age__gt=20)
>>> print(stu)
<QuerySet [<Student: Student object (2)>, <Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>, <Student: Student obje
ct (7)>, <Student: Student object (8)>]>
```

##### 6. order_by：排序

```
# 降序 desc
>>> stu_desc = Student.objects.order_by('-s_age')
>>> print(stu_desc)
<QuerySet [<Student: Student object (3)>, <Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (6)>, <Student: Student obje
ct (7)>, <Student: Student object (5)>, <Student: Student object (4)>]>

# 升序 asc
>>> stu_asc = Student.objects.order_by('s_age')
>>> print(stu_asc)
<QuerySet [<Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (2)>, <Student: Student object (6)>, <Student: Student obje
ct (7)>, <Student: Student object (1)>, <Student: Student object (3)>]>
```

##### 7. exists()：判断是否存在查询的值，存在True，不存在False

```
>>> stu = Student.objects.filter(s_age=30).exists()
>>> print(stu)
False
>>> stu = Student.objects.filter(s_age=18).exists()
>>> print(stu)
True
```

##### 8. count()：计算结果个数

```
>>> stu = Student.objects.filter(s_age=20).count()
>>> print(stu)
3
```

##### 9. 

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

重点：
1+N查询问题：当查询的对象又关联到其他对象，如果要获取关联对象的属性，在默认情况下，Django的ORM框架会执行1+N查询，效率非常低下。如果查询中存在关联查询，我们可以使用inner join或者left outer join的方式来替代1+N查询
~ 一对一或多对一：select_related('关联对象')
~ 多对多：prefetch_related('关联对象')

优化ORM操作：
~ QuerySet ---> only() - 指定只查询哪些属性
~ QuerySet ---> defer() - 指定延迟查询哪些属性
```
```
 # 多条件查询, 且或非
 and
 # 链式 filter().filter().filter()
 # stus = Student.objects.filter(s_gender=1).filter(s_age__gt=20)
 # print(stus)
 # stus = Student.objects.filter(s_gender=1, s_age__gt=20)
 # print(stus)
 # print('=========Q========')
 
 Q()作用和and一样
 # stus = Student.objects.filter(Q(s_gender=1), Q(s_age__gt=20))
 # stus = Student.objects.filter(Q(s_gender=1) & Q(s_age__gt=20))
 # print(stus)
 # print('========或==========')
 # 或必须将条件用Q括起来
 # stus = Student.objects.filter(Q(s_gender=1) | Q(s_age__gt=20))
 # print(stus)
 
 # print('================非====================')
 非 (查询不大于20的)
 # stus = Student.objects.filter(~Q(s_age__gt=20))
 # stus = Student.objects.filter(s_age__lte=20)
 # stus = Student.objects.exists(s_age__gt=20)
 # print(stus)

 模糊查询
 # contains(包含),类似于like %羽% / icontains-忽略大小写
 # stus = Student.objects.filter(s_name__contains='羽')
 # print(stus)

 # startswith 查询是否以指定条件开头
 # stus = Student.objects.filter(s_name__startswith='王')
 # print(stus)

 # endswith 查询是否以指定条件结尾
 # stus = Student.objects.filter(s_name__endswith='王')
 # print(stus)

 # F对比两字段的值 / 更新数据
 # sql: select * from student where s_gaosu > s_xiandai
 stus = Student.objects.filter(s_gaoshu__gt=F('s_xiandai'))
 print(stus)
 
 stus = Student.objects.filter(s_no=1001)
 stus.update(s_age=F('s_age')+10)

 stus = Student.objects.filter(s_gaoshu__gt=F('s_xiandai') - 10)
 print(stus)
```

