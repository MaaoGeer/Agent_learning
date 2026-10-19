"""
    设计模式
"""
# 单例模式  保证一个类只有一个示例，并提供一个全局访问点
from test_strtool import str_tool

s1 = str_tool
s2 = str_tool
print(id(s1))
print(id(s1))


# 工厂模式  需要大量创建一个类的示例，从原生的使用类的构造去创建对象的形式
class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Factory:
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()


factory = Factory()
worker = factory.get_person('w')
student = factory.get_person('s')
teacher = factory.get_person('t')
