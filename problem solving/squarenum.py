num=int(input())
a=num
root=[]
square=""
while a>0:
    digit=a%10
    sroot=digit**2
    root.append(sroot)
    a=a//10
for i in root:
    square=str(i)+square
print(square)

