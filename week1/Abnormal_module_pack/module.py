# 1.00
# import time    # 导入time模块,整个模块
# print('hello')
# time.sleep(5)     # 睡眠5秒
# print('你好')

# 2.00
# from time import sleep    # 导入模块中的具体函数
# print('hello')
# sleep(5)     # 睡眠5秒
# print('你好')

# 3.00
# from time import *      # *表示全部
# print('hello')
# sleep(5)     # 睡眠5秒
# print('你好')

# 4.00
# import time as t    # 使用as给模块或者函数加别名
# print('hello')
# t.sleep(5)     # 睡眠5秒
# print('你好')

# 5.00
# if __name__ == '__main__':      # 用于测试模块内的函数，若模块文件导入另一个文件执行时候，if判断为False
#     print('测试函数')

# 6.00
"""
    __all__变量
    __all__ = ['test_A']
    若直接导入整个模块，只能使用all函数里的内容
    若需要使用其他函数，可以使用导入具体函数的方法
"""
