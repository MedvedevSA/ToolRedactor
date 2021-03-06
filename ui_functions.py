
## ==> GUI FILE
from main import *


class comboCompanies(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 25px')
        self.addItems(['Microsoft', 'Facebook', 'Apple', 'Google'])
        self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())
        # return self.currentText()

class UIFunctions(MainWindow):
    
    #Функция анимирования при нажатии на кнопу Toggle
    def toggleMenu(self, maxWidth, enable):
        if enable:
#"""------------------------------------------------------------toggleMenu-------------------------"""
#"""------------------------------------------------------------toggleMenu-------------------------"""

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

#"""------------------------------------------------------------loadDrill-------------------------"""
#"""------------------------------------------------------------loadDrill-------------------------"""
    # Загрузка массива сверел 
    def loadDrill (self): 
        str_open = self._cur_Type_Tool
        str_close = "END_DATA"
        
        fg_transfer = 0
        data_str = []

        with open("tool_database.dat", "r", encoding='utf-8') as data_file:
            data_str = data_file.readlines()
    
        item_list = []
        index = 0
        for line in data_str:
            
            if fg_transfer and "DATA" in line and not "#END_DATA" in line:
                if line[0] == '#' :
                    self._list_hidden_row.append(index)
                index += 1

            if  line.find(str_open) > 0 :
                fg_transfer = 1

            elif line.find(str_close) > 0 and fg_transfer:
                fg_transfer = 2

            if fg_transfer == 1 and "DATA" in line:
                item_list.append(line.split("|"))

            elif fg_transfer == 2:
                break

            
        data_str.clear()

        return item_list


#"""------------------------------------------------------------updateToolDBfile-------------------------"""
#"""------------------------------------------------------------updateToolDBfile-------------------------"""
    def updateToolDBfile (self):
        str_open = self._cur_Type_Tool
        str_close = "END_DATA"

        fg_transfer = 0
        data_str = []

        with open("tool_database.dat", "r", encoding='utf-8') as data_file:
            for line in data_file: 

                if  line.find(str_open) > 0 :
                    data_str.append(line)
                    fg_transfer = 1

                    # Update data from self.DataTool
                    ####################################################
                    
                    for upd_str in self.DataTool :
                        data_str.append("|".join(upd_str)+"\n")
                    
                    #data_str.append(f"#{str_close}\n")

                    continue
                
                if line.find(str_close) > 0 :
                    fg_transfer = 0

                if fg_transfer == 0:
                    data_str.append(line)
    

        with open("tool_database_new.dat", "w", encoding='utf-8') as data_file:
                data_file.writelines(data_str)

            
#"""------------------------------------------------------------delRowData-------------------------"""
#"""------------------------------------------------------------delRowData-------------------------"""
    def delRowData(self):
        cur_row = self.ui.ToolTable.currentRow()
        self.ui.ToolTable.removeRow(cur_row)
        self.DataTool.pop(cur_row)
        #print(self.ui.ToolTable.item(1,1).text())


    
#"""------------------------------------------------------------ViewListTool-------------------------"""
#"""------------------------------------------------------------ViewListTool-------------------------"""
    def ViewListTool(self):
        tmp = []
        for i in range(0,34):
            tmp.append(i)
        tmp_str = []
        for i in range(0,34):
            tmp_str.append(str(i))

        name = self._cur_Type_Tool
        
        dict_row_col =      {   "CLASS SPIRAL_DRILL" : [ 2, 15, 17 ,20 , 21, 28, 29, 30, 33 ],
                                "CLASS END_MILL_NON_INDEXABLE" : tmp}
        dict_head_table =   {   "CLASS SPIRAL_DRILL" : [ "Название", "D", "L" ,"FL" , "PA", "SD", "SL", "STL", "ART", "Hiden" ],
                                "CLASS END_MILL_NON_INDEXABLE" : tmp_str}


        T_List = UIFunctions.loadDrill(self)
                                                    # Плюс комбо бокс
        width = len(dict_row_col[name]) + 1         #############
        height = len(T_List)

        self.ui.ToolTable.setColumnCount( width )
        self.ui.ToolTable.setRowCount( height )


        row = 0

        for tup in T_List:
            col = 0
            # Вносит соответствующее номеру столбца из словаря значение
            ##############################################
            for index in dict_row_col[name]:
                if len(T_List[row]) > width:

                    if "\n" in T_List[row][index-1] :
                        T_List[row][index-1] = T_List[row][index-1].replace ("\n","")
                    
                    if is_digit( T_List[row][index-1] ):
                        cellinfo = QTableWidgetItem("{0:.3f}".format(float( T_List[row] [index-1] ) ) )
                    
                    else :
                        cellinfo = QTableWidgetItem(T_List[row][index-1])

                    self.ui.ToolTable.setItem(row, col, cellinfo)
            
                    col += 1

                else:
                    break

            ## в строку последним элементом добаваляет чекбокс
            ######################################################
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                            QtCore.Qt.ItemIsEnabled)
            
            if row in self._list_hidden_row:
                item.setCheckState(QtCore.Qt.Checked)
            else :    
                item.setCheckState(QtCore.Qt.Unchecked)
            
            self.ui.ToolTable.setItem(row, width-1, item)


            row += 1
        

        # Асссоциирование клика с вызовом handleItemClicked
        ###############################
        self.ui.ToolTable.itemClicked.connect(self.handleItemClicked)

        self.ui.ToolTable.setHorizontalHeaderLabels(dict_head_table[name])
        for col in range(0,len(dict_row_col[name])):
            self.ui.ToolTable.setColumnWidth(col, 6*len(T_List[2] [dict_row_col[name][col]-1]))
        
        self.ui.ToolTable.setColumnWidth(width-1,30)
        
        self.DataTool = T_List








 ########################################################
def is_digit(string) :
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False