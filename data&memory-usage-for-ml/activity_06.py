# The Python Tuple is a collection of Python objects much like a list but Tuples are immutable in nature 
# i.e. the elements in the tuple cannot be added or removed once created. Just like a List, a Tuple can 
# also contain elements of various types. 
# ith or without 
# the use of parentheses for grouping of the data sequence. 
 
# # Creating a Tuple with 
# # the use of Strings 
# Tuple = ('Geeks', 'For') 
# print("\nTuple with the use of String: ") 
# print(Tuple) 
 
# # Creating a Tuple with 
# # the use of list 
# list1 = [1, 2, 4, 5, 6] 
# print("\nTuple using List: ") 
# Tuple = tuple(list1) 
 
# # Accessing element using indexing 
# print("First element of tuple") 
# print(Tuple[0]) 
 
# # Accessing element from last 
# # negative indexing 
# print("\nLast element of tuple") 
# print(Tuple[-1]) 
 
# print("\nThird last element of tuple") 
# print(Tuple[-3]) 
 
# The output should be: 
 
 
 
 
 
 
 
# Tuple with the use of String: 
 
# ('Geeks', 'For') 
# Tuple using List: 
# First element of tuple 
# 1 
# Last element of tuple 
# 6 
# Third last element of tuple 
# 4 
 
# The Tuple also has an enhanced version called NamedTuple, which returns a tuple object with names 
# for each position which the ordinary tuples lack. 
 
# For example, consider a tuple names student where the first element represents fname, second 
# represents lname and the third element represents the DOB. Suppose for calling fname instead of 
# remembering the index position you can actually call the element by using the fname argument, then 
# it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple. 
# from collections import namedtuple 
# # Declaring namedtuple() 
# Student = namedtuple('Student',['name','age','DOB']) 
# # Adding values 
# S = Student('Akber','19','2541997') 
# # Access using index 
# print ("The Student age using index is : ",end ="") 
# print (S[1]) 
# # Access using name 
# print ("The Student name using keyname is : ",end ="") 
# print (S.name) 
 
# The output would be: 
 
# The Student age using index is : 19 
# The Student name using keyname is : Akber 
# 1
# 5 
 
 
 
# The Python Set is an ordered collection of data that is mutable and does not allow any duplicate element. 
# Sets are basically used to include membership testing and eliminating duplicate entries. The data structure 
# used in this is Hashing, a popular technique to perform insertion, deletion, and traversal. 
 
# If Multiple values are present at the same index position, then the value is appended to that index position, 
# to form a Linked List. 
# # Creating a Set with 
# # a mixed type of values 
# # (Having numbers and strings) 
# Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
# print("\nSet with the use of Mixed Values") 
# print(Set) 
 
# # Accessing element using 
# # for loop 
# print("\nElements of set: ") 
# for i in Set: 
# print(i, end =" ") 
# print() 
 
# # Checking the element 
# # using in keyword 
# print("Geeks" in Set) 
 
# The output should be: 
 
# Set with the use of Mixed Values 
# {1, 2, 'Geeks', 4, 6, 'For'} 
 
 
# Elements of set: 
# 1 2 Geeks 4 6 For 
# True 
 
# Try also experimenting with frozen sets. 
# 1
# 6 
 
 
# 26 
 
# The Python Strings are arrays of bytes representing Unicode characters. In simpler terms, a string is an 
# immutable array of characters. Python does not have a character data type, a single character is simply a 
# string with a length of 1. As strings are immutable, modifying a string will result in creating a new copy. 
 
# String = "Welcome to GeeksForGeeks" 
# print("Creating String: ") 
# print(String) 
 
# # Printing First character 
# print("\nFirst character of String is: ") 
# print(String[0]) 
 
# # Printing Last character 
# print("\nLast character of String is: ") 
# print(String[-1]) 
 
# The output should be: 
 
# Creating String: 
# Welcome to GeeksForGeeks 
# First character of String is: 
# W 
# Last character of String is: 
# s 
# Try also experimenting with Bytearray. 