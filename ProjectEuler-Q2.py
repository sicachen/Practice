#Fibonacci序列是第x个数=（x-1）+（x-2），求小于4百万的序列中偶数之和
a=[1,2]
c=0
x=0
while c < 4000000:
    c=a[x]+a[x+1]
    a.append(c)
    x=x+1
x=0
b=[0]
while a[x]<4000000:
    c=int(a[x]) #注意将列表转换为数值型
    if c%2==0:
        b.append(a[x])
    x=x+1
f=sum(b)
print(f)