# Write a Python code to accept marks of a student from 1-100 and display the grade 
# according to the following formula. 
 
# Grade F if marks are less than 50 
# Grade E if marks are between 50 to 60 
# Grade D if marks are between 61 to 70 
# Grade C if marks are between 71 to 80 
# Grade B if marks are between 
# 81 to 90 
# Grade A if marks are between 91 to 100 

marks = int(input("Enter your marks (1-100): "))

if marks < 1 or marks > 100:
    print("Please enter marks between 1 and 100")
elif marks < 50:
    print("Grade F")
elif marks <= 60:
    print("Grade E")
elif marks <= 70:
    print("Grade D")
elif marks <= 80:
    print("Grade C")
elif marks <= 90:
    print("Grade B")
else:
    print("Grade A")


    