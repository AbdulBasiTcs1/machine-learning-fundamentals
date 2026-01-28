# Accept 5 integer values from user. Store these values in a list and display the list in 
# ascending order. 

myList = []
for i in range(5):
    val=input("Enter the value : ")
    n=int(val)
    myList.append(n)
myList.sort()
print(myList)