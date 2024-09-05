num=int(input("enter the length:"))
a=0
b=1
while num>0:
    temp=a
    a=b
    b=temp+b
    num-=1
print(a)

