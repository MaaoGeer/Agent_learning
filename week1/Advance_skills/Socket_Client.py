"""
    Socket客户端编程
"""

import socket

# 创建socket对象
socket_client = socket.socket()

# 连接到服务器
socket_client.connect(("localhost", 8888))

while True:
    # 发送消息
    send_msg = input("请输入要给服务端发送的消息：")

    if send_msg == 'exit':
        break

    socket_client.send(send_msg.encode("UTF-8"))

    # 接受消息
    recv_data = socket_client.recv(1024).decode("UTF-8")
    print(f"服务器回应的消息是：{recv_data}")

# 关闭链接
socket_client.close()

