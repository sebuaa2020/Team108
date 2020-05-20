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




			# '硬件设置'
            elif i == 7:
                self.centralWidget7 = QtWidgets.QWidget()
                self.centralWidget7.setStyleSheet('''background:#F0FFFF;border-width:0;''');

                self.layout7 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget7.setLayout(self.layout7)

                self.label7_1 = QtWidgets.QLabel()
                self.label7_1.setTextFormat(QtCore.Qt.AutoText)
                self.label7_1.setText("硬件设置")
                self.label7_1.setStyleSheet('''color:black;font-size:23px;background:#F0FFFF;
                                                font-family:Times new Romans;''');
                self.label7_1.setAlignment(Qt.AlignCenter)

                self.label7_2 = QtWidgets.QLabel()
                self.label7_2.setTextFormat(QtCore.Qt.AutoText)
                self.label7_2.setPixmap(QPixmap('structure.png'))
                self.label7_2.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label7_2.setAlignment(Qt.AlignCenter)

                self.label7_3 = QtWidgets.QLabel()
                self.label7_3.setTextFormat(QtCore.Qt.AutoText)
                self.label7_3.setPixmap(QPixmap('panel.png'))
                self.label7_3.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label7_3.setAlignment(Qt.AlignCenter)

                self.label7_4 = QtWidgets.QLabel()
                self.label7_4.setTextFormat(QtCore.Qt.AutoText)
                self.label7_4.setText("结构组成展示")
                self.label7_4.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label7_4.setAlignment(Qt.AlignCenter)


                self.label7_5 = QtWidgets.QLabel()
                self.label7_5.setTextFormat(QtCore.Qt.AutoText)
                self.label7_5.setText("开关面板展示")
                self.label7_5.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label7_5.setAlignment(Qt.AlignCenter)

                self.layout7.addWidget(self.label7_1, 0, 0, 1, 4)
                self.layout7.addWidget(self.label7_2, 1, 0, 1, 2)
                self.layout7.addWidget(self.label7_3, 1, 2, 1, 2)
                self.layout7.addWidget(self.label7_4, 2, 0, 1, 2)
                self.layout7.addWidget(self.label7_5, 2, 2, 1, 2)

                self.right_widget.addWidget(self.centralWidget7)

            # '遇到问题'
            elif i == 9:
                self.centralWidget9 = QtWidgets.QWidget()
                self.centralWidget9.setStyleSheet('''background:white;border-width:0;''');

                self.layout9 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget9.setLayout(self.layout9)

                self.label9_1 = QtWidgets.QLabel()
                self.label9_1.setTextFormat(QtCore.Qt.AutoText)
                self.label9_1.setText("在使用本机器人的过程中，你可能遇到以下几种问题：")
                self.label9_1.setStyleSheet('''color:white;font-size:23px;background:#1E90FF;
                                                font-family:Times new Romans;''');
                self.label9_1.setAlignment(Qt.AlignCenter)

                self.label9_2 = QtWidgets.QLabel()
                self.label9_2.setTextFormat(QtCore.Qt.AutoText)
                self.label9_2.setText(
                    "Q1：用户下达指令后，机器人无法运动\nA1：停止使用机器人，检查机器人电量是否充足(即剩余电量是否大于等于23)\n若电量不足，请先为机器人补充电量再使用\n若电量充足，或补充电量后机器人仍不运行\n请在下方“联系我们”处查找本设计组的联系方式，我们将为您提供免费的维修服务")
                self.label9_2.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label9_2.setAlignment(Qt.AlignCenter)

                self.label9_3 = QtWidgets.QLabel()
                self.label9_3.setTextFormat(QtCore.Qt.AutoText)
                self.label9_3.setText("Q2：机器人部件损坏或在运动中出现故障\nA1：请在下方“联系我们”处查找本设计组的联系方式，我们将为您提供免费的维修服务")
                self.label9_3.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label9_3.setAlignment(Qt.AlignCenter)

                self.label9_4 = QtWidgets.QLabel()
                self.label9_4.setTextFormat(QtCore.Qt.AutoText)
                self.label9_4.setText(
                    "Q3：机器人在运动中发生碰撞\nA3：立即使用“急停”按钮使机器人紧急制动\n查看机器人情况，从外观上初步判断机器人是否完好，并尝试机器人的其他功能\n若出现外观上的较大损坏或功能上的缺失\n请在下方“联系我们”处查找本设计组的联系方式，我们将为您提供免费的维修服务")
                self.label9_4.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label9_4.setAlignment(Qt.AlignCenter)

                self.label9_5 = QtWidgets.QLabel()
                self.label9_5.setTextFormat(QtCore.Qt.AutoText)
                self.label9_5.setText(
                    "Q4：机器人出现了其他的错误（包括报告未知错误信息）\nA4：请在下方“联系我们”处查找本设计组的联系方式，我们将为您提供免费的维修服务\n注意，我们需要您提供相关的错误信息，包括机器人当时的运动状态、如发生错误前后的操作、\n具体错误行为表现、控制单元报告的错误信息具体内容等")
                self.label9_5.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label9_5.setAlignment(Qt.AlignCenter)

                self.layout9.addWidget(self.label9_1, 0, 0, 1, 4)
                self.layout9.addWidget(self.label9_2, 1, 0, 1, 2)
                self.layout9.addWidget(self.label9_3, 1, 2, 1, 2)
                self.layout9.addWidget(self.label9_4, 2, 0, 1, 2)
                self.layout9.addWidget(self.label9_5, 2, 2, 1, 2)

                self.right_widget.addWidget(self.centralWidget9)

            else:
                if i!= 0 and i != 4 and i != 8:
                    self.centralWidget0=QtWidgets.QWidget()
                    self.centralWidget0.setStyleSheet('''background:white;border-width:0;''');
                    self.right_widget.addWidget(self.centralWidget0)



def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec()


if __name__ == '__main__':
    main()
