"""---author==hxj---"""


"""
1.

（1）编写一个矩形类Rect，包含：矩形的宽width；矩形的高height。要求创建对象的时候必须给width和height传值
    两个方法：求矩形面积的方法area()，求矩形周长的方法perimeter()
（2）通过继承Rect类编写一个具有确定位置的矩形类PlainRect，其确定位置用矩形的左上角坐标来标识，包含：
    添加两个属性：矩形左上角坐标start_x和start_y。要求创建PlainRect对象的时候width和height必须赋值，
    start_x和start_y可以赋值可以不赋值。
    添加一个方法：判断某个点是否在矩形内部的方法is_inside()。如在矩形内，返回True, 否则，返回False。
"""


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return (self.width + self.height) * 2
#
#
# class PlainRect(Rect):
#     def __init__(self, , width, height, start_x, start_y):
#         super.__init__()
#         self.width = width
#         self.height = height
#         self.start_x = start_x
#         self.start_y = start_y
#
#     def is_inside(self):

# 汽车类
"""
建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例。
至少要求 汽车能够加速 减速 停车。 再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD属性，并且
重新实现方法覆盖加速、减速的方法
"""


# class Auto:
#     def __init__(self, tyre, color, weight, speed):
#         self.tyre = tyre
#         self.color = color
#         self.weight = weight
#         self.speed = speed
#
#     def speed_up(self, value):
#         self.speed += value
#         print("您的当前车速为 {}".format(self.speed))
#         if self.speed >= 100:
#             print('您的车速过快，请减速慢行！')
#             raise ValueError
#
#     def speed_down(self, value):
#         self.speed -= value
#         if self.speed < 0:
#             print("您当前的车速为0已停车，下车请注意安全！")
#         elif self.speed < 100:
#             print("您的当前车速为 {}".format(self.speed))
#             print("您还可以继续加速！")
#
#
# a1 = Auto(12, 'white', '10吨', speed=100)
# print(a1.tyre, a1.color, a1.weight, a1.speed)
# a1.speed_down(70)
#
#
# class CarAuto(Auto):
#     def __init__(self, tyre, color, weight,  air_condition, cd, speed):
#         super().__init__(tyre, color, weight, speed)
#         self.air_condition = air_condition
#         self.cd = cd,
#
#     def speed_up(self, value):
#         self.speed += value
#
#         if self.speed >= 120:
#             print("您的当前车速为 {}".format(self.speed))
#             print('您的车速过快，请减速慢行！')
#
#     def speed_down(self, value):
#         self.speed -= value
#         if self.speed < 0:
#             print("您当前的车速为0已停车，下车请注意安全！")
#         elif self.speed < 120:
#             print("您的当前车速为 {}".format(self.speed))
#             print("您还可以继续加速！")
#
#
# c1 = CarAuto(4, 'white', '1.5吨', air_condition='media', cd='静悄悄', speed=80)
# print(c1.tyre, c1.color, c1.weight, c1.air_condition, c1.cd, c1.speed)
# c1.speed_up(80)
# c1.speed_down(110)

# 2.统计Person个数
"""
class Person:
    count = 0

    def __init__(self):
        self.name = 'ming'
        Person.count += 1


p1 = Person()
p2 = Person()
p3 = p2
print(Person.count)
"""

# 3.创建一个动物类，拥有属性：性别、年龄、颜色、类型 ，
# 要求打印这个类的对象的时候以'/XXX的对象: 性别-? 年龄-? 颜色-? 类型-?/' 的形式来打印
"""

class Animal:
    def __init__(self, name, sex, age, color, species):
        self.name = name
        self.sex = sex
        self.age = age
        self.color = color
        self.species = species

    def __repr__(self):
        print("{}的对象: 名称-{} 性别-{} 年龄-{} 颜色-{} 类型-{}".format(self.__class__,
        self.name, self.sex, self.age, self.color, self.species))


a1 = Animal('tiger', 'male', 8, 'brown', 'feline')
a1.__repr__()

"""

