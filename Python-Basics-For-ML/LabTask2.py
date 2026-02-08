# Write a program to calculate the factorial of a number 
number = int(input("Enter the number to calculate the factorial : "))
if number<0:
    print("Factorial of a negative number is not possible : ")
factoial=1
for i in range(1,number+1):
    factoial=factoial*i
print("Factorial of number is : ",factoial)