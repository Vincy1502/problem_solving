num=int(input()) 
a=num
sum=0
while a>0:
  #a=1234 true
  #a=123 true
  #a=12 true
  #a=1 true
  #a=0 false
  digit=a%10 
  #1234%10-->digit=4
  #123%10-->digit=3
  #12%10-->digit=2
  #1%10-->digit=1
  sum+=digit
  #0+4-->sum=4
  #4+3-->sum=7
  #7+2-->sum=9
  #9+1-->sum=10
  a=a//10
  #1234//10-->a=123
  #123//10-->a=12
  #12//10-->a=1
  #1//10-->a=0
print(sum)  
