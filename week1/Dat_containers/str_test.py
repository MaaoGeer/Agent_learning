#不可修改，支持重复元素，有序
# 1.00
# my_str = 'captaincy'
# value = my_str[1]
# value2 = my_str[-1]
# print(value,value2)

# 2.00
# my_str = 'itheima and itcast'
# index = my_str.index(input('请输入需要查找的字符：'))  # index函数统计起始元素的下标
# print(index)

# 3.00
# my_str = 'itheima and itcast'
# new_my_str = my_str.replace(input('请输入需要修改的字符：'),input('请输入修改后的字符：'))
# print(new_my_str)

# 4.00
# my_str = 'itheima and itcast'
# my_str_list = my_str.split(input('请输入分隔字符：'))       # split函数处理完成后会返回列表类型
# print(my_str_list)

# 5.00   strip函数将输入的字符串拆分成单个字符进行操作
my_str = '12itheima and itcast21'
new_my_str = my_str.strip(input('请输入需要删除的字符：')) # 不输入则默认为空格或换行符，删除字符串开头或结尾的指定字符
print(new_my_str)


# 6.00
# my_str = 'itheima and itcast'
# count = my_str.count('it') # count函数将输入字符串看作一个整体
# print(count)

#7.00
"""
    字符串比较
    从前到后比
    当首次出现不同的字符
        大的字符串就大
"""
