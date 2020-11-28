
## ==> GUI FILE
from main import *

class UIFunctions(MainWindow):
    
    #Функция анимирования при нажатии на кнопу Toggle
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    # Загрузка массива сверел 
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

    def ViewListTool(self):

        """T_List = [ [["1:1"],["1:2"],["1:3"],],
                   [["2:1"],["2:2"],["2:3"],],
                   [["3:1"],["3:2"],["3:3"],]]
        """
        T_List = UIFunctions.loadDrill()

        width = len(T_List[2])
        height = len(T_List)

        self.ui.ToolTable.setColumnCount( width )
        self.ui.ToolTable.setRowCount( height )


        row = 0
        for tup in T_List:
            col = 0
 
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.ui.ToolTable.setItem(row, col, cellinfo)
                col += 1
 
            row += 1

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")
 