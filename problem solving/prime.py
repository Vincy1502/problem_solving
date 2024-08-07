#prime interval
num=int(input("enter the number:"))

a=[]
b=[]

for n in range(1,num+1):#5 1,2,3,4,5
  if n>1: #2>1
     for i in range(2,n):#2,2 2,3 2,3
        if n%i==0:
           b.append(n)
         #   print("not prime",n) #3%2==0
           break
     else:
      #   print("prime",n)
        a.append(n)

print("prime",a)
print("notprime",b)

#prime or not
#input 5 
#output 1x5=5 upto 10
g=5
if g<=1:
   print("not")
elif g>1:
   for i in range(2,g):
      if g%i==0:
         print("not")
   else:
      print("prime")
      
#method 2
num=int(input())
def isPrime(a):
  flag=0
  if a<=1:
       return False
  elif a>1:
    for i in range(2,a):
      if a%i==0:
         flag=1
         break
    if flag==1:
       return False
    else:
       return True
primeList=[]
checkPrime1=isPrime(num)
# checkPrime2=isPrime(12)
# checkPrime3=isPrime(13)
primeList.append(checkPrime1)
# primeList.append(checkPrime2)
# primeList.append(checkPrime3)
for i in range(0,len(primeList)):
  if primeList[i]==True:
    print("prime")
  else:
    print("not prime")
#prime odd
num=int(input())
a=[]

for i in range(1,num+1):
     if i>1:
          for n in range(2,i):
               if i%n==0:
                   break
          else:
               a.append(i)               
for j in a:
     if j%2!=0:
          print(j,end=" ")