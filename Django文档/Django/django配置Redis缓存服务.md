#### settings中配置，其中"default"只是默认缓存的名称，可以自定义

```
CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': [
                'redis://120.77.222.217:6379/0',
            ],
            'KEY_PREFIX': '生成key的前缀',  # 这里随便写
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                'CONNECTION_POOL_KWARGS': {
                    'max_connections': 256,
                },
                'PASSWORD': '密码',
            }
        },
        "my_redis": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'CONNECTION_POOL_KWARGS': {
                    'max_connections': 256,
                },
            'PASSWORD': '123456',
        }
     },
    }
# 使用引擎
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 设置过期时间86400秒
SESSION_COOKIE_AGE = 86400
```

#### 使用方法

##### 第一种方法存储为String类型

```
from django.core.cache import cache  # cache是使用默认缓存的变量'default'

def login(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = uuid.uuid4().hex
    user = User.objects.get(username=request.data['username'])
    # cache只能存储为string类型的数据
    cache.set(token, user.id, timeout=1000)  # 1000秒
    res = {
    'token': token
    }
    return Response(res)
```

##### 第二种方法指定使用的缓存变量

```
from django.core.cache import caches

def login(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = uuid.uuid4().hex
    user = User.objects.get(username=request.data['username'])
    # 指定使用的缓存配置，存储类型string
    caches['my_redis'].set(token, user.id, timeout=1000)  # 1000秒
    res = {
    'token': token
    }
    return Response(res)
```

##### 第三种方法，获取redis连接对象

```
from django_redis import get_redis_connection 

def login(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = uuid.uuid4().hex
    user = User.objects.get(username=request.data['username'])
    redis = get_redis_connection(alias='my_redis')  # 获取redis连接对象,相当于redis_cli工具
    redis.set(token, user.id)  # 存储为String类型
    redis.hset('user_token', user.id, token)    # 存储为hash的类型
    res = {
    'token': token
    }
    return Response(res)
```


#### 注意，存储类型不一样取值的时候也不一样，下面是使用的String类型

```
from rest_framework.authentication import BaseAuthentication
from django.core.cache import cache
from user.models import User
from utils.errors import ParamsException

class UserAuthentication(BaseAuthentication):

    def authenticate(self, request):
        path = request.path
        paths = ['/user/user/login/', '/user/user/register/']
        if path in paths:
            return None  # 注意return None
        token = request.GET.get('token')
        if not token:
            raise ParamsException({'code': 1007, 'msg': '无法访问！！'})
        user_id = cache.get(token)  # String类型
        if not user_id:
            raise ParamsException({'code': 1008, 'msg': '请先登录11'})
        user = User.objects.get(pk=user_id)
        return user, token  # 此处必须返回user, token
```

