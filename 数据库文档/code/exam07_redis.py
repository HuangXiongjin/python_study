import redis

client = redis.Redis(host='localhost',
                     port=6379,
                     )
print(client.ping())
# print(client.get('username').decode())
client.set('username', '王大锤', ex=60)  # ex: expire指定过期时间（秒）
client.set('gender', 'male')
# client.set('username', 'wangdachui', ex=120)
# print(client.get('username').decode())
# print(client.ttl('username'))
client.expire('gender', 60)
client.hmset('stu:1001', {'name': '张三', 'age': 18})

# for value in client.hvals('stu:1001'):
#     print(value.decode())
# client.rpush('list1', 10, 20, 30, 40, 50, 60)
# for value in client.lrange('list1', 0, -1):
#     print(value.decode(), end=' ')
# print()
# client.flushall()
