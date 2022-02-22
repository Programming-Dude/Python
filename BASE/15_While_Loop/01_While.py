"""
Python Loops
Python has two primitive loop commands:

while loops
for loops
The while Loop
With the while loop we can execute a 
set of statements as 
long as a condition is true.  
"""
i = 1
while i < 6:
  print(i)
  i += 1

print("Hello\n")


# The while loop requires relevant variables to be ready, 
# in this example we need to define an indexing variable, 
# i,which we set to 1.
# The break Statement
# With the break statement we can stop the loop even if 
# the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("Hello\n")

# The continue Statement
# With the continue statement we can stop the current 
# iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)