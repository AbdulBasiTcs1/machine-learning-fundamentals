# In this we are going to make a decreasing right sided triangle
num = int(input("Enter the rows : "))
for i in range(num):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,num):
        print('*',end=' ')
    print()