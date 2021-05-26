#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2.py
# author:Asus
# datetime:2021/5/19 16:44
# software: PyCharm
'''
2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；

'''
# import module your need
import socket
from socket import *


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    local_addr = ('', 9999)
    udp_socket.bind(local_addr)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('gbk'))
    udp_socket.close()


if __name__ == '__main__':
    main()
