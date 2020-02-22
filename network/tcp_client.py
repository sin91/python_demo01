#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket

def connect_server():
    print('Connecting to server...')

    # 定义使用IPV4协议和传输流的socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 建立连接
    s.connect(('127.0.0.1', 8899))

    # 接收欢迎信息
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据
        s.send(data)
        print(s.recv(1024).decode('utf-8'))

    s.send(b'exit')
    s.close()

if __name__ == '__main__':
    connect_server()
