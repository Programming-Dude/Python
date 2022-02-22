"""
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, 
inside the parentheses. You can add as many arguments as you want, 
just separate them with a comma.

The following example has a function with one argument (fname). 
When the function is called, we pass along a first name, 
which is used inside the function to print the full name:  
"""
def my_function(fname):
  print(fname)

my_function("KENE")
my_function("AMEY")
my_function("KAJAL")

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: 
# information that are passed into a function.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, 
# you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("VINAY", "KENE")
