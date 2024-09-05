r=int(input("enter the row length:"))
c=int(input("enter the column length:"))
matrix=[]

for i in range(r):
    li=[]
    for j in range(c):
        li.append(input())
    matrix.append(li)
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if i==j:
            print(matrix[j][i])