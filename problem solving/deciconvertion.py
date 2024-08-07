num=int(input())
a=num
sum=0
s=0
while a>0:
    digit=a%10
    decimal=(2**s)*digit
    s=s+1
    sum+=decimal
    a=a//10
print(sum)
