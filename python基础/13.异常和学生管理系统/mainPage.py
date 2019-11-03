"""__author__ = 余婷"""
import fileManager
import studentManager

"""
账号密码的数据存储: 保存到本地文件中；所有的账号保存在一个字典中，一个账号对应一个键值对，
                 账号作为key，密码作为value
                 
                 文件采用json文件， 文件名:admins.json
"""

# 全局变量
admin_file = './files/admins.json'


def register():
    """注册"""
    # 1.输入账号
    while True:
        user_name = input('请输入账号(3~6位):')
        if 3 <= len(user_name) <= 6:
            break
        else:
            print('输入有误,账号必须是3~6位!')

    # 2.输入密码
    while True:
        password = input('请输入密码(6~12位):')
        if 6 <= len(password) <= 12:
            break
        else:
            print('输入有误，密码必须是6~12位!')

    # 3.对账号和密码进行保存
    # 获取原来注册的账号信息
    admins = fileManager.json_read(admin_file)
    # 判断当前账号之前是否已经注册过
    if user_name in admins:
        print('注册失败!该账号已经注册过!')
        return
    # 添加账号
    admins[user_name] = password
    # 更新文件
    fileManager.json_write(admins, admin_file)
    print('注册成功!')


def login():
    """登录"""
    # 1.输入账号和密码
    username = input('请输入账号:')
    password = input('请输入密码:')

    # 2.判断账号是否已经注册过
    admins = fileManager.json_read(admin_file)
    if username in admins:
        if admins[username] == password:
            print('登录成功!')
            # 进入学生管理页面
            studentManager.current_user = username
            studentManager.show_student_manager_page()
        else:
            print('登录失败!密码错误!')
    else:
        print('登录失败!该账号没有注册!')




def show_home_page():
    """显示主页"""
    # 获取主页面的内容
    home_page = fileManager.text_read('./files/home_page.txt')

    while True:
        # 打印主页面
        print(home_page)
        # 给出选择
        value = input('请选择(1-3):')
        if value == '1':
            # print('登录')
            login()
        elif value == '2':
            # print('注册')
            register()
        elif value == '3':
            break   # return\exit()
        else:
            print('输入有误!')


if __name__ == '__main__':
    show_home_page()

