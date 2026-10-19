"""
    封装:
        成员变量：
            私有成员变量：变量名以 __ 开头
        成员方法：
            私有成员方法：方法名以 __ 开头
"""
import json
import random
from typing import Union


# 私有变量和私有方法不能被类对象直接使用，但可以被类中的其他成员使用
class Phone:
    __current_v = 0.5

    def __keep_single_core(self):
        print("CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_v >= 1:
            print("5g通话已开启")
        else:
            print("手机电量太低")
            self.__keep_single_core()


phone = Phone()
phone.call_by_5g()

"""
    继承：
        单继承：
            class 类名(父类名):
                新增类内容(pass)
        多继承：(继承优先级：左边到右边)
            class 类名(父类1,父类2,父类3....):
                新增类内容(pass)
"""


# 基础语法
class Phone:
    IMET = None
    produce = "YLSD"

    def call_by_4g(self):
        print("4G通话")


class Phone2023(Phone):
    face_id = None

    def call_by_5g(self):
        print("5G通话")


phone = Phone2023()
print(phone.produce)
phone.call_by_4g()

# 复写父类成员和调用
class Phone:
    IMET = None
    produce = "YLSD"

    def call_by_5g(self):
        print("使用5G通话")


class Phone2023(Phone):
    face_id = None
    produce = "ITHM"        # 复写父类属性

    def call_by_5g(self):       # 复写父类方法
        print("开起CPU单核模式,确保通话过程省电")

        # 方式1 调用父类成员和方法
        # print(f"父类的厂商是：{Phone.produce}")
        # Phone.call_by_5g(self)

        # 方式2 调用父类成员和方法
        print(f"父类的厂商是：{super().produce}")
        super().call_by_5g()

        print("关闭CPU单核模式,确保性能")


phone = Phone2023()
print(phone.produce)
phone.call_by_5g()


"""
    类型注解
        变量的类型注解：一般无法直接看出变量类型时会添加变量的类型注解
        函数(方法)的类型注解
        Union类型
"""
# 基础数据类型注解
# var1: int = 10
# var2: float = 3.1415
# var3: bool = True
# var4: str = "heimab"


# 类对象类型注解
# class Student:
#     pass
# stu: Student = Student()

# 基础容器类型注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {"itheima": 666}

# 基础容器类型详细注解
# my_list1: list[int] = [1, 2, 3]
# my_tuple2: tuple[int, str, bool] = (1, "itheima", True)     # 必须将每一个元素类型都写出
# my_dict3: dict[str, int] = {"itheima": 666}     # [key, value]

# 在注释中注解
# var5 = random.randint(1, 10)    # type: int
# var6 = json.load('"{"name": "Jack"}"')                # type: dict[str, str]

# 函数(方法)的类型注解
# def add(x: int, y: int) -> int:     # (x: int)形参类型注解, ->返回值注解
#     return x+y
# add()

# Union类型注解
# my_list: list[Union[str, int]] = [1, 2, "itheima", "itcast"]
# my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}
#
# def add(data: Union[str, int]) -> Union[str, int]:      # 表示传入str或者int,返回str或者int
#     pass


"""
    多态
        指多种状态，即完成某个行为时，使用不同的的对象会得到不同的状态
"""


# 抽象类，也叫接口，好比一个标准，用于顶层设计
class Animal:
    """父类Animal的speck方法是空实现，这种设计的含义：
        1.父类用来确定有那些方法 2.具体方法的实现又子类自行决定
    """

    def speck(self):  # 抽象方法
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")
