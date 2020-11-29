test = "DATA |MILL-APPLITEC-3271-3-2.5|2|1|1|1| Твердосплавная фреза DIAMETER | TMC0_00001 | High Speed Steel |0|0|0|||2.5|2|7.5| 0.00000 |3|7|0|0|0|0| 0.00000 | 0.00000 | 1.0 |3|31.5|1.18|15| 90.00000%T | 70.00000%T | 50.00000%T||"
list_ = []
for i in range(0,31):
    list_.append(str(i))
d = {"key" : list_}

print (d["key"])

#print(list_)
