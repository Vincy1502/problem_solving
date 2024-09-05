#small and caps
length=int(input())
a=[]
b=[]
for i in range(length):
    character=input()
    b.append(character)
    a=[0]*60
    for char in b:
       x=ord(char)-65
       a[x] += 1
print(a)
for j in range(len(a)):
   if a[j] != 0:
      print(chr(j+65),":",a[j])
