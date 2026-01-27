# Find the numbers between 100 to 1000 that are divisible by 5 and 6.
for i in range(100,1001):
    if (i%5==0 and i%6==0):
        print("Numbers divisible by 5 and 6 are : ",i)