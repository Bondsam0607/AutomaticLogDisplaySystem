import sys
import random
from PyQt5.QtChart import QDateTimeAxis,QValueAxis,QLineSeries,QChart,QChartView
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from extract_sql import Extract_SQL
import time
import CONF
import chart_bottom



class BackendThread(QThread):
    update_line = pyqtSignal(list)
    def __init__(self):
        QThread.__init__(self)
        self.data = []

    def run(self):
        extract = Extract_SQL()
        while True:
            accNum = extract.fetchCount(chart_bottom.sectionMark)
            print(accNum)
            if self.data != accNum: 
                self.data = accNum
                self.update_line.emit(self.data)
            time.sleep(CONF.RefreshTime[0])

class ChartView(QChartView):
    def __init__(self):
        QChartView.__init__(self)
        #self.resize(300, 300)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.chart = QChart()
        self.seriesAcc = QLineSeries()
        self.seriesAcc.setName(CONF.leftUpNames[0])
        self.chart.addSeries(self.seriesAcc)
        #声明并初始化X轴，Y轴
        self.dtaxisX = QValueAxis()
        self.vlaxisY = QValueAxis()
        #设置坐标轴显示范围
        self.dtaxisX.setMin(0)
        #self.dtaxisX.setMax(100)
        self.vlaxisY.setMin(0)
        #self.vlaxisY.setMax(100)
        self.dtaxisX.setTickCount(3)
        self.vlaxisY.setTickCount(3)
        #设置坐标轴名称
        self.dtaxisX.setTitleText(CONF.leftUpNames[1])
        self.vlaxisY.setTitleText(CONF.leftUpNames[2])
        #设置网格不显示
        self.vlaxisY.setGridLineVisible(False)
        #把坐标轴添加到chart中
        self.chart.addAxis(self.dtaxisX,Qt.AlignBottom)
        self.chart.addAxis(self.vlaxisY,Qt.AlignLeft)

        self.seriesAcc.attachAxis(self.dtaxisX)
        self.seriesAcc.attachAxis(self.vlaxisY)

        self.initUI()


    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_line.connect(self.handleLine)
        self.backend.start()

    def handleLine(self, data):
        if data[0] == 0:
            self.seriesAcc.clear()
        else:
            self.dtaxisX.setMax(data[0])
            self.vlaxisY.setMax(data[0])
            self.seriesAcc.clear()
            self.seriesAcc.append(0, 0)
            self.seriesAcc.append(data[0], data[1])




        self.setChart(self.chart)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = ChartView()
    view.show()
    sys.exit(app.exec_())

