# Write a Python code to accept marks of a student from 1-100 and display the grade 
# according to the following formula. 
 
# Grade F if marks are less than 50 
# Grade E if marks are between 50 to 60 
# Grade D if marks are between 61 to 70 
# Grade C if marks are between 71 to 80 
# Grade B if marks are between 
# 81 to 90 
# Grade A if marks are between 91 to 100 

marks = int(input("Enter your marks (1-100) : "))

if marks < 50 :
    print("Grade F")
elif marks >= 50 and marks <=60 :
    print("Grade E")
elif marks >= 61 and marks <=70:
    print("Grade D")
elif marks >=71 and marks <=80 :
    print("Grade C")
elif marks >= 81 and marks <=90:
    print("Grade B")
elif marks >=91 and marks <=100:
    print("Grade A")
else :
    print("Please enter marks b/w 1 and 100")

    