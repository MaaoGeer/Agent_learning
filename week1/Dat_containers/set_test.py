#集合，无序且不可重复,无序故不支持下标索引,可以修改

#1.00
# my_set = {1, 2, 2, 3, 1, 1, 5}
# print(my_set)

#2.00
# my_set = {1, 2, 2, 3, 1, 1, 5, '黑马程序员'}
# my_set.add('Python')
# my_set.add('黑马程序员')
# print(my_set)

#3.00
# my_set = {1, 2, 2, 3, 1, 1, 5, '黑马程序员'}
# my_set.remove('黑马程序员')
# print(my_set)

#4.00 pop函数随机取出一个元素
# my_set = {1, 2, 2, 3, 1, 1, 5, '杨渊超'}
# element = my_set.pop()
# print(my_set)
# print(element)

#5.00
# my_set = {1, 2, 2, 3, 1, 1, 5, '杨渊超'}
# my_set.clear()
# print(my_set)

#6.00 差集：集合1里有而集合2里没有;两种写法 1. set.difference(set1,set2) 2.set1.difference(set2)_%不会改变set1的值
# set1 = {1,2,3}
# set2 = {1,5,6}
# set3 = set1.difference(set2)
# print(set3)

#7.00 在set1内部删除和set2相同的元素
# set1 = {1,2,3}
# set2 = {1,5,6}
# set.difference_update(set1,set2)
# print(set1)
# print(set2)

#8.00  取并集
# set1 = {1, 2, 3}
# set2 = {1, 5, 6}
# ste3 = set1.union(set2)
# print(ste3)

#9.00
# set1 = {1, 2, 3, 4, 5}
# num = len(set1)
# print(f'集合内有{num}个元素')

#10.00 集合的遍历 //集合不支持下标索引
# set1 = {1, 2, 3, 4, 5}
# for element in set1:
#     print(f'集合的元素有：{element}')
# print('---end---')