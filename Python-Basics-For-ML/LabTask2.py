# Write a program that takes a number from user and calculate the factorial of that number. 
num=int(input("Enter a number : "))
factorial=1
if num<0:
    print("Factorial is not defined for the negative numbers")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial is : ",factorial)