# For developing un understanding, use loops to accept 5 values from user and store them in a list. 
# Display all the values (objects) of the list.

myList = []
for i in range(5):
    val=input("Enter a value : ")
    myList.append(val)
print("The given list of values are : ")
print(myList)