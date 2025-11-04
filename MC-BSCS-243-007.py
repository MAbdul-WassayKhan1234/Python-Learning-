# ##################################### Getting Started with Python ###################################

# Install Python from https://www.python.org/downloads/
# Install IDE (Integrated Development Environment) like VSCode
# Create a new Python file with .py extension (e.g., first.py)
# open terminal or command prompt
# Navigate to the directory where your Python file is located using 'cd' and press tab key for auto-completion
# PS C:\Users\HC\Desktop\.py\PY.code>  python first.py
# To check Python version installed
# PS C:\Users\HC\Desktop\.py\PY.code> python --version

##################################### Getting Started with Python ######################################


# ### Python Basics                   


# Printing Hello World
print("Hello World")

# Printing single value
print(3)

# Printing multiple values
print(3,2,1)

# Printing the sum of values
print(3+2+1)

#  Printing number and string
print("name ",3+3)


# Variables
A = 22
B = 33
C = A + B
print(C)

# Printing name and age
age = 23
name = "Khan"
print(name,":",age)
print(age)

# Multiple variable assignment
A,B,C = "Orange","Banana","Apple"
print(A,B,C)

# List of fruits
Fruit = ["Orange","Banana","Apple"]
print(Fruit)
print(type(Fruit))

# Range of numbers
X=range(10)
print(X)
print(type(X))

# Dictionary to store student information
Student={
    "Name":"M.Abdul Wassay Khan",
    "Reg#":"MC-BSCS-243-007",
    "CGPA":"3.75",
    "Email":"mawk@example.com",
    "Phone":"123-456-7890",
    "Address":"123 Main St, Multan, Pakistan",
}
print(Student)
print(type(Student))
print(Student["Name"])
print(len(Student))

# Single line comment

'''
Multi-line comment
This is a multi-line comment
'''

# Boolean values

print(10<5)
print(8==7)
print(5>2)

# Declaration of variables of integer data types

a,b,c,d,e,f,g,h,i,j= 1,2,3,4,5,6,7,8,9,10
print(a,b,c,d,e,f,g,h,i,j)

# Getting input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:",name)
print("Age:",age)

# Python Operators
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)



# #<!-------------------------------------- End of Python Basics ------------------------------------------!># #