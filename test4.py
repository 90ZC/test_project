#输入某年某月某日，判断这一天是这一年的第几天？
import calendar
import Tools.Scripts
import time
import Tools.Scripts.treesync as tl
list1=[1,2,3,4,5,6,7,8,9,10,11,12]
list2=[31,0,31,30,31,30,31,31,30,31,30,31]
while True:
    d=tl.raw_input("查询日期")
    d=d.replace('-','')
    d=d.replace('/','')
    year=d[0:4]
    month=d[4:6]
    day=d[6:8]
    c=0
    if calendar.isleap(int(year)):
        for i in range(1,int(month)):
            c+=list2[i-1]
        if int(month)>2:
            c+=29
    else:
        for i in range(1,int(month)):
            c+=list2[i-1]
        if int(month)>2:
            c+=28
    print(c+int(day))

