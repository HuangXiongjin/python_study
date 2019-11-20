### serializers是什么？

> 将复杂的数据结构，例如ORM中的QuerytSet或者Model实例对象转换为Python内置的数据类型，更加方便将数据转换为json、xml等格式的数据类型。

### serializers的作用

> 1. 将queryset或者model实例等进行系列化，转换成json格式，返回给用户(api)
> 2. 将POST/PUT/PATCH上传的数据进行校验
> 3. 将POST/PUT/PATCH上传的数据进行处理

### serialziers中的字段

![](E:\django笔记\photo\serializers.png)

#### 1.常用的字段

**CharField、BooleanField、IntegerField、DateTimeField**

```
# 举例子
mobile = serializers.CharField(max_length=11, min_length=11)
age = serializers.IntegerField(min_value=1, max_value=100)

# format可以设置时间的格式，下面例子会输出如:2018-1-24 12:10
pay_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M')
is_hot = serializers.BooleanField()
```

> **在django中，form更强调对提交的表单进行一种验证，而serializer的field不仅在进行数据验证时起着至关重要的作用，在将数据进行序列化后返回也发挥着重要作用**

#### 2.Core arguments（核心参数）

> - **read_only**：True表示不允许用户自己上传，只能用于api的输出。**如果某个字段设置了read_only=True，那么就不需要进行数据验证，只会在返回时，将这个字段序列化后返回**
>
>   举个简单的例子：在用户进行购物的时候，用户post订单时，肯定会产生一个订单号，而这个订单号应该由后台逻辑完成，而不应该由用户post过来，如果不设置read_only=True，那么验证的时候就会报错。
>
>   ```
>   order_sn = serializers.CharField(readonly=True)
>   ```
>
> - **write_only**: 与read_only对应 ，需要用户传进来
>
> - **required**: 顾名思义，就是这个字段是否必填。
>
> - **allow_null/allow_blank**：是否允许为NULL/空 
>
> - **error_messages**：出错时，信息提示。
>
>   ```
>   name = serializers.CharField(required=True, min_length=6,
>                   error_messages={
>                       'min_length': '名字不能小于6个字符',
>                       'required': '请填写名字'})
>   ```
>
> - **label**: 字段显示设置，如 label=’验证码’
>
> - **help_text**: 在指定字段增加一些提示文字，这两个字段作用于api页面比较有用 
>
> - **style**: 说明字段的类型
>
>   ```
>   # 在api页面，输入密码就会以*显示
>   password = serializers.CharField(
>       style={'input_type': 'password'})
>   # 会显示选项框
>   color_channel = serializers.ChoiceField(
>       choices=['red', 'green', 'blue'],
>       style={'base_template': 'radio.html'})
>   ```
>
> - #### HiddenField
>
>   HiddenField的值不依靠输入，而需要设置默认的值，不需要用户自己post数据过来，也不会显式返回给用户，最常用的就是user。我们在登录情况下，进行一些操作，假设一个用户去收藏了某一门课，那么后台应该自动识别这个用户，然后用户只需要将课程的id post过来，那么这样的功能，我们配合CurrentUserDefault()实现。
>
>   ```
>   # 这样就可以直接获取到当前用户
>   user = serializers.HiddenField(default=serializers.CurrentUserDefault())
>   ```