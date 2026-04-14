#print() function is used to give output in various forms
#input() function enables interaction with users 
# input() fucntion gives user input on output screenby default in string until specified
# example
name = input("Enter Your Name: ")
print("Hello",name,"!Welcome")
#printing output using print()
print("Hello world")

#Printing variables
s = "coka  cola"
print(s)
age = 25
print(age)
city = "New York"
print(s,age,city)

# Taking Multiple inputs at once from the user in single one line
# Also splitting the values entered by user into seperate variables for each value using split() method
a, b= input("Enter two number: ").split()
print(a,b)
print(type(a))

# Taking different types of User Inputs 
i = int(input("How old are you: "))
f = float(input("Evaluate 7/2: "))
print(i,f)

#Perplexity Examples
name = input("Enter your name: ")
print("Hello! ",name)

age = 21
print("You will be ",age + 1,"Next year")

#Taking Multiple ijputs in one line 
j,k = input("Enter two numbers: ").split()
print(j,k)

#Taking Multiple inputs in one line via type conversion
a,b = map(int, input("Enter two numbers: ").split())
print(a,b)

#Problem -2 
#Take two numbers from the user in one line (space separated).
#Print their sum, difference, and product.
'''Sum: 30
Difference: 10
Product: 200'''
x ,y = map(int,input('Enter the two numbers').split())
print(x+y,x-y,x*y)

