# Python Tuple count() Method
# Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

# Python Tuple index() Method
# Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

"""
Definition and Usage
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

Syntax
tuple.index(value)
Parameter Values
Parameter	    Description
value	        Required. The item to search for  
"""