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
