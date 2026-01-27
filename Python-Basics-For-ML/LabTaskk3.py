#Fibonacci Series
n=int(input("Enter the number : "))

a=0
b=1

if n<=0:
    print("Please enter the positive")
elif n==1:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c