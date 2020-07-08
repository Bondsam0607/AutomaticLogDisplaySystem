import time
from table_model import CustomTableModel
from extract_sql import Extract_SQL
import pandas as pd
import random
from chart_left_up import ChartView
import sys
import CONF
import chart_bottom
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class BackendThread(QThread):
    update_sql = pyqtSignal(pd.DataFrame)
    update_num = pyqtSignal(list)
    def __init__(self):
        QThread.__init__(self)
        self.data = [["Null", "Null", "Null", "Null", "Null"]]
        self.accNum = [0,0,0,0]


    def run(self):
        #print(self.data)
        while True:
            dataTmp = Extract_SQL().fetch(chart_bottom.sectionMark)
            #print(dataTmp)
            accNumTmp = Extract_SQL().fetchCount(chart_bottom.sectionMark)
            #print(accNumTmp)
            if dataTmp != self.data:
                self.data = dataTmp
                self.update_sql.emit(pd.DataFrame(self.data))
            if self.accNum != accNumTmp:
                self.accNum = accNumTmp
                print(self.accNum)
                self.update_num.emit(self.accNum)
            time.sleep(CONF.RefreshTime[2])




class dataTable(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        ############ 中间layout设置 ##############
        # 表格设置
        self.table_view = QTableView()
        self.horizontal_header = self.table_view.horizontalHeader()
        self.vertical_header = self.table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.horizontal_header.setStretchLastSection(True)

        # 上方统计设置
        self.labelAccumulateCaseNum = QLabel()
        self.labelAccumulateFailNum = QLabel()
        self.labelCurrCaseNum = QLabel()
        self.labelCurrFailNum = QLabel()

        self.upper_layout = QHBoxLayout()
        self.upper_layout.addWidget(self.labelAccumulateCaseNum)
        self.upper_layout.addWidget(self.labelAccumulateFailNum)
        self.upper_layout.addWidget(self.labelCurrCaseNum)
        self.upper_layout.addWidget(self.labelCurrFailNum)
        self.upper = QWidget()
        self.upper.setLayout(self.upper_layout)

        # 中间layout，包括上方统计显示和下方表格
        self.mid_layout = QGridLayout()
        self.mid_layout.setSpacing(10)
        self.mid_layout.addWidget(self.upper,3,0)
        self.mid_layout.addWidget(self.table_view,5,0)
        ############ 中间layout设置结束 ##############

        self.initUI()
        self.setLayout(self.mid_layout)


    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_sql.connect(self.handleDisplay)
        self.backend.update_num.connect(self.handleNum)
        self.backend.start()

    def handleDisplay(self, data):
        model = CustomTableModel(data)
        self.table_view.setModel(model)

    def handleNum(self, data):
        self.labelAccumulateCaseNum.setText("累计Case数： "+str(data[0]))
        self.labelAccumulateFailNum.setText("累计Fail数： "+str(data[1]))
        self.labelCurrCaseNum.setText("当前Case数： "+str(data[2]))
        self.labelCurrFailNum.setText("当前Fail数： "+str(data[3]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = dataTable()
    view.show()
    sys.exit(app.exec_())