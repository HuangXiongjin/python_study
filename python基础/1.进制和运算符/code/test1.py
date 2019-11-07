"""---author==hxj---"""
num1 = 0b1011
print("num1=", num1)

num2 = 0o34
print(num2)

num3 = 0x34
print(num3)
print(oct(num3))
print(hex(num3))
num = 123
print(num // 10 % 10)
print(num // 10)
nums = [1, 2, 3]
nums.extend([10, 20])
print(nums)
nums.extend('hello')
print(nums)
nums.extend(range(100, 105))
print(nums)
nums = [23, 89, 60, 89, 60, 1,  60, 23, 1]
nums.sort(key= lambda num: num % 10)
print(nums)
