"""---author==hxj"""
# 1.continue
"""
continue是只能出现在循环体中的关键字；当执行循环体的时候遇到continue，
当次循环结束，执行进入下次循环的判断


"""
sum1 = 0
num = 0
while num < 100:
    num += 1
    if num % 7 == 0:
        continue
    sum1 += num
print(sum1)

# 2.break
"""
只能用在循环体中的关键字;执行循环体的时候遇到break,整个循环直接结束
"""
# for x in range(10):
#     print(x)
#     print("====")
#     break
#     print("+++")

sum1 = 0
num = 1
while True:
    sum1 += num
    if sum1 > 100000:
        print(num-1)
        break
    num += 1

# 3. else
"""
for 变量 in 序列：
    循环体
else；
    代码段
    
while 条件语句：
    循环体
else:
    代码段

执行过程：如果循环自然结束，else后面的代码段会执行；
        如果循环因为是遇到break而结束，else后面的代码段不会执行
"""
for x in range(4):
    print("1")
else:
    print("2")
print("3")

for x in range(4):
    print("11")
    break
else:
    print("22")
print("33")