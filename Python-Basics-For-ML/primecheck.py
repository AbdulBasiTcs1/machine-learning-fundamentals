# Write a Python code to accept an integer value from user and check that whether the 
# given value is prime number or not.

isPrime=True
i=2
n=int(input("Enter the number : "))
while i<n:
    remainder=n%i
    if remainder==0:
        isPrime=False
        break
    else:
        i=i+1
if isPrime:
    print("Number is Prime")
else:
    print("Number is not Prime")