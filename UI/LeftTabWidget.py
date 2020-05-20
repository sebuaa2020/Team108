#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import regex as re
import time
import ui1
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome


class LeftTabWidget(QWidget):
    '''左侧选项栏'''

    pointlist = []  #########
    renameIndex = 1

    def __init__(self):
        super(LeftTabWidget, self).__init__()
        # 设定UI名字
        self.setObjectName('LeftTabWidget')
        # UI窗口名称
        self.setWindowTitle('LeftTabWidget')
        self.list_style = ('''
            QListWidget, QListView, QTreeWidget, QTreeView {
                outline: 0px;
            }

            QListWidget {
                min-width: 150px;
                max-width: 150px;
                
                color: White;
                background:#545454;    
            }

            QListWidget::Item:selected {
                background: SlateGray;
                border-left: 5px solid #CAE1FF;
                color: black
            }
            HistoryPanel:hover {
                background: rgb(52, 52, 52);
            }
        ''')

        self.main_layout = QHBoxLayout(self, spacing=0)  # 窗口的整体布局
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.left_widget = QListWidget()  # 左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()

    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)  # list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)  # 去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['功能选择', '避障', '导航', '取物', '用户手册', '使用方法', '注意事项', '硬件设置', '联系与帮助', '遇到问题', '联系我们']

        for i in range(11):
            self.item = QListWidgetItem(list_str[i], self.left_widget)  # 左侧选项的添加
            self.item.setFont(QFont("等线", 11))
            if i == 0 or i == 4 or i == 8:
                self.item.setBackground(QColor('#1E90FF'))
                self.item.setFont(QFont("等线", 13, QFont.Bold))
                if i == 0:
                    self.item.setIcon(qtawesome.icon('fa.hand-pointer-o', color='white'))

                    self.centralWidget0 = QtWidgets.QWidget()
                    self.centralWidget0.setStyleSheet('''background:#F0FFFF;border-width:0;''');
                    self.layout0 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                    self.centralWidget0.setLayout(self.layout0)
                    self.label0_1 = QtWidgets.QLabel()  # 设置label
                    self.label0_1.setTextFormat(QtCore.Qt.AutoText)
                    self.label0_1.setStyleSheet('''color:black;font-size:23px; font-family:等线;''');
                    self.label0_1.setAlignment(Qt.AlignCenter)
                    self.label0_1.setPixmap(QPixmap('demo_rob.jpg'))
                    self.layout0.addWidget(self.label0_1, 0, 0, 1, 9)

                    self.right_widget.addWidget(self.centralWidget0)
                elif i == 4:
                    self.item.setIcon(qtawesome.icon('fa.tags', color='white'))

                    self.centralWidget4 = QtWidgets.QWidget()
                    self.centralWidget4.setStyleSheet('''background:#F0FFFF;border-width:0;''');
                    self.layout4 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                    self.centralWidget4.setLayout(self.layout4)
                    # self.centralWidget0.setLayout(self.layout0)
                    self.label4_1 = QtWidgets.QLabel()  # 设置label
                    self.label4_1.setTextFormat(QtCore.Qt.AutoText)
                    self.label4_1.setStyleSheet('''color:black;font-size:23px; font-family:等线;''');
                    self.label4_1.setAlignment(Qt.AlignCenter)
                    self.label4_1.setPixmap(QPixmap('demo_rob.jpg'))
                    self.layout4.addWidget(self.label4_1, 0, 0, 1, 9)

                    self.right_widget.addWidget(self.centralWidget4)
                elif i == 8:
                    self.item.setIcon(qtawesome.icon('fa.envelope', color='white'))

                    self.centralWidget8 = QtWidgets.QWidget()
                    self.centralWidget8.setStyleSheet('''background:#F0FFFF;border-width:0;''');
                    self.layout8 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                    self.centralWidget8.setLayout(self.layout8)
                    # self.centralWidget0.setLayout(self.layout0)
                    self.label8_1 = QtWidgets.QLabel()  # 设置label
                    self.label8_1.setTextFormat(QtCore.Qt.AutoText)
                    self.label8_1.setStyleSheet('''color:black;font-size:23px; font-family:等线;''');
                    self.label8_1.setAlignment(Qt.AlignCenter)
                    self.label8_1.setPixmap(QPixmap('demo_rob.jpg'))
                    self.layout8.addWidget(self.label8_1, 0, 0, 1, 9)

                    self.right_widget.addWidget(self.centralWidget8)

            self.item.setSizeHint(QSize(60, 65))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示


def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec()


if __name__ == '__main__':
    main()
