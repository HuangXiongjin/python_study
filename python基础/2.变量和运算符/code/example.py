"""---author==hxj"""
summation = 0
num = 1
while num <= 100:
    if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
        summation += 1
    num += 1
print(summation)
