#Variables practice
x = 10          # int
name = "Shivansh"  # str
pi = 3.14       # float
is_pass = True  # bool
print(type(x))
print(type(name))
print(type(pi))

#Swapping two variables | problem - 1
x,y = 10, 20 
x,y = y,x
print(x,y)

# problem -2 
x = 10
y = "20"
z = 30.5
w = True
print(f"x is of type: {type(x)}") #Using f- string to print the labled output
print(f"y is of type: {type(y)}")
print(f"z is of type: {type(z)}")
print(f"w is of type: {type(w)}")

#Problem -3 Variable Reassignment 
x = 10
x = x + 5
x = x * 2
x = str(x)
print(x)
print(type(x))

#Problem -4 Bug fix
name = "Shivansh"
age = 21
city = "Delhi"
print(type(age))
print(type(city))
print(type(name))


#3 ways to fix this code 
# Way 1 — comma (your fix) ✅
print("Age: ", age) # I applied this 
print(type(age))

# Way 2 — str() conversion
print("Age: " + str(age)) 
print(type(age))
# Way 3 — f-string (cleanest, use this going forward)
print(f"Age: {age}")
print(type(age))


a = 10
b = 20

temp = a # a = 10 ,
a = b
b = temp

print(a, b)
