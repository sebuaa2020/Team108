# !/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import regex as re
import time
# import ui1
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome


class LeftTabWidget(QWidget):
    '''左侧选项栏'''

    pointlist = []
    renameIndex = 1

    def __init__(self):
        super(LeftTabWidget, self).__init__()
        # 设定UI名字
        self.setObjectName('LeftTabWidget')
        # UI窗口名称
        self.setWindowTitle('LeftTabWidget')
        # 设定左侧栏相关设置
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

        # 运行_setup_ui()，定义左侧选项栏各个页面显示
        self._setup_ui()

    def _setup_ui(self):
        '''加载界面ui'''
        # list和右侧窗口的index对应绑定
        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)
        # 去掉边框
        self.left_widget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['功能选择', '避障', '导航', '取物', '用户手册', '使用方法', '注意事项', '环境配置', '联系与帮助', '遇到问题', '联系我们']
        # os.system("gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&source ./devel/setup.bash&&roslaunch robot_sim_demo robot_spawn.launch\"'")

        for i in range(11):
            self.item = QListWidgetItem(list_str[i], self.left_widget)  # 左侧选项的添加
            self.item.setFont(QFont("等线", 11))

            # 设定功能选择、用户手册、联系与帮助相关界面内容
            if i == 0 or i == 4 or i == 8:
                # 设定页面背景颜色
                self.item.setBackground(QColor('#1E90FF'))
                # 设定字体格式
                self.item.setFont(QFont("等线", 13, QFont.Bold))

                # 功能选择界面
                if i == 0:
                    self.item.setIcon(qtawesome.icon('fa.hand-pointer-o', color='white'))

                    self.centralWidget0 = QtWidgets.QWidget()
                    self.centralWidget0.setStyleSheet('''background:#F0FFFF;border-width:0;''');
                    # 创建左侧部件的网格布局层
                    self.layout0 = QtWidgets.QGridLayout()
                    self.centralWidget0.setLayout(self.layout0)
                    # 设置label
                    self.label0_1 = QtWidgets.QLabel()
                    self.label0_1.setTextFormat(QtCore.Qt.AutoText)
                    self.label0_1.setStyleSheet('''color:black;font-size:23px; font-family:等线;''');
                    self.label0_1.setAlignment(Qt.AlignCenter)
                    self.label0_1.setPixmap(QPixmap('demo_rob.jpg'))

                    self.layout0.addWidget(self.label0_1, 0, 0, 1, 9)
                    # 增加虚拟场景加载指令按钮
                    self.button1 = QtWidgets.QPushButton()
                    self.button1.setText("开始")
                    # 设置按钮大小
                    self.button1.setFixedSize(100, 40)
                    # 设置按钮渲染格式
                    self.button1.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:10px;font-family:等线;
                                                                   font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                    # 设置按钮按动时相应的函数
                    self.button1.clicked.connect(self.button1_0click)

                    # 设置右边窗口相关内容
                    self.right_widget.addWidget(self.centralWidget0)
                    self.layout0.addWidget(self.button1, 9, 4, 2, 2)

                # 设置用户手册界面
                elif i == 4:
                    self.item.setIcon(qtawesome.icon('fa.tags', color='white'))

                    self.centralWidget4 = QtWidgets.QWidget()
                    self.centralWidget4.setStyleSheet('''background:#F0FFFF;border-width:0;''')
                    # 创建左侧部件的网格布局层
                    self.layout4 = QtWidgets.QGridLayout()
                    self.centralWidget4.setLayout(self.layout4)
                    # self.centralWidget0.setLayout(self.layout0)
                    # 设置label
                    self.label4_1 = QtWidgets.QLabel()
                    # 设置字体格式
                    self.label4_1.setTextFormat(QtCore.Qt.AutoText)
                    # 设置style
                    self.label4_1.setStyleSheet('''color:black;font-size:23px; font-family:等线;''')
                    # 设置对齐格式
                    self.label4_1.setAlignment(Qt.AlignCenter)
                    # 设置图片
                    self.label4_1.setPixmap(QPixmap('demo_rob.jpg'))
                    # 把label4_1添加到页面布局中
                    self.layout4.addWidget(self.label4_1, 0, 0, 1, 9)

                    self.right_widget.addWidget(self.centralWidget4)

                # 设置联系与帮助相关
                elif i == 8:

                    self.item.setIcon(qtawesome.icon('fa.envelope', color='white'))

                    self.centralWidget8 = QtWidgets.QWidget()
                    self.centralWidget8.setStyleSheet('''background:#F0FFFF;border-width:0;''')
                    self.layout8 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                    self.centralWidget8.setLayout(self.layout8)
                    # self.centralWidget0.setLayout(self.layout0)
                    # 设置label
                    self.label8_1 = QtWidgets.QLabel()
                    # 设置字体格式
                    self.label8_1.setTextFormat(QtCore.Qt.AutoText)
                    # 设置style
                    self.label8_1.setStyleSheet('''color:black;font-size:23px; font-family:等线;''')
                    # 设置对齐方式
                    self.label8_1.setAlignment(Qt.AlignCenter)
                    # 设置加载的图片
                    self.label8_1.setPixmap(QPixmap('demo_rob.jpg'))
                    # 把label8_1加入页面布局中
                    self.layout8.addWidget(self.label8_1, 0, 0, 1, 9)

                    self.right_widget.addWidget(self.centralWidget8)
                    self.item.setSizeHint(QSize(60, 65))
                    self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

            # 设置大小
            self.item.setSizeHint(QSize(60, 65))
            # 居中显示
            self.item.setTextAlignment(Qt.AlignCenter)

            if i == 1:
                # 创建整体背景
                self.centralWidget1 = QtWidgets.QWidget()
                self.centralWidget1.setStyleSheet('''background:#F0FFFF;border-width:0;''');
                # 创建左侧部件的网格布局层
                self.layout1 = QtWidgets.QGridLayout()
                self.centralWidget1.setLayout(self.layout1)

                # 创建机器人最大运行速度的输入框
                self.edit1_1 = QtWidgets.QLineEdit()
                self.edit1_1.setPlaceholderText("请输入速度(两位小数,0.0-0.2)")
                self.edit1_1.setStyleSheet('''color:black;background:transparent;border-width:0;
                                                border-style:outset;border-bottom:1px solid black;
                                                font-size:20px; font-family:等线;''')
                # 利用正则匹配限定输入
                self.vel_reg = QRegExp(r"^(0)|(0\.[0-9])|(1)|(1\.0)$")
                self.vel_validator = QRegExpValidator(self.vel_reg, self.edit1_1)
                self.edit1_1.setValidator(self.vel_validator)

                # 创建避障任务巡航时间的输入框
                self.edit1_2 = QtWidgets.QLineEdit()
                self.edit1_2.setPlaceholderText("请输入时间(三位整数)")
                self.edit1_2.setStyleSheet('''color:black;background:transparent;border-width:0;
                                                border-style:outset;border-bottom:1px solid black;
                                                font-size:20px; font-family:等线;''')
                # 利用正则匹配限定巡航时间
                self.time_reg = QRegExp("^[0-9]{3}$")
                self.time_validator = QRegExpValidator(self.time_reg, self.edit1_2)
                self.edit1_2.setValidator(self.time_validator)

                # 设置速度提示标签：label1_1
                self.label1_1 = QtWidgets.QLabel()
                self.label1_1.setTextFormat(QtCore.Qt.AutoText)
                self.label1_1.setText("速度")
                self.label1_1.setStyleSheet('''color:1E90FF;font-size:26px;background:#F0FFFF;
                                                font-family:等线;''')
                self.label1_1.setAlignment(Qt.AlignCenter)

                # 设置时间提示标签：label1_2
                self.label1_2 = QtWidgets.QLabel()
                self.label1_2.setTextFormat(QtCore.Qt.AutoText)
                self.label1_2.setText("时间")
                self.label1_2.setStyleSheet('''color:1E90FF;font-size:26px;background:#F0FFFF;
                                                font-family:等线;''')
                self.label1_2.setAlignment(Qt.AlignCenter)

                # 设置避障标签：label1_3
                self.label1_3 = QtWidgets.QLabel()
                self.label1_3.setTextFormat(QtCore.Qt.AutoText)
                self.label1_3.setText("避障")
                self.label1_3.setStyleSheet('''color:1E90FF;font-size:23px;background:#F0FFFF;
                                                font-family:等线;''')
                self.label1_3.setAlignment(Qt.AlignCenter)

                # 设置调用巡航任务接口的按钮button1
                self.button1 = QtWidgets.QPushButton()
                self.button1.setText("开始")
                self.button1.setFixedSize(100, 40)
                self.button1.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:10px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button1.clicked.connect(self.button1_1click)

                self.layout1.setColumnStretch(0, 2)
                self.layout1.setColumnStretch(1, 2)
                self.layout1.setColumnStretch(2, 2)
                self.layout1.setColumnStretch(3, 2)
                self.layout1.setColumnStretch(5, 2)
                self.layout1.setColumnStretch(6, 2)
                self.layout1.setColumnStretch(7, 2)
                self.layout1.setColumnStretch(8, 2)
                self.layout1.setColumnStretch(4, 1)

                self.layout1.addWidget(self.label1_3, 0, 0, 1, 9)
                self.layout1.addWidget(self.label1_1, 4, 2, 2, 2)
                self.layout1.addWidget(self.label1_2, 6, 2, 2, 2)
                self.layout1.addWidget(self.edit1_1, 4, 4, 2, 3)
                self.layout1.addWidget(self.edit1_2, 6, 4, 2, 3)
                self.layout1.addWidget(self.button1, 9, 4, 2, 2)
                self.right_widget.addWidget(self.centralWidget1)

            elif i == 2:
                # os.system("gnome-terminal -e 'bash -c \"roscore\"'")
                # 创建整体背景
                self.centralWidget2 = QtWidgets.QWidget()
                self.centralWidget2.setStyleSheet('''background:#F0FFFF;border-width:0;''');
                self.layout2 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget2.setLayout(self.layout2)

                # 创建按钮2_7，启动手柄
                self.button2_7 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_7.setObjectName("button7")
                self.button2_7.setText("启动方向控制")
                self.button2_7.clicked.connect(self.button2_7click)
                self.button2_7.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_7.setFixedHeight(40)

                # 创建按钮2_8，启动手柄
                self.button2_8 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_8.setObjectName("button8")
                self.button2_8.setText("启动语音控制")
                self.button2_8.clicked.connect(self.button2_8click)
                self.button2_8.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_8.setFixedHeight(40)

                # 创建按钮2_1，功能是调用地图创建终端
                self.button2_1 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_1.setObjectName("button1")
                self.button2_1.setText("构建地图")
                self.button2_1.clicked.connect(self.button2_1click)
                self.button2_1.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_1.setFixedHeight(40)

                # 创建按钮2_2，调用保存地图指令
                self.button2_2 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_2.setObjectName("button2")
                self.button2_2.setText("保存地图")
                self.button2_2.clicked.connect(self.button2_2click)
                self.button2_2.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_2.setFixedHeight(40)

                # 创建按钮2_3，终端调用设立航点命令
                self.button2_3 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_3.setObjectName("button3")
                self.button2_3.setText("设立航点")
                self.button2_3.clicked.connect(self.button2_3click)
                self.button2_3.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_3.setFixedHeight(40)

                # 创建按钮2_4，调用终端保存航点命令
                self.button2_4 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_4.setObjectName("button4")
                self.button2_4.setText("保存航点")
                self.button2_4.clicked.connect(self.button2_4click)
                self.button2_4.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_4.setFixedHeight(40)

                # 创建按钮2_5，调用终端导航指令
                self.button2_5 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_5.setObjectName("button5")
                self.button2_5.setText("开始导航")
                self.button2_5.clicked.connect(self.button2_5click)
                self.button2_5.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_5.setFixedHeight(40)

                # 增加容器comboBox2
                # self.comboBox2 = QtWidgets.QComboBox(self.centralWidget2)
                # self.comboBox2.setObjectName("comboBox")
                # self.comboBox2.setStyleSheet('''QComboBox{background:#1E90FF;border-radius:10px;font-family:等线;
                #                                font-size:18px;color:white}QComboBox:hover{background:#EEDC82;}''')
                # self.comboBox2.setFixedHeight(40)

                # 设置button2_6，机器人运行按钮
                # self.button2_6 = QtWidgets.QPushButton(self.centralWidget2)
                # self.button2_6.setObjectName("button6")
                # self.button2_6.setText("G O !")
                # self.button2_6.clicked.connect(self.button2_6click)
                # self.button2_6.setStyleSheet('''QPushButton{background:#1E90FF;border-radius:20px;font-family:等线;
                #                                font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                # self.button2_6.setFixedHeight(40)

                # 增加页面标题，导航
                self.label2_1 = QtWidgets.QLabel()
                self.label2_1.setTextFormat(QtCore.Qt.AutoText)
                self.label2_1.setText("导航")
                self.label2_1.setStyleSheet('''color:1E90FF;font-size:23px;background:#F0FFFF;
                                                font-family:等线;''')
                self.label2_1.setAlignment(Qt.AlignCenter)

                # 增加页面第二个标题
                # self.label2_2 = QtWidgets.QLabel()
                # self.label2_2.setTextFormat(QtCore.Qt.AutoText)
                # self.label2_2.setText("")
                # self.label2_2.setAlignment(Qt.AlignCenter)

                #
                self.layout2.setColumnStretch(0, 1)
                self.layout2.setColumnStretch(1, 2)
                self.layout2.setColumnStretch(2, 2)
                self.layout2.setColumnStretch(3, 1)
                self.layout2.setColumnStretch(4, 2)
                self.layout2.setColumnStretch(5, 2)
                self.layout2.setColumnStretch(6, 1)
                self.layout2.setRowStretch(0, 2)
                self.layout2.setRowStretch(1, 2)
                self.layout2.setRowStretch(2, 2)
                self.layout2.setRowStretch(3, 2)
                self.layout2.setRowStretch(4, 2)
                self.layout2.setRowStretch(5, 2)
                self.layout2.setRowStretch(6, 2)
                self.layout2.setRowStretch(7, 2)
                self.layout2.setRowStretch(8, 2)
                self.layout2.setHorizontalSpacing(5)
                self.layout2.setVerticalSpacing(5)
                self.layout2.addWidget(self.label2_1, 0, 0, 1, 7)
                self.layout2.addWidget(self.button2_7, 2, 4, 1, 2)
                self.layout2.addWidget(self.button2_1, 2, 1, 1, 2)
                self.layout2.addWidget(self.button2_2, 4, 1, 1, 2)
                self.layout2.addWidget(self.button2_3, 4, 4, 1, 2)
                self.layout2.addWidget(self.button2_4, 6, 1, 1, 2)
                self.layout2.addWidget(self.button2_5, 6, 4, 1, 2)
                self.layout2.addWidget(self.button2_8, 8, 1, 1, 2)
                # self.layout2.addWidget(self.button2_6, 8, 4, 1, 2)
                # self.layout2.addWidget(self.comboBox2, 8, 1, 1, 2)
                # self.layout2.addWidget(self.label2_2, 9, 1, 1, 7)
                self.right_widget.addWidget(self.centralWidget2)

            elif i == 3:
                # label3_1 设置标题相关属性
                self.label3_1 = QtWidgets.QLabel()
                self.label3_1.setTextFormat(QtCore.Qt.AutoText)
                self.label3_1.setText("取物")
                self.label3_1.setStyleSheet('''color:black;font-size:23px;background:#F0FFFF;
                                                            font-family:等线;''');
                self.label3_1.setAlignment(Qt.AlignCenter)

                # label3_2 指南针图标相关属性
                self.label3_2 = QtWidgets.QLabel()
                self.label3_2.setAlignment(Qt.AlignCenter)
                pixmap = QPixmap('指南针.png').scaled(self.label3_2.width() * 0.25,
                                                   self.label3_2.height() * 0.35)
                self.label3_2.setPixmap(pixmap)

                # label3_3 放大镜图标相关属性
                self.label3_3 = QtWidgets.QLabel()
                self.label3_3.setAlignment(Qt.AlignCenter)
                pixmap = QPixmap('放大镜.png').scaled(self.label3_3.width() * 0.25,
                                                   self.label3_3.height() * 0.35)
                self.label3_3.setPixmap(pixmap)

                self.centralWidget3 = QtWidgets.QWidget()
                # 更改颜色
                self.centralWidget3.setStyleSheet('''background:#F0FFFF;border-width:0;''');
                self.layout3 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget3.setLayout(self.layout3)

                # 设置标定航点任务的按钮
                self.button3_1 = QtWidgets.QPushButton()
                self.button3_1.setText("标定航点")
                self.button3_1.setFixedSize(200, 40)
                self.button3_1.setStyleSheet('''
                                QPushButton{
                                    border:none;color:#1E90FF;
                                    border-bottom:1px solid #1E90FF;
                                    font-size:20px;
                                    font-weight:700;
                                    font-family:等线;
                                }
                            ''')

                # 设置检测物体并抓取任务的按钮
                self.button3_2 = QtWidgets.QPushButton()
                self.button3_2.setText("检测物体并抓取")
                self.button3_2.setFixedSize(200, 40)
                self.button3_2.setStyleSheet('''
                                QPushButton{
                                    border:none;color:#1E90FF;
                                    border-bottom:1px solid #1E90FF;
                                    font-size:20px;
                                    font-weight:700;
                                    font-family:等线;
                                }
                            ''')

                # 将所有元素添加到抓取任务的画板中
                self.layout3.addWidget(QtWidgets.QWidget(), 1, 0, 1, 10)
                self.layout3.addWidget(QtWidgets.QWidget(), 5, 0, 2, 10)
                self.layout3.addWidget(self.label3_1, 0, 0, 1, 9)
                self.layout3.addWidget(self.label3_2, 2, 2, 1, 1)
                self.layout3.addWidget(self.label3_3, 2, 6, 1, 1)
                self.layout3.addWidget(self.button3_1, 4, 2, 1, 2)
                self.layout3.addWidget(self.button3_2, 4, 6, 1, 2)
                self.right_widget.addWidget(self.centralWidget3)

            elif i == 5:
                # 设置使用方法整体布局
                self.centralWidget5 = QtWidgets.QWidget()
                self.centralWidget5.setStyleSheet('''background:#F0FFFF;border-width:0;''')
                self.layout5 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget5.setLayout(self.layout5)

                self.label5_0 = QtWidgets.QLabel()
                self.label5_0.setTextFormat(QtCore.Qt.AutoText)
                self.label5_0.setText("使用方法")
                self.label5_0.setStyleSheet('''color:black;font-size:23px;background:#F0FFFF;
                                                font-family:等线;''')
                self.label5_0.setAlignment(Qt.AlignCenter)

                self.label5_1 = QtWidgets.QLabel()
                self.label5_1.setAlignment(Qt.AlignCenter)
                pixmap = QPixmap('robot.png').scaled(self.label5_1.width() * 0.07, self.label5_1.height() * 0.10)
                self.label5_1.setPixmap(pixmap)

                self.label5_2 = QtWidgets.QLabel()
                self.label5_2.setAlignment(Qt.AlignCenter)
                pixmap = QPixmap('避障.png').scaled(self.label5_2.width() * 0.07, self.label5_2.height() * 0.10)
                self.label5_2.setPixmap(pixmap)

                self.label5_3 = QtWidgets.QLabel()
                self.label5_3.setAlignment(Qt.AlignCenter)
                pixmap = QPixmap('导航.png').scaled(self.label5_3.width() * 0.07, self.label5_3.height() * 0.10)
                self.label5_3.setPixmap(pixmap)

                self.label5_4 = QtWidgets.QLabel()
                self.label5_4.setAlignment(Qt.AlignCenter)
                pixmap = QPixmap('抓取.png').scaled(self.label5_4.width() * 0.07, self.label5_4.height() * 0.10)
                self.label5_4.setPixmap(pixmap)

                self.label5_5 = QtWidgets.QLabel()  # 设置label
                self.label5_5.setTextFormat(QtCore.Qt.AutoText)
                self.label5_5.setText('''
                                        控制界面：进行功能选取、操纵机器人前行\n
                                        打开机器人：按下底盘上的开关按钮使之变亮\n
                                        关闭机器人：按下底盘上的开关按钮使之变暗\n
                                        USB连接： 麦克风、相机、雷达、以太网等\n
                                       （具体接口参照用户手册）''')
                self.label5_5.setStyleSheet('''color:black;font-size:14px; font-family:等线;''')
                self.label5_5.setAlignment(Qt.AlignLeft)

                self.label5_6 = QtWidgets.QLabel()  # 设置label
                self.label5_6.setTextFormat(QtCore.Qt.AutoText)
                self.label5_6.setText('''
                                        避障：在给定区域内随机行走，自主避障\n
                                        输入速度(m/s)，机器人将以该线速度行走\n
                                        输入时间(s)，机器人在限制时间段内行走\n
                                        点击开始按钮，机器人开始行走（输入的时间与速度\n
                                        需符合给定要求）''')
                self.label5_6.setStyleSheet('''color:black;font-size:14px; font-family:等线;''')
                self.label5_6.setAlignment(Qt.AlignLeft)

                self.label5_7 = QtWidgets.QLabel()  # 设置label
                self.label5_7.setTextFormat(QtCore.Qt.AutoText)
                self.label5_7.setText('''
                                        导航：机器人行走至目标航点\n
                                        点击建立地图按钮，在图形化界面操纵机器人行走\n
                                        点击保存地图按钮，保存刚刚建立的地图\n
                                        点击标定航点按钮，在地图上标定目标航点\n
                                        点击保存航点按钮，保存刚刚标定的航点信息\n
                                        下拉菜单中可选择机器人行走的目标航点\n
                                        点击开始导航按钮，机器人将行走至目标航点\n
                                        注意事项：\n
                                        若已经构建过地图且没有重新构建，则不需要构建地图\n
                                        构建的地图应覆盖所在区域\n
                                        地图保存完毕前不要关掉虚拟环境\n
                                        航点保存完毕前不要关掉虚拟环境\n
                                        ''')
                self.label5_7.setStyleSheet('''color:black;font-size:14px; font-family:等线;''')
                self.label5_7.setAlignment(Qt.AlignLeft)

                self.label5_8 = QtWidgets.QLabel()  # 设置label
                self.label5_8.setTextFormat(QtCore.Qt.AutoText)
                self.label5_8.setText('''
                                        抓取：机器人识别目标物体并进行抓取\n
                                        点击建立航点按钮，带领机器人用语音标定航点\n
                                        点击开始检测并抓取按钮，机器人将识别出目标物体\n
                                        并完成抓取动作\n
                                        抓取结束后机器人将回到开始识别的地点并将物体递给用户\n
                                        注意事项:\n
                                        选择的抓取物品需满足要求(参考注意事项)\n''')
                self.label5_8.setStyleSheet('''color:black;font-size:14px; font-family:等线;''')
                self.label5_8.setAlignment(Qt.AlignLeft)

                self.layout5.addWidget(self.label5_0, 0, 0, 1, 8)
                self.layout5.addWidget(self.label5_1, 1, 0, 1, 4)
                self.layout5.addWidget(self.label5_2, 1, 4, 1, 4)
                self.layout5.addWidget(self.label5_3, 5, 0, 1, 4)
                self.layout5.addWidget(self.label5_4, 5, 4, 1, 4)
                self.layout5.addWidget(self.label5_5, 2, 0, 3, 4)
                self.layout5.addWidget(self.label5_6, 2, 4, 3, 4)
                self.layout5.addWidget(self.label5_7, 6, 0, 3, 4)
                self.layout5.addWidget(self.label5_8, 6, 4, 3, 4)
                self.right_widget.addWidget(self.centralWidget5)

            elif i == 6:
                self.centralWidget6 = QtWidgets.QWidget()
                self.centralWidget6.setStyleSheet('''background:#F0FFFF;border-width:0;''');

                self.layout6 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget6.setLayout(self.layout6)

                ##start coding
                self.label6_1 = QtWidgets.QLabel()
                self.label6_1.setTextFormat(QtCore.Qt.AutoText)
                self.label6_1.setText("注意事项")
                self.label6_1.setStyleSheet('''color:white;font-size:23px;background:#1E90FF;
                                                font-family:Times new Romans;''');
                self.label6_1.setAlignment(Qt.AlignCenter)

                self.label6_2 = QtWidgets.QLabel()
                self.label6_2.setTextFormat(QtCore.Qt.AutoText)
                self.label6_2.setText('环境要求:\n\
                1、机器人仿真环境正常建立：界面由暗到亮，且能够拖拽改变视角。\n\
                2、计算机运行内存资源充足。保证虚拟环境仿真、建图指令有足够空间运行。\n\
                3、保证仿真环境建图指令正确运行，机器人能够成功扫描四周并建图。\n\
                4、保证机器人所处地点不在死角，四周可以规划出一条合理路径。\n\
                5、标定航点不设置在障碍物中。')
                self.label6_2.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label6_2.setAlignment(Qt.AlignCenter)

                self.label6_3 = QtWidgets.QLabel()
                self.label6_3.setTextFormat(QtCore.Qt.AutoText)
                self.label6_3.setText("避免损伤:\n\
                1、设定的移动速率不超过0.2m/s，避免因机器人速度过快造成的损伤。\n\
                2、机器人运行的起始位置附近相对空旷，避免碰撞。\n\
                3、标定的航点附近应相对空旷，避免碰撞。\n")
                self.label6_3.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label6_3.setAlignment(Qt.AlignCenter)

                self.layout6.addWidget(self.label6_1, 0, 0, 1, 4)
                self.layout6.addWidget(self.label6_2, 1, 0, 1, 2)
                self.layout6.addWidget(self.label6_3, 1, 2, 1, 2)
                # self.layout6.addWidget(self.label6_4,2,0,1,2)
                # self.layout6.addWidget(self.label6_5,2,2,1,2)

                self.right_widget.addWidget(self.centralWidget6)

            # '环境配置'
            elif i == 7:
                self.centralWidget7 = QtWidgets.QWidget()
                self.centralWidget7.setStyleSheet('''background:#F0FFFF;border-width:0;''')

                self.layout7 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget7.setLayout(self.layout7)

                self.label7_1 = QtWidgets.QLabel()
                self.label7_1.setTextFormat(QtCore.Qt.AutoText)
                self.label7_1.setText("环境配置")
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
                self.label7_3.setPixmap(QPixmap('simulate3.png'))
                self.label7_3.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label7_3.setAlignment(Qt.AlignCenter)

                self.label7_4 = QtWidgets.QLabel()
                self.label7_4.setTextFormat(QtCore.Qt.AutoText)
                self.label7_4.setText("机器人结构组成展示")
                self.label7_4.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''')
                self.label7_4.setAlignment(Qt.AlignCenter)

                self.label7_5 = QtWidgets.QLabel()
                self.label7_5.setTextFormat(QtCore.Qt.AutoText)
                self.label7_5.setText("仿真环境展示")
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
                    "Q1：用户下达指令后，机器人无法运动\nA1：重新运行该指令\n若成功，则继续向下运行系统\n若机器人仍不运行\n请在下方“联系我们”处查找本设计组的联系方式，我们将为您提供免费的维修服务")
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
                    "Q3：机器人在运动中发生碰撞\nA3：立即使机器人紧急制动\n若机器人能够正常制动，则重新规划路径运行\n若出现机器人仍发生碰撞\n请在下方“联系我们”处查找本设计组的联系方式，我们将为您提供免费的维修服务")
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

            # '联系我们'
            elif i == 10:
                self.centralWidget10 = QtWidgets.QWidget()
                self.centralWidget10.setStyleSheet('''background:white;border-width:0;''');

                self.layout10 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget10.setLayout(self.layout10)

                self.label10_1 = QtWidgets.QLabel()
                self.label10_1.setTextFormat(QtCore.Qt.AutoText)
                self.label10_1.setText("下面是我们几位可爱与机智并存的开发者的联系方式：")
                self.label10_1.setStyleSheet('''color:white;font-size:23px;background:#1E90FF;
                                                font-family:Times new Romans;''');
                self.label10_1.setAlignment(Qt.AlignCenter)

                self.label10_2 = QtWidgets.QLabel()
                self.label10_2.setTextFormat(QtCore.Qt.AutoText)
                self.label10_2.setPixmap(QPixmap('zt.jpeg'))
                self.label10_2.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:10;border-style:outset;border-color:#00BFFF;
                                                font-family:等线;''');
                self.label10_2.setAlignment(Qt.AlignCenter)

                self.label10_3 = QtWidgets.QLabel()
                self.label10_3.setTextFormat(QtCore.Qt.AutoText)
                self.label10_3.setText("组长 邹桃\n邮箱：17373358@buaa.edu.cn\n负责：部分导航模块\n部分UI架构模块\n讨论实现物体检测与抓取\n格言：没有bug！")
                self.label10_3.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''');
                self.label10_3.setAlignment(Qt.AlignCenter)

                self.label10_4 = QtWidgets.QLabel()
                self.label10_4.setTextFormat(QtCore.Qt.AutoText)
                self.label10_4.setPixmap(QPixmap('zzx.jpeg'))
                self.label10_4.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:10;border-style:outset;border-color:#00BFFF;
                                                font-family:等线;''');
                self.label10_4.setAlignment(Qt.AlignCenter)

                self.label10_5 = QtWidgets.QLabel()
                self.label10_5.setTextFormat(QtCore.Qt.AutoText)
                self.label10_5.setText("组员：张稚馨\n邮箱：17373357@buaa.edu.cn\n负责：部分导航模块\n部分UI架构模块\n讨论实现物体检测与抓取\n格言：不想起床")
                self.label10_5.setStyleSheet('''color:black;font-size:23px;background:rgb(00,0,0,0);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''');
                self.label10_5.setAlignment(Qt.AlignCenter)

                self.label10_6 = QtWidgets.QLabel()
                self.label10_6.setTextFormat(QtCore.Qt.AutoText)
                self.label10_6.setPixmap(QPixmap('yc.jpeg'))
                self.label10_6.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,0);
                                                border-width:10;border-style:outset;border-color:#00BFFF;
                                                font-family:等线;''');
                self.label10_6.setAlignment(Qt.AlignCenter)

                self.label10_7 = QtWidgets.QLabel()
                self.label10_7.setTextFormat(QtCore.Qt.AutoText)
                self.label10_7.setText(
                    "组员：杨昶\n邮箱：17373356@buaa.edu.cn\n负责：部分避障与自由行走模块\n部分UI架构模块\n讨论实现物体检测与抓取\n格言：吃饭睡觉乐呵呵")
                self.label10_7.setStyleSheet('''color:black;font-size:23px;background:rgb(0,00,0,0);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''');
                self.label10_7.setAlignment(Qt.AlignCenter)

                self.label10_8 = QtWidgets.QLabel()
                self.label10_8.setTextFormat(QtCore.Qt.AutoText)
                self.label10_8.setPixmap(QPixmap('xyy.jpeg'))
                self.label10_8.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,00,0);
                                                                border-width:10;border-style:outset;border-color:#00BFFF;
                                                                font-family:等线;''');
                self.label10_8.setAlignment(Qt.AlignCenter)

                self.label10_9 = QtWidgets.QLabel()
                self.label10_9.setTextFormat(QtCore.Qt.AutoText)
                self.label10_9.setText("组员：邢译洋\n邮箱：1038927366@qq.com\n负责：部分避障与自由行走模块\n部分UI架构模块\n讨论实现物体检测与抓取\n格言：一只猫猫虫～")
                self.label10_9.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''');
                self.label10_9.setAlignment(Qt.AlignCenter)

                self.label10_10 = QtWidgets.QLabel()
                self.label10_10.setTextFormat(QtCore.Qt.AutoText)
                self.label10_10.setPixmap(QPixmap('gyf.jpeg'))
                self.label10_10.setStyleSheet('''color:black;font-size:23px;background:rgb(00,00,0,0);
                                                 border-width:10;border-style:outset;border-color:#00BFFF;
                                                font-family:等线;''');
                self.label10_10.setAlignment(Qt.AlignCenter)

                self.label10_11 = QtWidgets.QLabel()
                self.label10_11.setTextFormat(QtCore.Qt.AutoText)
                self.label10_11.setText("组员：葛毅飞\n邮箱：gyfhhxx1@163.com\n负责：部分导航模块\n部分UI架构模块\n讨论实现物体检测与抓取\n格言：不掉头发！")
                self.label10_11.setStyleSheet('''color:black;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:5;border-style:ridge;border-color:#1E90FF;
                                                font-family:等线;''');
                self.label10_11.setAlignment(Qt.AlignCenter)

                self.layout10.addWidget(self.label10_1, 1, 1, 1, 6)

                self.layout10.addWidget(self.label10_2, 2, 1)
                self.layout10.addWidget(self.label10_3, 3, 1, 2, 1)

                self.layout10.addWidget(self.label10_4, 2, 2)
                self.layout10.addWidget(self.label10_5, 3, 2, 2, 1)

                self.layout10.addWidget(self.label10_6, 2, 3)
                self.layout10.addWidget(self.label10_7, 3, 3, 2, 1)

                self.layout10.addWidget(self.label10_8, 2, 4)
                self.layout10.addWidget(self.label10_9, 3, 4, 2, 1)

                self.layout10.addWidget(self.label10_10, 2, 5)
                self.layout10.addWidget(self.label10_11, 3, 5, 2, 1)

                self.right_widget.addWidget(self.centralWidget10)

            else:
                if i != 0 and i != 4 and i != 8:
                    self.centralWidget0 = QtWidgets.QWidget()
                    self.centralWidget0.setStyleSheet('''background:white;border-width:0;''');
                    self.right_widget.addWidget(self.centralWidget0)

    def button1_1click(self):
        vel = 0
        time = 0
        # 设置运行的速度，default值是0.5
        if self.edit1_1.text() == "":
            vel = 0.5
        else:
            vel = float(self.edit1_1.text())

        # 设置运行的时间，default值是0.5
        if self.edit1_2.text() == "":
            time = 60
        else:
            time = int(self.edit1_2.text())

        self.setConfig(vel, time)

        print("roslaunch wpb_home_apps 6_path_plan.launch")
        free_walk_cmd = "gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials 6_path_plan.launch\"'"
        os.system(free_walk_cmd)

    # 增加按钮一点击调用的函数
    def button1_0click(self):
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&source ./devel/setup.bash&&export SVGA_VGPU10=0&&roslaunch robot_sim_demo robot_spawn.launch\"'")

    # 增加按钮2——1点击调用的函数
    def button2_1click(self):
        print("roslaunch wpb_home_tutorials gmapping.launch")
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&source ./devel/setup.bash&&roslaunch wpb_home_tutorials gmapping.launch\"'")

    # 增加按钮2——7点击调用的函数
    def button2_7click(self):
        print("rosrun robot_sim_demo keyboard_vel_ctrl")
        # os.system("rosrun robot_sim_demo keyboard_vel_ctrl")
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&source ./devel/setup.bash&&rosrun robot_sim_demo keyboard_vel_ctrl\"'")
    def button2_8click(self):
        print("roslaunch xfyun_waterplus voice_cmd_wpb_home.launch")
        os.system("gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&source ./devel/setup.bash&&roslaunch xfyun_waterplus voice_cmd_wpb_home.launch\"'")

    # 增加按钮2_2点击调用的函数
    def button2_2click(self):
        print("rosrun map_server map_saver -f map")
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&source ./devel/setup.bash&&rosrun map_server map_saver -f map&&cp map.yaml ~/demo_ws/src/wpb_home/wpb_home_tutorials/maps/map.yaml&&cp map.pgm ~/demo_ws/src/wpb_home/wpb_home_tutorials/maps/map.pgm\"'")

    # 增加按钮2_3点击调用的函数
    def button2_3click(self):
        print("roslaunch waterplus_map_tools add_waypoint.launch")
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&roslaunch waterplus_map_tools add_waypoint.launch\"'")

    # 增加按钮2_4点击调用的函数
    def button2_4click(self):
        print("rosrun waterplus_map_tools wp_saver")
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&cd ~/demo_ws/&&source ./devel/setup.bash&&rosrun waterplus_map_tools wp_saver\"'")
        time.sleep(2)
        self.comboBox2.clear()
        if os.path.exists('~/demo_ws/waypoints.xml') == False:
            file = open('~/demo_ws/waypoints.xml', 'w')
            file.write('<Waterplus>\n</Waterplus>')
            file.close()
        f = open('~/demo_ws/waypoints.xml', 'r')
        newFile = re.sub(r"(?<=<Name>).+?(?=</Name>)", indexRename, f.read())
        f.close()
        f = open('~/demo_ws/waypoints.xml', 'w')
        f.write(newFile)
        f.close()
        self.renameIndex = 1
        f = open('~/demo_ws/waypoints.xml', 'r')
        pointlist = re.findall(r"(?<=<Name>).+?(?=</Name>)", f.read(), re.S)
        print(pointlist)
        self.comboBox2.addItems(pointlist)
        f.close()

    # 增加按钮2_5点击调用的函数
    def button2_5click(self):
        print("roslaunch waterplus_map_tools wpb_home_nav_test.launch")
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&cd ~/demo_ws/&&source ./devel/setup.bash&&roslaunch waterplus_map_tools wpb_home_nav_test.launch; exec bash\"'")
        print("rosrun waterplus_map_tools wp_nav_test")
        os.system(
            "gnome-terminal -e 'bash -c \"cd ~/demo_ws/&&cd ~/demo_ws/&&source ./devel/setup.bash&&rosrun waterplus_map_tools wp_nav_test; exec bash\"'")

    # 增加按钮2_6点击调用的函数
    def button2_6click(self):
        print(self.comboBox2.currentIndex() + 1)
        # get to the chosed point
        pointoutput = open('~/demo_ws/point.txt', 'w')
        pointoutput.write(str(self.comboBox2.currentIndex() + 1))
        pointoutput.close()


def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec_()


if __name__ == '__main__':
    main()
