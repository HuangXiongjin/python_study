"""---author==hxj---"""
import random
# python内置了一个模块random, 提供了随即操作相关的方法
# 1）random.randint(M,N) -- 产生M~N的整数(M N 都能被取到)
print(random.randint(0, 10))
# 2）random.random() -- 产生0~1的随机数(小数， 0可以取到， 1取不到)
print(random.random())

# 3）random.randrange(M,N,step) -- 产生序列range(M, N, step)中的任意一个整数
print(random.randrange(0, 100, 2))

# 4) random.choices(序列， k = N) -- 在序列中随机获取N个元素，以列表的形式返回。N默认是1
nums = [1, 3, 4, 5, 6]
print(random.choices(nums))
print(random.choices(nums, k=2))

# 5)random.shuffle(列表) -- 随机打乱列表元素的位置
nums = [1, 3, 4, 5, 6]
random.shuffle(nums)
print(nums)
