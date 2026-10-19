"""
元组可看作不可修改的列表，支持重复元素
"""
# 1.00
# t1 = (1, 'hello', True)
# print(f'{type(t1)},{t1}')
# t2 = ('hello',)
# print(f'{type(t2)},{t2}')

# 2.00
# t1 = ((1, 2, 3), (4, 5, 6))
# for element in t1:
#     print(element)
#     for ele1 in element:
#         print(ele1)

# 3.00
# t1 = (1, 2, [3, 4])
# t1[2][1] = 5
# print(t1)