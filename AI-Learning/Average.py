#Average of numbers
num = int(input("How many numbers ?"))
average=0
total_sum = 0
for i in range (num):
    numbers = float(input("Enter numbers : "))
    total_sum = total_sum +numbers
average = total_sum / num # How many num in total so divide it on total_sum to get average
print("Average: ",average)