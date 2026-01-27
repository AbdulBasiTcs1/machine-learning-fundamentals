# In this code we are going to make the right sided triangle 
num=int(input("Enter the number of rows in pattern : "))
for i in range(num):
    for j in range(i,num):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()


    # the number of chracters must be to the same 