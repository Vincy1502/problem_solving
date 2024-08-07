num=int(input())
a=num
b=[]
binary=""
while a>0:
    digit=a%2
    b.append(digit)
    a=a//2
print(b)
for i in b:
    binary=str(i)+binary
print(binary)

 
    
