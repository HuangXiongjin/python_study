"""---author==hxj---"""
import json


def system_menu():
    print("******欢迎来到学生管理系统******")
    print("***********1.登录**************")
    print("***********2.注册**************")
    print("***********3.退出**************")
    print("*******************************")

    choice1 = eval(input("请选择(1-3)："))
    if choice1 == 1:
        return user_login()
    elif choice1 == 2:
        return register_user()
    elif choice1 == 3:
        return system_quit()
    # else:
    #     return "输入错误！！"


def user_login():
    with open('files/admin.json', encoding='utf-8') as f:   # 读取json文件中的用户
        admin_data = json.loads(f.read())
    username = input('请输入用户名:')
    password = input('请输入密　码:')
    for n in admin_data:
        if username == n[0]['users']['user']:       # 判断用户是否正确
            while password == n['password']:      # 判断密码是否正确
                print("登陆成功！")
                return student_info()
            else:
                print('登录失败!')
                break
                return user_login()
        else:
            print('用户不存在!')


def register_user():
    with open('files/admin.json', 'r', encoding='utf-8') as f:   # 读取json文件中的用户
        admin_data = json.loads(f.read())
    username = input("请输入用户名(3-6位)：")
    while True:
        while not 3 <= len(username) <= 6:
            username = input("用户名格式不正确！\n请输入用户名(3-6位)：")
        for n in admin_data:
            if username == n['user']:
                username = input("用户名已存在！\n请输入用户名(3-6位)：")
                break
        else:
            break
    password = input("请输入密码(6~12位)：")
    while not 6 <= len(password) <= 12:
        password = input("密码格式不正确！\n请输入密码(6~12位)：")
    with open('files/admin.json', 'w', encoding='utf-8') as f:
        admin_data.append({'user': username, 'password': password})
        f.write(json.dumps(admin_data))
        print("注册成功！")


def student_info():
    with open('./files/student_info.txt', 'r', encoding='utf-8') as f2:
        student_input = input(f2.read())
    choice = input("请选择(1-5)：")
    if choice == '1':
        return add_student()


def add_student():
    with open('files/admin.json', 'r', encoding='utf-8') as f:   # 读取json文件中的用户
        admin_data = json.loads(f.read())
    print(admin_data[0]['students'][0])
    student_name = input("请输入学生姓名：")
    student_sno = input("学号：")
    student_sex = input("性别：")
    student_age = input("年龄：")
    student_tel = input("电话：")
    with open('files/admin.json', 'w', encoding='utf-8')as f:
        admin_data[0].append([{'name': student_name, 'sno': student_sno, 'sex': student_sex,
                             'age': student_age, 'tel': student_tel}])
        f.write(json.dumps(admin_data))
        print("添加成功！")


def system_quit():
    print("退出成功！")


system_menu()








