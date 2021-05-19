#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3.py
# author:Asus
# datetime:2021/5/19 17:01
# software: PyCharm
'''
3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
'''
# import module your need

import socket,sys,os
from multiprocessing import Pool

local_addr = ('', 9999)
dest_addr = ('127.0.0.1', 1234)


def main():
    fn = sys.stdin.fileno()
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(local_addr)
    po = Pool(2)
    po.apply_async(send, (udp_socket, fn))
    po.apply_async(recv, (udp_socket,))
    po.close()
    po.join()
    # while True:
    #     recv_data = udp_socket.recvfrom(1024)
    #     print(recv_data[1][0] + ':' + recv_data[0].decode('gbk'))
    #     send(udp_socket)


def send(s, fn):
    sys.stdin = os.fdopen(fn)
    while True:
        send_data = input()
        s.sendto(send_data.encode('utf-8'), dest_addr)


def recv(s):
    while True:
        recv_data = s.recvfrom(1024)
        print(recv_data[1][0]+':' + recv_data[0].decode('gbk'))


if __name__ == '__main__':
    main()