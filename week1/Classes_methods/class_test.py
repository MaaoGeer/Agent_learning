"""
    类
    class 类名称:
        类的属性：即定义在类中的变量(成员变量)
        类的行为：即定义在类中的方法(成员方法)
"""

# 类可以封装属性
# class Student:
#     name = None
#     age = None
#     address = None

# 类的定义和使用
# class Student:
#     name = None
#     age = None
#     address = None
#
#     def say_hi(self):
#         print(f"大家好，我是{self.name}")
#
#     def say_hi2(self,msg):
#         print(f"大家好，我是{self.name}，{msg}")
#
#
# stu1 = Student()
# stu1.name = "周杰伦"
# stu1.say_hi()
#
# stu2 = Student()
# stu2.name = "林俊杰"
# stu2.say_hi2("修炼爱情")

# 类和对象的关系，即面向对象的编程思路
"""
    类是设计图纸
    对象是具体物品
    基于 类 创建 对象，并使用 对象 完成具体任务
"""


# class Clock:
#     id = None
#     price = None
#
#     def ring(self):
#         import winsound
#         winsound.Beep(2000, 3000)
#
#
# clock1 = Clock()
# clock1.id = "03002"
# clock1.price = 23
# clock1.ring()

# __init__方法，即 构造方法
# class Student:
#     name = None
#     age = None
#     address = None
#
#     def __init__(self, name, age, address):     # 可以自动执行，可将传入参数自动传递给__init__方法使用
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# stu = Student("周杰伦", 44, "山西省朔州市")

# 常用内置方法(魔术方法)
# __str__方法
# class Student:
#     def __init__(self, name, age):     # 可以自动执行，可将传入参数自动传递给__init__方法使用
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Student类对象，name：{self.name}，age：{self.age}"
#
#
# stu = Student("周杰伦", 44)
# print(stu)

# __lt__ 完成对象的直接比较,比较 < 和 >
# class Student:
#     def __init__(self, name, age):     # 可以自动执行，可将传入参数自动传递给__init__方法使用
#         self.name = name
#         self.age = age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#
# stu1 = Student("zjl", 11)
# stu2 = Student("ljj", 13)
# print(stu1 < stu2)
# print(stu1 > stu2)

# __le__ 完成对象的直接比较,比较 <= 和 >=
# class Student:
#     def __init__(self, name, age):     # 可以自动执行，可将传入参数自动传递给__init__方法使用
#         self.name = name
#         self.age = age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
#
# stu1 = Student("zjl", 11)
# stu2 = Student("ljj", 13)
# print(stu1 <= stu2)
# print(stu1 >= stu2)

# __eq__ 比较运算符实现方式(==)
# class Student:
#     def __init__(self, name, age):     # 可以自动执行，可将传入参数自动传递给__init__方法使用
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#
# stu1 = Student("zjl", 11)
# stu2 = Student("ljj", 13)
# print(stu1 == stu2)
