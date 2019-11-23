### REST介绍

REST前言

> REST（Representational State Transfer）表述性状态转移，基于HTTP、URI、XML、JSON等标准和协议，支持轻量级、跨平台、跨语言的架构设计。
>
> 1. REST是所有的Web应用都应该遵守的一种架构风格（一种思想）。
> 2. REST指的是一组架构约束条件和原则，如果一个架构符合REST的约束条件和原则，就称它为RESTful架构。

#### 什么是轻量级

> web框架可以分为基于请求的（request-based）和基于组件的（component-based）两大阵营。前者的代表有Struts和Spring MVC等，后者的成员则有JSF、Tapestry等等。
>
> 轻量级框架一般是由Struts , Spring组成的，侧重于减小开发的复杂度，但是相应的它的处理能力便有所减弱（如事务功能减弱，不具备分布式处理能力），比较适用于开发中小型企业应用。
>
> 轻量级是指它的创建和销毁不需要消耗太多的资源，意味着可以在程序中经常创建和销毁session的对象；重量级意味着不能随便的创建和销毁它的实例，会占用很多资源。

#### REST核心：资源， 状态转移，统一接口

> **资源**：是REST最明显的的特征，是指对某类信息实体的抽象，资源是服务器上一个可命名的抽象概念，以名词为核心来组织命名。
>
> **状态转移**：指客户端与服务器进行交互的过程中，客户端通过对资源的表述，实现对资源增删改查的目的。
>
> **统一接口**：REST要求，必须通过统一的接口来对资源执行各种操作，对于每个资源只能执行一组有限的操作。比如客户端通过HTTP的请求方式(POST, GET, PUT, PATCH,DELETE)来操作资源，也就意味着不管你的URL是什么，请求的资源是什么，操作的接口都是统一的。

#### REST架构的主要原则

- 对网络上所有的资源都有一个资源标识符（URI）
- 对资源的操作不会改变该资源标识符
- 同一种资源有多种表现形式（XML，JSON）
- 所有的操纵都是无状态的（stateless）

*符合上述REST原则的架构方式就称为RESTful架构*

#### URI和URL的区别

> URI（uniform resource identifier）统一资源标识符，用来唯一标识一个资源，Web上的每种资源如HTML文档、图片、视频等都是由一个URI来定位的。
>
> URI一般由三部分组成：
>
> 1. 访问资源的命名机制
> 2. 存放资源的主机名
> 3. 资源自身的名称，由路径标识，着重强调资源
>
> URL（uniform resource locator）统一资源定位器，它是一种具体的URI，即URL可以用来标识一个资源而且还指明了如何定位（查找）这个资源。
>

### RESTful介绍

> 1. RESTful是一种常见的REST应用，是遵循REST风格的web服务，REST式的web服务是一种ROA（面向资源的架构）。
> 2. RESTful是一种软件架构风格、设计风格，而不是标准
> 3. 所有的东西都是资源，每一个网址代表一种资源。所有的操作都通过对资源的增删改查
> 4. 对资源的增删改查对应的URL的操作（POST,DELETE,PUT,PATCH,GET）
> 5. 无状态的（不能使用session）
> 6. URL命名
>   a）/资源
>   b）/资源名称/{资源ID}
>   c）/资源名称/{资源ID}/子资源名称
>   d）/资源名称/{资源ID}/子资源名称/{子资源ID}
>
> 例如有一个API提供动物园（zoo）的信息，还包括各种动物和雇员的信息，则它的路径应该设计成下面这样。
>
> ```
> https://api.example.com/v1/zoos
> 
> https://api.example.com/v1/animals
> 
> https://api.example.com/v1/employees
> ```
>
> 

#### RESTful资源操作

|  http方法   | 资源操作 | 幂等 | 安全 |
| :---------: | :------: | :--: | :--: |
|     GET     |  SELECT  |  是  |  是  |
|    POST     |  INSERT  |  否  |  否  |
| PUT / PATCH |  UPDATE  |  是  |  否  |
|   DELETE    |  DELETE  |  是  |  否  |

> 幂等性：对同一个REST接口多次访问，得到的资源状态是相同的。
>
> 安全性：对该REST接口的访问，不会使服务器的状态发生改变。

#### 传统的URL请求格式

```
http://127.0.0.1/user/query/1 　GET 根据用户id查询用户数据

http://127.0.0.1/user/save 　POST 新增用户

http://127.0.0.1/user/update 　POST 修改用户信息

http://127.0.0.1/user/delete 　GET/POST 删除用户信息

```

#### RESTful请求格式

```
http://127.0.0.1/user/1　GET 根据用户id查询用户数据

http://127.0.0.1/user 　POST 新增用户

http://127.0.0.1/user 　PUT 修改用户信息

http://127.0.0.1/user 　DELETE 删除用户信息
```

#### 接口分类

##### １．HTTP　Methods

| HTTP Operation | Description |
| :------------: | :---------: |
|      GET       |    查找     |
|      POST      |    增加     |
|      PUT       |    更新     |
|     PATCH      |  部分更新   |
|     DELETE     |    删除     |

##### 2. 接口分类

```
资源对象的CRUD操作
GET http://api/users          #获取trades列表
GET http://api/users/{id}     #根据id获取单个user
POST http://api/users         #创建user
PUT http://api/users/{id}     #根据id更新user
PATCH http://api/users/{id}    #根据id部分更新user
DELETE http://api/users/{id}  #根据id删除user
```

#### 响应设计

> 原则：数据接收到即可使用，无需拆箱
>
> **1、什么是装箱？什么是拆箱？**
>
> 装箱：基本类型转变为包装器类型的过程。
> 拆箱：包装器类型转变为基本类型的过程。
>
> **2、装箱和拆箱的执行过程？**
>
> - 装箱是通过调用包装器类的 valueOf 方法实现的
> - 拆箱是通过调用包装器类的 xxxValue 方法实现的，xxx代表对应的基本数据类型。
> - 如int装箱的时候自动调用Integer的valueOf(int)方法；Integer拆箱的时候自动调用Integer的intValue方法。

**在一次请求中，content body仅仅用于传输数据，Header中存放描述请求或请求的元数据**

```
错误做法
{
	"status": 200,
	"data": {
		"user_id": 1001,
		"user_name": "张飞"
	}
}

正确的做法
Response Headers:
	Status: 200
Response Body:
    {
        "user_id": 1001,
        "user_name": "张飞"
    }
```

