'''题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？'''
from Tools.Scripts.treesync import raw_input

c=raw_input('此次利润：')
I=float(c)
list=[1000000,600000,400000,200000,100000]
list2=[400000,200000,200000,100000,100000]
list3=[0.01,0.015,0.03,0.05,0.075,0.1]
d=0
for i in range(len(list)) :
    if I-list[i] >=0 :
        d+=(I-list[i])*list3[i]
        for j in range(len(list2)):
            d+=list2[j]*list3[j+1]
    break
print(d)