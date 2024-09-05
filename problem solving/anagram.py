s=input()
s2=list(input())
a=""
if len(s) != len(s2):
    print("not anagram")
else:
    for i in s:
        if i in s2:
            s2.remove(i)
            a+=i
    if s==a:
        print("anagram")
    else:
        print("not anagram")
 
