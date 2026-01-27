# We are going to make the square pattern with the number of rows and columns user wants
num = int(input("Enter the n : "))
for i in range (num):
    for j in range (num) : 
        print("*",end="  ")
    print()