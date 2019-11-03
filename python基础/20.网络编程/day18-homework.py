"""---author==hxj---"""
# for x in range(101, 200):
#     for y in range(2, x):
#         if x % 2 == 0:
#             break
# print(x)
fz = 2
fm = 1
for _ in range(20-1):
    a = fz
    fz = fz + fm
    fm = a
print(fz, '/', fm)

count = 1
fz = 2
fm = 1
while count < 20:
    f = fz
    fz = fz + fm
    fm = f
    count += 1
print(fz, '/', fm)










