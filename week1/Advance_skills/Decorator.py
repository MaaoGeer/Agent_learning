"""
    装饰器其实也是闭包，其功能是 不破坏目标函数的原有代码和功能的前提下,为目标函数增加新功能
"""


# 装饰器的一种写法
# def sleep():
#     import random
#     import time
#     print("睡眠中.............")
#     time.sleep(random.randint(1, 5))
#
#
# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
#
# fn = outer(sleep)
# fn()


# 装饰器的快捷写法
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中.............")
    time.sleep(random.randint(1, 5))


sleep()
