from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

sectionMark = 0

class BottomView(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.button = QRadioButton("主界面")
		self.button.setChecked(True)
		self.button1 = QRadioButton("Section1")
		self.button1.setChecked(False)
		self.button2 = QRadioButton("Section2")
		self.button2.setChecked(False)


		self.button.toggled.connect(self.changeMark)
		self.button1.toggled.connect(self.changeMark)
		self.button2.toggled.connect(self.changeMark)

		self.layout = QHBoxLayout()
		self.layout.addWidget(self.button)
		self.layout.addWidget(self.button1)
		self.layout.addWidget(self.button2)

		self.setLayout(self.layout)

	def changeMark(self):
		global sectionMark
		if self.button.isChecked():
			sectionMark = 0
		if self.button1.isChecked():
			sectionMark = 1
		if self.button2.isChecked():
			sectionMark = 2

if __name__ == '__main__':
	app = QApplication(sys.argv)
	view = BottomView()
	view.show()
	sys.exit(app.exec_())