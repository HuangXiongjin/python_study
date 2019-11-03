"""__author__ = 余婷"""
import fileManager

"""
数据结构的设计:
1. 账号和学生需要对应起来
2. 学号依次增加，一个学号只能用一次

所有学生: 一个列表中有多个字典
方案一:
{
用户名1: {
        'num': 3,
        'all_student': [
            {'name':姓名, 'age': 年龄, 'tel': 电话, 'study_id': 学号},
            {'name':姓名, 'age': 年龄, 'tel': 电话, 'study_id': 学号},
            {'name':姓名, 'age': 年龄, 'tel': 电话, 'study_id': 学号}
         ]
 },
 
用户名2:{ 
        'num': 0,
        'all_student':[
        
            ]
    }
}

一个json文件，保存一个字典; all_info.json

方案二：
一个账号对应一个json文件, 账号名就是文件文件名，账号中内容:
{
        'num': 3,
        'all_student': [
            {'name':姓名, 'age': 年龄, 'tel': 电话, 'study_id': 学号},
            {'name':姓名, 'age': 年龄, 'tel': 电话, 'study_id': 学号},
            {'name':姓名, 'age': 年龄, 'tel': 电话, 'study_id': 学号}
         ]
 }


"""

# 保存当前登录成功的用户名
current_user = ''

# =================获取用户信息================
def get_user_info():
    """
    获取当前用户的信息
    :return: 当前用户的所有学生，当前用户已经添加过的学生数量
    """
    user_dict = fileManager.json_read('files/%s.json' % current_user)
    if not user_dict:
        return [], 0

    return user_dict['all_student'], user_dict['num']


# =================添加学生================
def add_student():
    """添加学生"""

    # 获取当前账号数据
    all_student, num = get_user_info()
    while True:
        # 1.输入学生信息
        name = input('请输入学生的姓名:')
        age = int(input('请输入学生的年龄:'))
        tel = input('请输入学生的电话:')
        # 2.生成学号
        num += 1
        study_id = 'stu' + str(num).zfill(3)
        # 3.创建学生
        stu = {'name': name, 'age': age, 'tel': tel, 'study_id': study_id}
        # 添加学生
        all_student.append(stu)

        # 4.更新文件
        fileManager.json_write({'num': num, 'all_student': all_student}, 'files/%s.json' % current_user)
        print('添加成功!')

        # 5.给出选择
        print('1.继续\n2.返回')
        value = input('请选择(1~2):')
        if value == '2':
            break


# ===========================查看学生============================
def show_student(stu):
    return '学号:%s 名字:%s 年龄:%s ☎️:%s' % (stu['study_id'], stu['name'], stu['age'], stu['tel'])


def find_all():
    """查看所有学生"""
    all_student, num = get_user_info()

    if not all_student:
        print('当前账号没有被管理的学生!')
        return

    for stu in all_student:
        print(show_student(stu))


def find_with_name():
    """按姓名查找学生"""
    all_student, num = get_user_info()
    if not all_student:
        print('当前账号没有被管理的学生!')
        return
    name = input('输入姓名:')

    flag = False   # 保存是否有该学生， 默认没有
    for stu in all_student:
        if stu['name'] == name:
            print(show_student(stu))
            flag = True   # 有该学生

    if not flag:
        print('没有该学生!')


def find_width_id():
    """按学号查找"""
    pass


def check_student():
    """查看学生"""
    print('1.查看所有学生\n2.按姓名查找\n3.按学号查找\n其他:返回')
    value = input('请选择:')
    if value == '1':
        # print('查看所有')
        find_all()
    elif value == '2':
        # print('按姓名找')
        find_with_name()
    elif value == '3':
        # print('按学号找')
        find_width_id()
    else:
        return


# =======================删除学生==========================
def del_with_name():
    del_name = input('请输入学生名字:')
    all_student, num = get_user_info()

    # 找到和删除的名字相同的学生
    del_students = []
    for stu in all_student:
        if stu['name'] == del_name:
            del_students.append(stu)

    if not del_students:
        print('没有该学生!')
        return

    index = 0
    for stu in del_students:
        print(index, show_student(stu))
        index += 1

    value = input('请输入需要删除的学生对应的编号, 输入q表示返回:')
    if value == 'q':
        return

    # 根据标号找到对应的学生
    del_stu = del_students[int(value)]
    # 删除学生
    all_student.remove(del_stu)
    # 更新文件
    fileManager.json_write({'num': num, 'all_student': all_student}, 'files/%s.json' % current_user)
    print('删除成功！')


def del_student():
    """删除学生"""
    print('1.按姓名删除\n2.按学号删除\n其他:返回')
    value = input('请选择:')
    if value == '1':
        # print('姓名删')
        del_with_name()
    elif value == '2':
        print('学号删')
    else:
        return


# ====================显示主页面===========================
def show_student_manager_page():
    """显示管理页面"""
    student_page = fileManager.text_read('./files/student_page.txt')
    while True:
        # 打印页面
        print(student_page % current_user)
        # 给出选择
        value = input('请选择(1-5):')
        # 根据选择执行不同的功能
        if value == '1':
            # print('添加学生')
            add_student()
        elif value == '2':
            # print('查看学生')
            check_student()

        elif value == '3':
            print('修改学生')
        elif value == '4':
            # print('删除学生')
            del_student()
        elif value == '5':
            # 返回
            return
        else:
            print('输入有误!')

