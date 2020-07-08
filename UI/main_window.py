from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import CONF


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)

        self.setWindowTitle(CONF.windowName)
        self.resize(1500,700)
        self.setCentralWidget(widget)


