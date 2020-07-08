import matplotlib.pyplot as plt
from wordcloud import WordCloud
from extract_sql import Extract_SQL
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time
import CONF
import chart_bottom

class BackendThread(QThread):
    update_cloud = pyqtSignal(dict)
    def __init__(self):
        QThread.__init__(self)
        self.data = []

    def run(self):
        while True:
            accNum = Extract_SQL().fetchCaseName(chart_bottom.sectionMark)
            if self.data != accNum:
                self.data = accNum
                self.update_cloud.emit(self.data)
            time.sleep(CONF.RefreshTime[4])

class Cloud(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		#self.resize(300,400)
		self.layout=QVBoxLayout()
		self.pic = QLabel()
		self.layout.addWidget(self.pic)
		self.initUI()

	def initUI(self):
		self.backend = BackendThread()
		self.backend.update_cloud.connect(self.handleCloud)
		self.backend.start()

	def handleCloud(self, data):

		wc = WordCloud(
		# 设置字体，不指定就会出现乱码
		# 设置背景色
		background_color='white',
		# 设置背景宽
		width=400,
		# 设置背景高
		height=230,
		# 最大字体
		max_font_size=CONF.maxFontSize,
		# 最小字体
		min_font_size=CONF.minFontSize,
		max_words=CONF.maxWords,
		repeat=False
		#mode='RGBA'
		#colormap='pink'
		)
		if data != {}:
			wc.fit_words(data)
		else:
			wc.fit_words({'There':2, 'Is':1, 'NO':15, 'Data':10})
		wc.to_file(r"wordcloud.png")

		self.pic.setPixmap(QPixmap(r"wordcloud.png"))

		self.setLayout(self.layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Cloud()
    demo.show()
    sys.exit(app.exec_())







