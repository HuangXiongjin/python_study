"""---author==hxj---"""
# import random
# random_num = random.randint(0, 100)
# print(random_num)
# while True:
#     num = int(input("请输入数字："))
#     if num > random_num:
#         print("数字大了！")
#     if num < random_num:
#         print("数字小了！")
#     if num == random_num:
#         print("恭喜你猜对了！！")
#         break


def menu():
    print("*****学生管理系统*******")
    print("*****1.添加学生信息*****")
    print("*****2.查看学生信息*****")
    print("*****3.修改学生信息*****")
    print("*****4.删除学生信息******")
    print("*****5.返回******")


def student_info():
    student_list = []
    while True:
        name = input("名字：")
        if name == ' ':
            break
        else:
            age = input("年龄：")
            no = input("学号：")
        info = {"姓名": name, "年龄": age, "学号": no}
        student_list.append(info)
    print("输入完毕！")
    return student_list


def show_student_info(student_info):
    print("名字     ",  "年龄     ", "学号     ")
    for info in student_info:
        print(info[name], )