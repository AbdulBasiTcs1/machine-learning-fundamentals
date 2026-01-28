# Understanding Data and Memory usage for Machine Learning

# Objective: 
# This lab will give you practical implementation of different types of sequences including lists, 
# tuples, sets and dictionaries. We will use lists alongside loops in order to know about indexing 
# individual items of these containers. This lab will also allow students to write their own functions. 

# Activity Outcomes: 
# ability to: 
# Develop a basic understanding of data structures commonly used for AI 
# Understanding Lists and Tupples 
# Solving complex mathematical problems 
# Using loops with lists 
# Developing customized functions for logical inference 
# Basic understanding of Object Oriented Concepts like Class definitions etc.

# 1) Useful Concepts 
# In Python the concept of Lists is used which is just like arrays, declared in other languages which is an 
# ordered collection of data. It is very flexible as the items in a list do not need to be of the same type. 
 
# The implementation of Python List is similar to Vectors in C++ or ArrayList in JAVA. The costly operation 
# is inserting or deleting the element from the beginning of the List as all the elements are needed to be 
# shifted. Insertion and deletion at the end of the list can also become costly in the case where the pre-allocated 
# memory becomes full. 
 
# Python provides different types of data structures as sequences. In a sequence, there are more than one 
# values and each value has its own index as can be seen in Figure 1 below: 
 
# Figure 1: Assigning values in a List (Image Courtesy: https://www.geeksforgeeks.org/python-data-structures/) 
 
# The first value will have an index 0 in python, the second value will have index 1 and so on. These indices 
# are used to access a particular value in the sequence. 
 
# Python offers different types of sequences. Lists are the most important type of sequence being used in 
# Python. It is a collection of same or different type of objects. These objects are separated by commas to 
# distinguish from each other enclosed in square brackets. The following activities show that how lists are 
# used in Python. 
 
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences 
# between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas 
# lists use square brackets. The data type "set", which is a collection type, has been part of Python since 
# version 2.4. A set contains an unordered collection of unique and immutable objects. 
 
# The set data type is, as the name implies, a Python implementation of the sets as they are known from 
# mathematics. This explains, why sets unlike lists or tuples can't have multiple occurrences of the same 
# element. 
 
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written 
# with curly brackets, and they have keys and values.