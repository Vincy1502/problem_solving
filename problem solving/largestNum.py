length=int(input())#4
a=[]
for i in range(length):
     numbers=int(input())
     a.append(numbers)
print(a)
for i in range(len(a)):
     for j in range(0,len(a)-i-1):
          if a[j]<a[j+1]:
               temp=a[j]
               print(temp)
               a[j]=a[j+1]
               print(a[j])
               a[j+1]=temp
               print(a[j+1])
print(a)
print(a[0])
