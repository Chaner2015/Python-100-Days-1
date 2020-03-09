"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

Version: 0.1
Author: 骆昊
"""
from random import randint
from time import sleep
from math import sqrt


def games():
    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')


class Student(object):

    __nickname: str = '2333'

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age: int = 18):
        self.name = name
        self.age = age
        if age >= 18:
            self.__nickname = 'sss'

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

    def nickname(self):
        return self.__nickname


class Clock(object):
    """数字时钟"""
    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


class Point(object):
    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def move_point():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == "__main__":
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('ash')
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()
    print(stu1.nickname())
    # print(type(stu1.nickname()))

    # clock = Clock(23, 59, 58)
    # while True:
    #     print(clock.show())
    #     sleep(1)
    #     clock.run()
    move_point()
"""
面向对象进阶

在前面的章节我们已经了解了面向对象的入门知识，知道了如何定义类，如何创建对象以及如何给对象发消息。
为了能够更好的使用面向对象编程思想进行程序开发，我们还需要对Python中的面向对象编程进行更为深入的了解。
"""

# @property装饰器
# 之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
# 但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
# 我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，
# 那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
# 如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。

# __slots__魔法
# 我们讲到这里，不知道大家是否已经意识到，Python是一门动态语言。
# 通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。
# 但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
# 需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。


class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age: int = 18):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age: int):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


person = Person('王大锤', 12)
person.play()
person.age = 22
person.play()
