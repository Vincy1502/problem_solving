
#small characters
charlength=int(input())
a=[]
b=[]


for i in range(charlength):
    character=input()
    b.append(character)
    a=[0]*26
    for char in b:
      value=ord(char)-97
      a[value] += 1
for j in range(len(a)):
  if a[j] != 0:
    print(chr(j+97),":",a[j])

    