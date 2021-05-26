#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3_SQlAchemy_Message_Board.py
# author:Asus
# datetime:2021/5/24 21:45
# software: PyCharm
'''
3  对2中的表结构，用SQLAlchemy模块来实现同样的操作；
'''
# import module your need


from models.messageModel import MessageModel as m


def main():
    while True:
        print('《《《留言板》》》\n\n1、添加留言;\n2、删除留言;\n3、查询;\n4、修改;\n5、退出留言板。\n')
        flag = int(input('输入功能序号：'))
        if flag == 1:
            m.add_content()
        elif flag == 2:
            m.del_content()
        elif flag == 3:
            m.get_all_content()
            m.search_content()
        elif flag == 4:
            m.update_content()
        elif flag == 5:
            break
        if int(input('\n是否继续？ 1/0：')) == 0:
            break


if __name__ == '__main__':
    main()
