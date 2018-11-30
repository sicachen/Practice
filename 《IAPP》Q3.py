#1~100张写了数字的牌，从第2张开始，隔1张翻牌；从第3张开始，隔2张翻牌；直到没有可翻动的牌为止。求所有背面朝上的牌的数字。
a=[False]*100 #列表重复数量在[]外面
n=1
i=2
while i<100:
    while n<100:
        a[n]=not a[n]
        n=n+i
    i=i+1   
    n=i-1   #i的值在变，起始n的值也是变化的
print(a)
for x in range(0,100):  #列表中有bool值不能用index
    if a[x]==False:
        y=x+1
        print(y)
    x=x+1

'''
n1=2
i1=n1+1
while n1<10:
    if a[n1]==True:
        a[n1]= not True
    else:
        a[n1]= not False
    n1=n1+i1
    print(a)
n2=3
i2=n2+1
while n2<10:
    if a[n2]==True:
        a[n2]= not True
    else:
        a[n2]=not False
    n2=n2+i2
    print(a)'''