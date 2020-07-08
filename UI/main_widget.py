import time
from table_model import CustomTableModel
from extract_sql import Extract_SQL
import pandas as pd
import random
from chart_left_up import ChartView
from chart_left_down import BarView
from chart_mid import dataTable
from chart_right_up import TopFailSection
from chart_right_down import Cloud
from chart_bottom import BottomView
from clock import clock
from Title import title
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)


        ############ 左边layout设置 ##############

        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(title())
        self.left_layout.addWidget(ChartView())
        self.left_layout.addWidget(BarView())

        ############ 左边layout设置结束 ##############


        ############ 右边layout设置 ##############

        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(clock())
        self.right_layout.addWidget(TopFailSection())
        self.right_layout.addWidget(Cloud())

        ############ 右边layout设置结束 ##############

        self.main_layout = QHBoxLayout()
        self.left = QWidget()
        self.right = QWidget()

        self.left.setLayout(self.left_layout)
        self.left.resize(400,900)
        self.right.setLayout(self.right_layout)
        self.right.resize(400,900)

        self.main_layout.addWidget(self.left)
        self.main_layout.addWidget(dataTable())
        self.main_layout.addWidget(self.right)

        self.up_layout = QWidget()
        self.up_layout.setLayout(self.main_layout)

        self.whole_layout = QVBoxLayout()
        self.whole_layout.addWidget(self.up_layout)
        self.whole_layout.addWidget(BottomView())

        # Set the layout to the QWidget
        self.setLayout(self.whole_layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Widget()
    view.show()
    sys.exit(app.exec_())
    