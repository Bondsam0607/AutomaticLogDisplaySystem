import sys
import argparse
import pandas as pd

from PyQt5.QtWidgets import *
from main_window import MainWindow
from main_widget import Widget
from extract_sql import Extract_SQL


if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)
    
    widget = Widget()
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())