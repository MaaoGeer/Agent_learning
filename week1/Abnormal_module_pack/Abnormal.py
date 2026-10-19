# 1.00 对可能出现的异常进行处理，提前捕获
# # 基本捕获语法
# try:
#     f = open('E:\\pytest\\pythonProject\\file2.txt', 'r', encoding='UTF-8')
# except:           # 捕获全部异常，或者Exception
#     print('出现异常，文件不存在')
#     f = open('E:\\pytest\\pythonProject\\file2.txt', 'w', encoding='UTF-8')
#
# # 捕获指定异常
# try:
#     print(name)
# except NameError as e:         # e中存储异常具体信息
#     print('出现了变量未定义的异常')
#     print(e)
#
# # 捕获多个异常
# try:
#     print(1)
# except (NameError,ZeroDivisionError) as e:      # 有异常的情况执行
#     print('出现了变量未定义或者除0异常')
# else:           # 没有异常的情况，不必须
#     print('未出现异常')
# finally:        # 一定执行的语句
#     print('-*-end-*-')

# 2.00 异常的传递
def func1():
    print('func1 开始执行')
    num = 1/0
    print('func1 结束执行')

def func2():
    print('func2 开始执行')
    func1()
    print('func2 结束执行')

def main():
    try:
        func2()
    except Exception as e:
        print(f'出现异常了，异常的信息是：{e}')

main()
