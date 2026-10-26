# f = open('E:\\Agent_learning\\week2\\test.txt','r',encoding='utf-8')
# content = f.read()
# print(content)

# cont_list = f.readlines()
# print(cont_list)
# f.close()

f1 = open('E:\\Agent_learning\\week2\\test1.txt','w',encoding='utf-8')
try:
    f1.write('cont_list[0]\n')
    f1.write('cont_list[1]\n')
finally:    # finally使得文件可以一定关闭
    f1.close()

# 推荐方式
with open('E:\\Agent_learning\\week2\\test1.txt','r',encoding='utf-8') as f:
    f1.write('cont_list[2]\n')
    f1.write('cont_list[3]\n')