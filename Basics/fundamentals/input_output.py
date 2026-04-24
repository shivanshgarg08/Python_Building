#python input_output exercise 
# PROGRAM 1 — Name + Age Printer
# firstly taking user input using input() function
# secondly printing the user name and age together as output using print()
name = input("Please enter your name: ")
age = int(input("Enter your age: "))
print("Hello! ,",name,"You are...",age,"years old")

#This is my brute force attempt
# Now enhanced version ofn this program using
name_1 = input("Enter your name: ")
year  = int(input("Enter your birth year: "))
age = 2026 - year #A formula created to calculate age ny just entering the birth year
print(f"Hello {name} !!") #Using f-strings to use variable inside print function to get output 
print(f"Currently your age is {age}")
print(f"In 2027 you will be {age +1 } years old")  
#Key learnings
"""
use of f strings
"""
