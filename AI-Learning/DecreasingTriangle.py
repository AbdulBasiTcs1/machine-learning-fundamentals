# In this code we guys are going to make a Decreasing Triangle 
num = int(input("Enter the num : "))
for i in range(num):
    for j in range(i,num):
        print("*",end=" ")
    print()