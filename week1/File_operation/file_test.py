# 1.00
# 'r':只读；'w':写入，若原文件存在则删除原有内容，若不存在则创建新文件； 'a':追加，若原文件存在则写入原有内容之后，若不存在则创建新文件
# f = open("E:\\pytest\\pythonProject\\File_operation\\file.txt", "r", encoding="UTF-8")
# # read函数读取的是字符串类型
# print(f"read方法读取指定字节的结果是：{f.read(10)}")
# # 文件指针更新
# print(f"read方法读取全部字节的结果是：{f.read()}")
# print('----------------------------------')
#
# # 读取全部行
# lines = f.readlines()
# print(lines)
#
# # 读取一行，返回字符串类型
# line1 = f.readline()
# print(line1)
#
# # 文件关闭
# f.close()

# 2.00
# f = open("E:\\pytest\\pythonProject\\File_operation\\file.txt", "r", encoding="UTF-8")
# for line in f:        # 或者in f.readlines()
#     print(f'每一行的数据是：{line}')
# # 文件关闭
# f.close()

# 3.00 with open可以自动完成文件关闭
# with open("E:\\pytest\\pythonProject\\File_operation\\file.txt" "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f'每一行数据是：{line}')


# 4.00 write函数先将数据传入缓存区，flush函数将数据写入文件
# f = open("E:\\pytest\\pythonProject\\File_operation\\file1.txt", "w", encoding="UTF-8")
# f.write('Hello World')        # 将数据写入内存中
# f.flush()              # 将内存积攒的数据写入硬盘中
# f.close()              # close方法内置flush函数
#

# 5.00
# f = open("E:\\pytest\\pythonProject\\File_operation\\file.txt", "a", encoding="UTF-8")
# f.write('\nHello World')
# f.close()
