"""
    演示多线程编程的使用

    import threading
    thread_onj = threading.Thread(group, target, name, args, kwargs)
    - group : 暂时无用,未来功能的预留参数
    - target : 执行的目标任务名
    - args : 以元组的方式给执行任务传参
    - kwargs : 以字典的方式给执行任务传参
    - name : 线程名,一般不设置

    thread_onj.start()      启动线程
"""
import threading
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing, args=("我要唱歌", ))
    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "我要跳舞"})

    # 启动线程
    sing_thread.start()
    dance_thread.start()
