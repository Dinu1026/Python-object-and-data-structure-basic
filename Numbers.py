 #1.) Types of Numbers in Python
#2.) Basic Arithmetic
#3.) Differences between classic division and floor division
# 4.)Object Assignment in Python
#lets start with basic aritmatic
  
# Addition
a=5
b=5
c=a+b
print(c)  #Ans:10
# Subtraction
a=10
b=5
c=a-b
print(c)   #Ans: 5
# Multiplication
a=10
b=5
c=a*b
print(c)   #Ans:50
# Division
a=7
b=4
c=a/b
print(c)  #Ans: 1.75
# Floor Division
a=7
b=4
c=a//b
print(c)  #Ans: 1

print("****************************************************************") #just for proper view

#The names you use when creating these labels need to follow a few rules:

#1. Names can not start with a number.
#2. There can be no spaces in the name, use _ instead.
#3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
#4. It's considered best practice (PEP8) that names are lowercase.
#5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
 #  or 'I' (uppercase letter eye) as single character variable names.
#6. Avoid using words that have special meaning in Python like "list" and "str"
#Using variable names can be a very useful way to keep track of different variables in Python. For example:

# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

print("The answer is",my_taxes)