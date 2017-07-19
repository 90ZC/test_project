#题目：输入三个整数x,y,z，请把这三个数由小到大输出
import Tools.Scripts.treesync as tst
c=tst.raw_input("请输入三个数并以“,”分隔：")
list=c.split(',')
for j in range(2):
    for i in range(2):
        a = int(list[i])
        b = int(list[i+1])
        if a>=b:
            a,b=b,a
            list[i]=a
            list[i+1]=b
            print(list)



