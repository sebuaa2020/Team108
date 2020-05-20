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

       

def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec()


if __name__ == '__main__':
    main()
