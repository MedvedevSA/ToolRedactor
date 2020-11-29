
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

        self._list_Type_Tool = [    "CLASS END_MILL_NON_INDEXABLE",
                                    "CLASS SPIRAL_DRILL"]
    
        self._cur_Type_Tool = self._list_Type_Tool[0] 

        self._list_hidden_row = []
        ## Tool list load to tableWidget
        ########################################################################
        UIFunctions.ViewListTool(self)
        
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        
        ## PAGES
        ########################################################################
        
        # PAGE 1
        
        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))

        self.ui.DelBtn.clicked.connect(lambda: UIFunctions.delRowData(self))
        self.ui.ResetBtn.clicked.connect(lambda: UIFunctions.ViewListTool(self))
        
        
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
        saveFile = contextMenu.addAction("Save File")

        action = contextMenu.exec_(self.mapToGlobal (event.pos()))

        if action == delRow:
            UIFunctions.delRowData(self)
        
        if action == saveFile:
            UIFunctions.updateToolDBfile(self)
            
        

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")

#"""------------------------------------------------------------handleItemClicked-------------------------"""
#"""------------------------------------------------------------handleItemClicked-------------------------"""
    # Ивент включающийся по нажатию на чек бокс
    ############################
    def handleItemClicked(self, item):
        self._list_hidden_row = set(self._list_hidden_row)
        self._list_hidden_row = list(self._list_hidden_row)
        
        if item.checkState() == QtCore.Qt.Checked:
            self._list_hidden_row.append(item.row())
            print(self._list_hidden_row)
            self.DataTool[item.row()][0] = "#DATA " 
        elif item.checkState() == QtCore.Qt.Unchecked:
            try:
                self._list_hidden_row.pop(self._list_hidden_row.index(item.row()))
                print(self._list_hidden_row)
                self.DataTool[item.row()][0] = "DATA " 

            except:
                print()

        



stylesheet = """
 /* --------------------------------------- QScrollBar  -----------------------------------*/
 QScrollBar:horizontal
 {
     height: 15px;
     margin: 3px 15px 3px 15px;
     border: 1px transparent #2A2929;
     border-radius: 4px;
     background-color: yellow;    /* #2A2929; */
 }

 QScrollBar::handle:horizontal
 {
     background-color: #c1c1c1;      /* #605F5F; */
     min-width: 5px;
     border-radius: 4px;
 }

 QScrollBar::add-line:horizontal
 {
     margin: 0px 3px 0px 3px;
     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
     width: 10px;
     height: 10px;
     subcontrol-position: right;
     subcontrol-origin: margin;
 }

 QScrollBar::sub-line:horizontal
 {
     margin: 0px 3px 0px 3px;
     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
     height: 10px;
     width: 10px;
     subcontrol-position: left;
     subcontrol-origin: margin;
 }

 QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
 {
     border-image: url(:/qss_icons/rc/right_arrow.png);
     height: 10px;
     width: 10px;
     subcontrol-position: right;
     subcontrol-origin: margin;
 }


 QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
 {
     border-image: url(:/qss_icons/rc/left_arrow.png);
     height: 10px;
     width: 10px;
     subcontrol-position: left;
     subcontrol-origin: margin;
 }

 QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
 {
     background: none;
 }


 QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
 {
     background: none;
 }

 QScrollBar:vertical
 {
     background-color: #c1c1c1;
     width: 15px;
     margin: 15px 3px 15px 3px;
     border: 1px transparent #c1c1c1;
     border-radius: 4px;
 }

 QScrollBar::handle:vertical
 {
     background-color: #c1c1c1;         /* #605F5F; */
     min-height: 5px;
     border-radius: 4px;
 }

 QScrollBar::sub-line:vertical
 {
     margin: 3px 0px 3px 0px;
     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
     height: 10px;
     width: 10px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }

 QScrollBar::add-line:vertical
 {
     margin: 3px 0px 3px 0px;
     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
     height: 10px;
     width: 10px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
 {

     border-image: url(:/qss_icons/rc/up_arrow.png);
     height: 10px;
     width: 10px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }


 QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
 {
     border-image: url(:/qss_icons/rc/down_arrow.png);
     height: 10px;
     width: 10px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
 {
     background: none;
 }


 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
 {
     background: none;
 }

 """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet) 
    window = MainWindow()
    sys.exit(app.exec_())
