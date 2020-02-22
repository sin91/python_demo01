#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import threading
import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed!' % addr)

def start_server():
    # 定义一个使用IPV4和传输流的socket对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 指定监听地址和端口
    server.bind(('127.0.0.1', 8899))

    # 调用监听方法，开始监听，参数指定等待连接的最大数量
    server.listen(5)
    print('Waiting for connection...')

    # 启动服务循环
    while True:
        # 接收一个新的连接
        s, addr = server.accept()

        # 创建新线程处理TCP连接
        t = threading.Thread(target=tcplink, args=(s, addr))
        t.start()


if __name__ == '__main__':
    start_server()
