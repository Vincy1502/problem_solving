name=input() #malayalam

def checkPalindrome(str):
  for i in range(0,len(str)): #0,9
    if str[i] != str[len(str)-i-1]: 
      #str[0] != str[9-0-1]
      #str[1] != str[9-1-1]
      #str[2] != str[9-2-1]
      #str[3] != str[9-3-1]
      #str[4] != str[9-4-1]
      #str[5] != str[9-5-1]
      #str[6] != str[9-6-1]
      #str[7] != str[9-7-1]
      #str[8] != str[9-8-1]
      return False
    return True
isPalindrome=checkPalindrome(name)
  
if isPalindrome==True:
  print("True") 
else:
  print("False")
#method 2
name=input()
a=name[::-1]
print(a)




    