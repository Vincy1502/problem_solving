#method 1
length=int(input())
a=[]
b=[]
c=[]
for i in range(length):
    num=int(input())
    a.append(num)
for k in a:
   if k in b:
      c.append(k)
   elif k not in b:
      b.append(k)
d=set(c)
for j in d:       
   print(j,"repeates",a.count(j),"times")

#method 2
charlength=int(input())
a=[]
b=[]


for i in range(charlength):
    numbers=int(input())
    a.append(numbers)
    b=[0]*10
    for num in a:
      value=(num)-1
      b[value] += 1
for j in range(len(b)):
  if b[j] != 0:
    print((j+1),":",b[j])




    

      
