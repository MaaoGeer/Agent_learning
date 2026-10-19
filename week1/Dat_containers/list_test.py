#可修改，支持重复元素，有序
#1.00
# mylist = ['it', 'is', 'a', 'pig']
# ele = input('请输入需要查询的元素：')
# index = mylist.index(ele)
# print(index)
#

#2.00
# mylist = [1, 2, 3, [1, 2, 3]]
# print(mylist)
# mylist[3][0]=3
# print(mylist)

#3.00
# mylist = [1, 2, 3]
# mylist.insert(1, "yyc")
# print(mylist)

#4.00
mylist = [1,2,3]
mylist.append(4)
print(mylist)
mylist.append([5,6,7])
print(mylist)
mylist.extend([8,9,10])
print(mylist)

#5.00
# mylist = [1, 2, 3]
# del mylist[0]
# print(mylist)
# element = mylist.pop(1)
# print(f"取出的元素为：{element}，列表变为：{mylist}")

#6.00 remove函数去掉第一个出现的目标元素
# mylist = [1,2,3,3,3,4,3]
# mylist.remove(3)
# print(mylist)

#7.00
# mylist = [1,2,3]
# mylist.clear()
# print(mylist)

#8.00
# mylist = [1,2,3,4,4,4,4,5]
# count = mylist.count(4)
# print(count)

#9.00
# mylist = [1,2,3,1,2,3]
# length = len(mylist)
# print(length)
