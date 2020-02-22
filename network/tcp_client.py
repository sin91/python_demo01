#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def start_udp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in ['Devin', 'Pall', 'Jinny']:
        # 发送数据 UDP发送数据不需要先connect
        sock.sendto(data,('127.0.0.1', 8899))

        # 接收数据
        print(sock.recv(1024).decode('utf-8'))
    socket.close()

if __name__ == '__main__':
    start_udp_client()
