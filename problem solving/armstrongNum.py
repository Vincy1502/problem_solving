num=int(input("enter the number:"))#153

temp=num #153
sum=0
while temp>0: #153
    #15
    #1
    digit=temp%10 
    #153%10-->digit=3
    #15%10-->digit=5
    sum=sum+digit**3
    #0+3**3-->sum=27
    #27+5**3-->sum=152
  
    temp=temp//10
    #153//10-->temp=15
    #15//10-->temp=1
print(sum)
if num==sum:
    print("this num is armstrong number")
else:
    print("this number is not armstrong number")



# 153
# 1*1*1=1
# 5*5*5=125
# 3*3*3=27

# 1+125+27=153

# print(153%10)
# print(153//10)
# print(15/2)
# print(15%2)
# print(1/10)
