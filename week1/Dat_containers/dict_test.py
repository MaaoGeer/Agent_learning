"""
    字典
    key：value
"""
#1.00
# my_dict = {'yyc': 'sx','lxl': 'fj', 'lyh': 'hn' }
# my_dict1 = {}
# my_dict2 = dict()
# print(f'字典1的内容是{my_dict},类型是{type(my_dict)}')
# print(f'字典2的内容是{my_dict1},类型是{type(my_dict1)}')
# print(f'字典3的内容是{my_dict2},类型是{type(my_dict2)}')

#2.00
# my_dict = {'yyc': 'sx', 'lxl': 'fj', 'lyh': 'hn'}
# print(my_dict[input('enter:')])

# 3.00
# my_dict = {
#     '王力宏': {'语文': 77, '数学': 66, '英语': 33},
#     '周杰伦': {'语文': 88, '数学': 86, '英语': 55},
#     '林俊杰': {'语文': 99, '数学': 96, '英语': 66}
# }
# print(my_dict[input('请输入想要查询的学生姓名：')][input('请输入想要查询的科目：')])

#4.00 增加或者更新元素
my_dict = {'王力宏': 77, '周杰伦': 88, '林俊杰': 99}
my_dict['薛之谦'] = 66
print(my_dict)
my_dict['王力宏'] = 76
print(my_dict)

#5.00 删除元素 pop(key)
# my_dict = {'王力宏': 77, '周杰伦': 88, '林俊杰': 99}
# score = my_dict.pop('王力宏')
# print(my_dict)

#6.00 清空字典
# my_dict = {'王力宏': 77, '周杰伦': 88, '林俊杰': 99}
# my_dict.clear()
# print(my_dict)

#7.00 获取全部key  keys()
# my_dict = {'王力宏': 77, '周杰伦': 88, '林俊杰': 99}
# keys = my_dict.keys()
# print(keys)

#8.00 遍历
# my_dict = {'王力宏': 77, '周杰伦': 88, '林俊杰': 99}
# keys = my_dict.keys()
# for key in keys: #for key in my_dict: 这个循环取出的每一个元素都是字典的key
#     print(f'字典的key是：{key}')
#     print(f'字典的value是：{my_dict[key]}')
#     print()

#9.00
 