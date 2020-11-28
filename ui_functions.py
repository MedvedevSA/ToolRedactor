
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

    def updateToolDBfile (self):
        str_open = "CLASS SPIRAL_DRILL"
        str_close = "END_DATA"

        fg_transfer = 0
        data_str = []

        with open("tool_database.dat", "r", encoding='utf-8') as data_file:
            for line in data_file: 

                line = data_file.readline()
                if  line.find(str_open) > 0 :
                    data_str.append(line)
                    fg_transfer = 1

                    # Update data from self.DataTool
                    ####################################################
                    
                    for upd_str in self.DataTool :
                        data_str.append("|".join(upd_str))
                    
                    data_str.append(f"#{str_close}\n")

                    continue
                
                if line.find(str_close) > 0 :
                    fg_transfer = 0

                if fg_transfer == 0:
                    data_str.append(line)
    

        with open("tool_database_new.dat", "w", encoding='utf-8') as data_file:
                data_file.writelines(data_str)

            
            
    def delRowData(self):
        
        cur_row = self.ui.ToolTable.currentRow()
        self.ui.ToolTable.removeRow(cur_row)
        self.DataTool.pop(cur_row)
        #print(self.ui.ToolTable.item(1,1).text())


    def ViewListTool(self):

        name = "CLASS SPIRAL_DRILL"
        dict_row_col = {"CLASS SPIRAL_DRILL" : [2, 15, 17 ,20 , 21, 28, 29, 30]}
        
        T_List = UIFunctions.loadDrill()

        width = len(dict_row_col[name])
        height = len(T_List)

        self.ui.ToolTable.setColumnCount( width )
        self.ui.ToolTable.setRowCount( height )


        row = 0

        for tup in T_List:
            col = 0
 
            for index in dict_row_col[name]:
                if len(T_List[row]) > width:

                    cellinfo = QTableWidgetItem(T_List[row][index-1])
                    self.ui.ToolTable.setItem(row, col, cellinfo)
                    col += 1
                else:
                    break
            row += 1
            
        return T_List
    

 