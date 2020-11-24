import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QComboBox, QPushButton)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QSize
from GUI import Ui_MainWindow


def loadDrill (): 
    str_open = "CLASS SPIRAL_DRILL"
    str_close = "END_DATA"
    
    fg_transfer = 0
    data_str = []

    with open("tool_database.dat", "r", encoding='utf-8') as data_file:
        data_str = data_file.readlines()

    item_list = []
    for line in data_str:

        if  line.find(str_open) > 0 :
            fg_transfer = 1

        elif line.find(str_close) > 0 and fg_transfer:
            fg_transfer = 2

        if fg_transfer == 1 and not line[0] == '#':
            item_list.append(line.split("|"))

        elif fg_transfer == 2:
            break

    data_str.clear()

    return item_list


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonYAP.clicked.connect(self.btnClicked)


    def btnClicked(self):
        loadDrill()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())