# 1.00
# my_list = [1, 2, 3]
# my_tuple = (1, 2, 3)
# my_str = 'itheima'
# print(max(my_list))
# print(max(my_tuple))
# print(max(my_str))
# print(min(my_list))
# print(min(my_tuple))
# print(min(my_str))

# 2.00 类型转换
# list()
# set()
# str()
# tuple()

# 3.00 sorted(容器，[reserve=False]) False表示正序排列  此外，sorted函数有返回值，返回列表类型
# my_list = [3, 1, 2, 5, 7, 6, 9]
# my_str = 'adhjguyrucvbkj'
# print(sorted(my_list,reverse=False))
# print(sorted(my_str))
# print(result)

# 4.00 .sort()方法对列表排序
my_list = [["a", 30], ["b", 55], ["c", 70]]
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)