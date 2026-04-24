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
#Program-2 
#Building a calculator 
# taking user input using input()fn to get two seperate digits on which calculations to be performed
# then using that digits performing arithmetic operations like +,-,/,* to get the result 
# brute force attempt

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Enter +,-,/,* to perform arithmetic operation: ")

if c=='/':
    div = a/b
    print(f"division = {div}")
    if a/0:
        print("Not defined")
elif c=='*':
    mul = a*b
    print(f"Multiplication = {mul}")
elif c=='+':
    add = a+b
    print(f"Addition = {add}")
elif c=='-':
    sub = a-b
    print(f"Subtraction = {sub}")            
#Program is working 

#Perfect attempt 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number"))
print(f"Sub = {num1 - num2}")
print(f"Add = {num1 + num2}")
print(f"Mul = {num1*num2}")
print(f"div = {num1/num2}")
print(f"Not defined... {num1/0}") #solved the number/0 problem 
