---
typora-root-url: images
---

### 实现字段搜索的两种方式

1. Mysql的模糊查询 %like%

    实现起来简单，但是当数量较大的情况下，查询效率极低

2. ElasticSearch 全文搜索引擎  
    专业的全文搜索引擎，效率高，但是实现起来比较复杂

### ElasticSearch 简述
ElasticSearch是基于Lucene的搜索服务器，提供了一个分布式多用户的能力的全文搜索引擎，基于RESTful Web接口开发。ElasticSearch是用java语言开发的，是目前最受欢迎的企业级搜索引擎。

### ElasticSearch 原理
ElasticSearch 的实现原理主要分为以下几个步骤，首先用户将数据提交到Elastic Search 数据库中，再通过分词控制器去将对应的语句分词，将其权重和分词结果一并存入数据，当用户搜索数据时候，再根据权重将结果排名，打分，再将返回结果呈现给用户。

![images](https://github.com/HuangXiongjin/python_study/blob/master/Django%E6%96%87%E6%A1%A3/%E7%BD%91%E7%BB%9C%E5%8D%8F%E8%AE%AE/images/elasticsearch.png)


### ELK
ElasticSearch是与名为Logstash的数据收集和日志解析引擎以及名为Kibana的分析和可视化平台一起开发的。这三个产品被设计成一个集成解决方案，称为“Elastic Stack”（以前称为“ELK stack”）

### django中实现ElasticSearch

#### 安装和配置

    # 安装django-elasticsearch-dsl
    pip install django-elasticsearch-dsl==0.5.1
    
    # settings.py文件配置
    INSTALLED_APPS = [
            ....
        'django_elasticsearch_dsl'
    ]
    
    # 配置主机端口
    ELASTICSEARCH_DSL={
        'default': {
            'hosts': 'localhost:9200'
        },
    }

#### models.py

    from django.db import models


    class Comic(models.Model):
        """漫画模型"""
        # 漫画id
        comic_id = modes.AutoField(primary_key=True)
        # 漫画标题
        title = models.CharField(max_length=128, blank=True, null=True)
        # 漫画分类
        category = models.CharField(max_length=32, blank=True, null=True)
        # 漫画链接
        link = models.CharField(max_length=1024, blank=True, null=True)
    
        class Meta:
            db_table = 'comic'

#### documents.py(放在models.py应用目录)

    from elasticsearch_dsl.connections import connections
    from django_elasticsearch_dsl import DocType, Index
    from elasticsearch import Elasticsearch
    from elasticsearch_dsl import Search
    from elasticsearch_dsl import Q
    
    # 获取Elasticsearch对象
    client = Elasticsearch()
    
    my_search = Search(using=client)
    
    from .models import Book
    
    # 创建ElasticSearch连接
    connections.create_connection()
    
    # 指定创建索引的应用app
    book = Index('books')
    
    book.settings(
        number_of_shards=1,
        number_of_replicas=0
    )


    @book.doc_type
    class ComicDocument(DocType):
    
        class Meta:
            model = Comic
            fields = ['title', 'category']


    # 设置自己搜索的函数
    def search(keyword):
        # mutil_match 多条匹配， query查询的关键字 fields搜索的字段
        q = Q("multi_match", query=keyword, fields=['title', 'category'])
        query = my_search.query(q)
        response = query.execute()
        return response


#### 创建全文搜索索引

    python manage.py search_index --rebuilds


#### 实例

    >>> from book.models import Comic
    >>> from book.documents import search
    >>> search('镇魂街')
    <Response: [<Hit(books/doc/4): {'title': '镇魂街'}>, <Hit(books/doc/54): {'title': '镇魂街'}>, <Hit(books/doc/104): {'title': '镇魂街
    '}>, <Hit(books/doc/154): {'title': '镇魂街'}>, <Hit(books/doc/204): {'title': '镇魂街'}>, <Hit(books/doc/254): {'title': '镇魂街'}>,
    <Hit(books/doc/304): {'title': '镇魂街'}>, <Hit(books/doc/354): {'title': '镇魂街'}>, <Hit(books/doc/404): {'title': '镇魂街'}>, <Him
    t(books/doc/454): {'title': '镇魂街'}>]>
    >>>
