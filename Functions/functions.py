# Let's create a function

# SYNTAX - def name_of_function():

# each function has a block of code to execute to ideally run one task
  def greeting(name):
      #(argument)
      print("Welcome " + name)

# if we execute this program now it would display nothing as we have not called this function

# Syntax to call the function
greeting("Dono")

# calling our greeting functions
# this will execute the code within the function

# create a new function that takes 2 arguments as ints and adds the value of the two args

 def add(num1, num2):
 # creating a function that takes two arg (num1, num2)
     print(num1 + num2)
 # Displaying the args received
 add(20, 6)

 def subtract(num1, num2):
 # creating a function to subtract 2 arg provided
     print(num1 - num2)

 subtract(40, 20)

# create a function to *
def multiply(num1, num2):
    return num1 * num2
# Calling the function that passes 2 values with a return statement
print(multiply(5, 6))

# create a function to /
 def divide(num1, num2):
     return num1 / num2

 # create a function to %
 def modulus(num1, num2):
     return num1 % num2
# research return statement and use it instead of print




