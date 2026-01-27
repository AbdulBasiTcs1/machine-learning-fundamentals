# In this code we wanna make the increasing triangle
num = int(input("Enter the number : "))
for i in range(num) : 
    for j in range (i+1)  :
        print("*",end="  ")
    print()

    # As in this we have the same number of rows like we was having in the sqyare so in this 
    # we have to icrease the columns like in the first row 1 column and in 2nd 2 and so on
    # that why we applied the logic of the i + 1