"""---author==hxj---"""
# dict1 = [{'name': '压缩', '年龄': 90, '成绩': 15000, '电话': 110, '性别': '男'}]
# student_info = [
#         {'name': '压缩', '年龄': 90, '成绩': 98, '电话': '100', '性别': '**'},
#         {'name': '盖伦', '年龄': 17, '成绩': 100, '电话': '110', '性别': '男'},
#         {'name': '剑圣', '年龄': 99, '成绩': 77, '电话': '111', '性别': '男'},
#         {'name': '女警', '年龄': 16, '成绩': 59, '电话': '208', '性别': '女'},
#         {'name': '妖姬', '年龄': 11, '成绩': 75, '电话': '210', '性别': '女'},
#         {'name': '蛇女', '年龄': 88, '成绩': 44, '电话': '220', '性别': '女'}
# ]
#
# # print(student_info[4])
# num1 = 0
# num2 = 0
# max_grade = 0
# count = 0
# for student in student_info:
#     if int(student['电话']) % 10 == 8:
#         print("手机尾号是8的学生是：", student['name'])
#     if student['成绩'] < 60:
#         num1 += 1
#         print(student['name'], student['成绩'])
#     if student['年龄'] < 18:
#         num2 += 1
#     if student['成绩'] > max_grade:
#         max_grade = student['成绩']
#         max_name = student['name']
#     if student['性别'] != '男' and student['性别'] != '女':
#         student_info.remove(student)
# print(student_info)
# print("最大成绩为：", max_grade, max_name)
# print("不及格的学生个数有:%d个" % num1)
# print("未成年的学生个数有:%d个" % num2)

# chinese = ['小明', '小李', '小赵', '小红', '小花', '小黄']
# english = ['小李', '小赵', '小红', '小花', '小王']
# math = ['小明', '小李', '小赵', '小王']
# set1 = set(chinese)
# set2 = set(english)
# set3 = set(math)
# sum_student = set1 | set2 | set3
# sum1 = set1 - set2 - set3
# sum2 = (set1 - set2 - set3) ^ (set2 - set3 - set1) ^ (set3 - set2 - set1)
# sum3 = set1 & set2 & set3
# sum4 = sum_student - sum2 - sum3
# print("选课学生总共有%d人." % len(sum_student))
# print("只选了第一个学科的人的数量和对应的名字:", len(sum1), ''.join(list(sum1)))
# print("只选了一门学科的学生的数量和对应的名字:", len(sum2), ''.join(sum2))
# print("只选了两门学科的学生的数量和对应的名字:", len(sum4), ' '.join(sum4))
# print("选了三门课程的学生数量和对应的名字：", ' '.join(sum3))
# student = {'name': '小明', 'age': 18, 'gender': '男'}
# print(student.items())
# print(student.values(), student.keys())
student_info = [
        {'name': '压缩', '年龄': 90, '成绩': 98, '电话': '100', '性别': '**'},
        {'name': '盖伦', '年龄': 17, '成绩': 100, '电话': '110', '性别': '男'},
        {'name': '剑圣', '年龄': 99, '成绩': 77, '电话': '111', '性别': '男'},
        {'name': '女警', '年龄': 16, '成绩': 59, '电话': '208', '性别': '女'},
        {'name': '妖姬', '年龄': 11, '成绩': 75, '电话': '210', '性别': '女'},
        {'name': '蛇女', '年龄': 88, '成绩': 44, '电话': '220', '性别': '女'}
]

scores = []
new_student_info = []
for i in student_info:
    scores.append(i['成绩'])
print(scores)
length = len(scores)
for x in range(len(scores)-1):
    for y in range(x+1, len(scores)):
        if scores[x] < scores[y]:
            scores[x], scores[y] = scores[y], scores[x]

for z in scores:
    for index in student_info:
        if index['成绩'] == z:
            new_student_info.append(index)
print(new_student_info)
