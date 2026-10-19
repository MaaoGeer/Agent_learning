"""
    Python闭包特性
        闭包使用的变量难以被错误修改调用
        无需定义全局变量即可持续使用
"""


# 简单闭包
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner  # 返回内部函数


fn1 = outer("黑马")  # inner调用的变量outer无法访问，全局变量无法修改
fn1("大家好")


# 使用nonlocal关键字修改外部函数的值
def outer1(num1):
    def inner1(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner1


fn1 = outer1(10)
fn1(10)
fn1(10)


# 使用闭包实现ATM案例
def account_creat(initial_amount: int):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款：{num},账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款：{num},账户余额：{initial_amount}")

    return atm


account1 = account_creat(100)
account1(200)
account1(100, False)
