#Python supports the usual logical conditions from mathematics:

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#If statement:

a = 33
b = 200

if b > a:
  print("b is greater than a")

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

# can also have an else without the elif:
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

a = 2
b = 330
print("A") if a > b else print("B")

#can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The or keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#You can have if statements inside if statements, this is called nested if statements.
  
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass
