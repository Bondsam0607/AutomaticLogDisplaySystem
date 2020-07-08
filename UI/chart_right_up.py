import sys
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis, QBarSeries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from extract_sql import Extract_SQL
import time
import CONF
import chart_bottom


class BackendThread(QThread):
    update_bar = pyqtSignal(list)
    def __init__(self):
        QThread.__init__(self)
        self.data = []

    def run(self):
        while True:
            accNum = Extract_SQL().fetchSectionFail(chart_bottom.sectionMark)
            if self.data != accNum:
                self.data = accNum
                self.update_bar.emit(self.data)
            time.sleep(CONF.RefreshTime[3])

class TopFailSection(QChartView):
    def __init__(self):
        QChartView.__init__(self)
        #self.resize(300,300)
        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_bar.connect(self.handleBar)
        self.backend.start()

    def handleBar(self, data):
        self.series = QBarSeries()
        self.series.clear()
        self.chart = QChart()
        self.chart.setTitle(CONF.rightUpNames[0])
        set0 = QBarSet(CONF.rightUpNames[1])

        for i in range(len(data)):
            set0 << data[i][1]

        self.series.append(set0)
 
        self.chart.addSeries(self.series)
        categories = [data[i][0] for i in range(len(data))]
        print(categories)
        axis = QBarCategoryAxis()
        axis.append(categories)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(axis, self.series)

 

        self.setChart(self.chart)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = TopFailSection()
    view.show()
    sys.exit(app.exec_())











