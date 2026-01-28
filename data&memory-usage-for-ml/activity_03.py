# Accept two lists from user and display their join.

myList1=[]
for i in range(5):
    val=input("Enter the value (First List) : ")
    n=int(val)
    myList1.append(n)
    
myList2=[]
for i in range(5):
    val=input("Enter the value (Second List) : ")
    n=int(val)
    myList2.append(n)
    
list3=myList1+myList2
print(list3)

