# 1.00 多返回值函数
# def test_return():
#     return  1,'hello'
# x, y = test_return()
# print(x)
# print(y)

# 2.00 函数的多种传入参数方式
# def use_info(name, age, gender='man'):
#     print(f'您的名字是：{name}，年龄是{age}，性别是：{gender}')
# # 位置参数
# use_info('yyc', 17,'man')
# # 关键字参数
# # 这样传入，需要把位置参数放在前边并且匹配参数顺序
# use_info('yyc', gender='man', age=17)
# # 缺省参数（默认值）
# use_info('yyc', 17)
# use_info('lxl', 18, 'woman')

# 3.00 不定长参数（不确定使用多少参数）
# # 位置参数，传入元素存储为元组
# def use_info(*args):
#     print(args)
# use_info('Tom')
# use_info('Jack', 18)
#
# #关键字参数，传入参数存储为字典
# def use_info1(**kwargs):
#     print(kwargs)
# use_info1(name = 'yyc',age = 17, gender = 'man')

# 4.00 传入函数,实际上是计算逻辑
# def test_func(addition):
#     result = addition(1,2)
#     print(type(addition))
#     print(result)
# def addition(x,y):
#     return x+y
# test_func(addition)

# 5.00 lambda匿名函数:只能临时使用一次
# def test_func(addition):
#     result = addition(1,2)
#     print(result)
# test_func(lambda x,y: x+y)
