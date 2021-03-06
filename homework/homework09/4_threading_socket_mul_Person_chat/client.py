#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:client.py
# author:Asus
# datetime:2021/5/22 10:35
# software: PyCharm
'''
客户端
'''
# import module your need

import socket
import threading
import os
import get

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (get.get_ip(), 10000)
s.connect(addr)

def recv_msg():
    print('连接成功！现在可以接收消息！\n')
    while True:
        try:
            response = s.recv(1024)
            print(response.decode('gbk'))
        except ConnectionResetError:
            print('服务器关闭，聊天结束！')
            s.close()
            break


def send_msg():
    print("连接成功！现在可以发送消息！\n")
    print("输入消息按回车来发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("gbk"))


threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
for t in threads:
    t.start()