# 4. 写一个圆类， 拥有属性半径、面积和周长；要求获取面积和周长的时候的时候可以根据半径的改属性不能赋值
# 值把对应的值取到。但是给面积和周长赋值的时候，程序直接崩溃，并且提示
"""
from math import pi


class WriteError(Exception):
    def __str__(self):
        return '该属性不能赋值'


class Circle:
    def __init__(self, radius):
        if not (isinstance(radius, int) or (isinstance(radius, float))):
            raise ValueError
        self.radius = radius
        self._area = 0
        self._perimeter = 0

    @property
    def area(self):
        return pi*self.radius**2

    @area.setter
    def area(self, value):
        raise WriteError

    @property
    def perimeter(self):
        return 2*pi*self.radius

    @perimeter.setter
    def perimeter(self, value):

        raise WriteError


c1 = Circle(4)
print(c1.area, c1.perimeter)
c1.radius = 8
print(c1.area, c1.perimeter)
c1.area = 23

"""

"""5. 写一个扑克类， 要求拥有发牌和洗牌的功能(具体的属性和其他功能自己根据实际情况发挥)"""
import random


class Poker:
    # 创建一副牌
    colors = ['♥', '♠', '♣', '♦']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    kings = [('black', '小王'), ('red', '大王')]
    pokers = []
    for color in colors:
        for num in numbers:
            pokers.append((color, num))
    pokers.extend(kings)

    def __init__(self, landowner):
        self.landowner = landowner  # 定义地主牌

    # 洗牌
    def shuffle(self):
        random.shuffle(Poker.pokers)
        return Poker.pokers

    # 发牌
    def deal(self):
        deal_pokers = iter(Poker.shuffle(self))
        # 创建玩家
        player1 = []
        player2 = []
        player3 = []
        # 拿出地主牌
        landowner_poker = [next(deal_pokers), next(deal_pokers), next(deal_pokers)]

        # 给玩家发牌
        num = 1
        for _ in range(51):
            if num == 1:
                player1.append(next(deal_pokers))
            elif num == 2:
                player2.append(next(deal_pokers))
            elif num == 3:
                player3.append(next(deal_pokers))
                num = 0
            num += 1
        # 确定地主
        if self.landowner in player1:
            player1.extend(landowner_poker)
        elif self.landowner in player2:
            player2.extend(landowner_poker)
        elif self.landowner in player3:
            player3.extend(landowner_poker)

        print(player1)
        print(player2)
        print(player3)


p1 = Poker(('black', '小王'))
p1.deal()


# class PlayCard:
#     flower_color = ['♥', '♠', '♦', '♣']
#     cards = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
#     flower_card = []
#     mode = []
#
#     for x in cards:
#         for y in flower_color:
#             flower_card.append(y + x)
#     print(flower_card)
#
#     def __init__(self, genre, num):
#         self.genre = genre
#         self.play_num = num
#
#     # 洗牌
#     def riffle(self):
#         if self.genre != '红三':
#             PlayCard.flower_card.extend(['大鬼', '小鬼'])
#         PlayCard.mode = PlayCard.flower_card * 1
#         print(PlayCard.mode)
#         # random.shuffle(PlayCard.flower_card)
#         # print(random.shuffle(PlayCard.flower_card))
#         PlayCard.flower_card = iter(PlayCard.flower_card)
#         print(next(PlayCard.flower_card))
#         print(next(PlayCard.flower_card))
#         print(next(PlayCard.flower_card))
#         print(next(PlayCard.flower_card))
#
#
# p1 = PlayCard('斗地主', 3)
# p1.riffle()

class Person:
    def __init__(self, name, gender):
        self.name = name
        self._age = 0
        self.gender = gender
        self._week = 0

    @property  # 添加getter的作用
    def week(self):
        if self._week == 0:
            return '星期天'
        elif self._week == 1:
            return '星期一'
        elif self._week == 2:
            return '星期二'
        elif self._week == 3:
            return '星期三'
        elif self._week == 4:
            return '星期四'
        elif self._week == 5:
            return '星期五'
        elif self._week == 6:
            return '星期六'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):  # 判断类型,如果不是指定的类型就报错
            raise TypeError
        self._age = value


p1 = Person('小明', '男')
# p1._week = 4
# print(p1._week)  # 4
# print(p1.week)  # 实质是在调用week方法获取返回值

# print("=========================================")
p1.age = 200
print(p1.age)
# print(p1.name, p1.age, p1.gender, p1.week)
# print(p1.week)

