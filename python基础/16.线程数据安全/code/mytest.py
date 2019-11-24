"""---author==hxj---"""
list1 = []
for i in range(1, 7):
    for j in range(1, i+1):
        print("{}*{}={}".format(j, i, j*j), end=' ')
    print('\n')
