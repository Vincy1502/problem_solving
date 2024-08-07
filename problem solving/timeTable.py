#time table
d={"period1":"GM","period2":"CT","period3":"IOT","mrng":["period1","period2","period3"],"afternoon":["period4","period5"],
   "period4":"PRJ.T","period5":"GM LAB","break":["11.0","12.20"],"11.0":"mrng break","12.20":"lunch break"}

sess=(input("enter the session:"))

if sess=="mrng":
    print(d.get("mrng"))
    period=input("enter the period:")
    if period=="period1":
        print(d.get("period1"))
    elif period=="period2":
        print(d.get("period2"))
    elif period=="period3":
         print(d.get("period3"))
elif sess=="afternoon":
    print(d.get("afternoon"))
    period=input("enter the period:")
    if period=="period4":
        print(d.get("period4"))
    elif period=="period5":
        print(d.get("period5"))
elif sess=="break":
    print(d.get("break"))
    brk=input("enter the break time:")
    if brk=="11.0":
        print(d.get("11.0")) 
    elif brk=="12.20":
        print(d.get("12.20")) 

else:
    print("It is not the college time")       

#find cgpa

cgpa=float(input("enter your cgpa:  "))

if cgpa>5 and cgpa<=10:
    if cgpa>=5.0 and cgpa<=5.9:
        print("pass with grade E")
    elif cgpa>=6.0 and cgpa<=6.9:
        print("pass with grade D")
    elif cgpa>=7.0 and cgpa<=7.9:
        print("pass with grade C") 
    elif cgpa>=8.0 and cgpa<=8.9:
        print("pass with grade B")
    elif cgpa>=9.0 and cgpa<=9.9:
        print("pass with grade A")
else:
    print("you are fail")
        