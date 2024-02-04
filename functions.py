def my_function():
  print("Hello from a function")

my_function()

#Information can be passed into functions as arguments.

#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

#The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#If we call the function without argument, it uses the default value:

def my_function(country = "China"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x):
  print(x)

my_function(x = 3)

#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)

#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

def my_function(x):
  print(x)

my_function(3)

#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

#To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
