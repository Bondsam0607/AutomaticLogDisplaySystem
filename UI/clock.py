import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class BackendThread(QThread):
    update_time = pyqtSignal(str)
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            self.update_time.emit(t)
            time.sleep(1)


class clock(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.label = QLabel()
		layout = QHBoxLayout()
		layout.addWidget(self.label)
		self.setLayout(layout)
		self.initUI()

	def initUI(self):
		self.backend = BackendThread()
		self.backend.update_time.connect(self.handleTime)
		self.backend.start()

	def handleTime(self,data):
		self.label.setText(data)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	view = clock()
	view.show()
	sys.exit(app.exec_())



