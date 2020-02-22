#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def start_upd_server():
    # 定义IPV4 socket，注意参数使用socket.SCOK_DGRAM
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定地址和端口号, TCP和UDP可使用同一个端口不互相影响
    sock.bind(('127.0.0.1', 8899))

    print('UDP bind to 8899...')

    # UDP协议不需要Listen
    while True:
        # 接收数据
        data, addr = sock.recvfrom(1024)
        print('Received from %s:%s' % addr)
        
        # 直接发送数据给对方
        sock.sendto(b'Hello, %s!' % data, addr)
        
if __name__ == '__main__':
    start_upd_server()
