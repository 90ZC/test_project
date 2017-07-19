'''有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
import string as str

for i in range(1,5):
    list = [1, 2, 3, 4]
    del list[i-1]
    #print(i)
    #print(list)
    for j in list:
        list2=[list[0],list[1],list[2]]
     #   print(list2)
        list2.remove(j)
      #  print(list2)
        print(j*100+list2[0]*10+list2[1])
        print(j * 100 + list2[1] * 10 + list2[0])
