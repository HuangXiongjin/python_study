"""__author__ = YuTing"""
import json


def get_all_user():
    with open('files/userinfo', encoding='utf-8') as f:
         # f.read()   # '{}'
        return json.loads(f.read())
        # return json.load(f)


def register():
    """注册"""
    # 输入账号
    while True:
        username = input('请输入账号(3-6位):')
        if 3 <= len(username) <= 6:
            break

    # 输入密码
    while True:
        password = input('请输入密码(6-12位):')
        if 6 <= len(password) <= 12:
            break

    # 拿到之前注册过的所有的账号
    # {"aaa":"123456"}
    all_user = get_all_user()
    # 判断当前账号之前是否注册过
    if username in all_user:
        print('注册失败！该账号已经注册过！')
        return

    # 注册成功后要保存账号信息
    # {"aaa":"123456", "bbb": "123456"}
    all_user[username] = password
    with open('files/userinfo', 'w', encoding='utf-8') as f:
        f.write(json.dumps(all_user))
    print('注册成功!')


def login():
    username = input('请输入账号:')
    password = input('请输入密码:')
    all_user = get_all_user()

    # 判断是否注册过
    if username not in all_user:
        print('登录失败!该账号没有注册!')
        return

    # 判断密码是否正确
    if all_user[username] != password:
        print('登录失败!密码错误!')
        return

    print('登录成功!')


def main_page():
    """主页"""
    with open('files/page', encoding='utf-8') as f:
        page = f.read()

    while True:
        # 显示主页面
        print(page)
        # 给出选择
        value = input('请选择(lanlianhua.txt-3):')
        if value == 'lanlianhua.txt':
            # print('登录')
            login()
        elif value == '2':
            # print('注册')
            register()
        elif value == '3':
            print('退出成功!')
            break
        else:
            print('输入有误!')



main_page()