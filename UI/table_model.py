from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import *
import CONF


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        self.input_section = data[0].values
        self.input_case = data[1].values
        self.input_result = data[2].values
        self.input_status = data[3].values
        self.input_time = data[4].values


        self.column_count = 5
        self.row_count = len(self.input_result)

    # virtual functions

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return (CONF.tableColumnName[0], CONF.tableColumnName[1], CONF.tableColumnName[2], CONF.tableColumnName[3], CONF.tableColumnName[4])[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            if column == 0:
                raw_name = self.input_section[row]
                return raw_name
            elif column == 1:
                return self.input_case[row]
            elif column == 2:
                return self.input_result[row]
            elif column == 3:
                return self.input_status[row]
            elif column == 4:
                return self.input_time[row]
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None
