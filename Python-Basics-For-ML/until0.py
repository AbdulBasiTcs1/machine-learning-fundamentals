# Write a Python code to keep accepting integer values from user until 0 is entered. 
# Display sum of the given values. 

sum=0
s=input("Enter integer ")
n=int(s)
while n!=0:
    sum=sum+s
    s=input("Enter integer ")
    n=int(s)
print("SUM ",sum)