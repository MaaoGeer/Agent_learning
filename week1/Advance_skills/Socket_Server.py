"""
    Socket服务端编程
"""

import socket

# 创建Socket对象
socket_server = socket.socket()

# 绑定ip地址和端口  传入参数为(ip地址, 端口)
socket_server.bind(("localhost", 8888))

# 监听端口
# listen方法内接受一个整数传参，表示接受的链接数量
socket_server.listen(1)

# 等待客户端链接
# accept()方法,是阻塞的方法。等待客户端连接,如果没有客户端连接就卡在这一行
# accept方法返回二元元组(链接对象, 客户端的地址信息),可通过两个变量直接接受元组内的两个元素
conn, address = socket_server.accept()
# result: tuple = socket_server.accept()
# conn = result[0]        # 客户端和服务端的链接对象
# address = result[1]     # 客户端的地址信息
print(f"接受到了客户端的链接，客户端的信息是：{address}")


while True:
    # 接受客户端的信息,要使用客户端和服务端的本次链接对象，而非socket_server对象
    # recv接收的参数是缓存区大小,一般是1024即可
    # recv的方法的返回值是一个字符数组也就是bytes对象, 可通过decode方法通过UTF-8编码, 转换为字符串
    data: str = conn.recv(1024).decode("UTF-8")     # recv方法是阻塞式的
    print(f"客户端发来的消息是：{data}")

    # 发送回复消息
    msg = input("请输入要回复的消息：")

    if msg == 'exit':       # 判断程序是否继续执行
        break
    # 发送回复消息
    conn.send(msg.encode("UTF-8"))     # encode可以将字符串编码为字节数组类型

# 关闭链接
conn.close()
socket_server.close()
