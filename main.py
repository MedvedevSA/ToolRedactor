
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        ## Tool list load to tableWidget
        ########################################################################
        self.DataTool = UIFunctions.ViewListTool(self)
        
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        
        ## PAGES
        ########################################################################
        
        # PAGE 1
        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.Btn_Menu_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.Btn_Menu_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
            
        self.show()
        ## ==> END ##

    def contextMenuEvent(self, event) :
        contextMenu = QMenu(self)   

        delRow = contextMenu.addAction("Delete row")

        action = contextMenu.exec_(self.mapToGlobal (event.pos()))

        if action == delRow:
            cur_row = self.ui.ToolTable.currentRow()
            print(self.ui.ToolTable.item(1,1).text())
            self.ui.ToolTable.removeRow(cur_row)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
