# a set is an unordered collection of unique elements
# a set can be created in two ways
# 1. using the set() function
# 2. using curly braces {}

set1 = set()
print(set1)
set1.add(1)
print(set1)
set1.add(2)
print(set1)
set1.add(2)
print(set1)
set1.add(3)
print(set1)
set1.add(4)
print(set1)

# OUTPUT:
# set()
# {1}
# {1, 2}
# {1, 2}
# {1, 2, 3}
# {1, 2, 3, 4}





# we can also pass a list to the set() function
set2 = set(['James', 'John', 'Peter', 'James', 'John', 'Peter','Martin'])
print(set2)
# OUTPUT:
# {'John', 'James', 'Martin', 'Peter'}





# we can also pass a string to the set() function
set3 = set('James Jimmy Kinyenje')
print(set3)
# OUTPUT:
# {'m', 'J', 'n', 'e', ' ', 'j', 'a', 'i', 's', 'K', 'y'}





# we can also pass a tuple to the set() function
set4 = set(('James', 'John', 'Peter', 'James', 'John', 'Peter','Martin'))
print(set4)
# OUTPUT:
# {'James', 'Martin', 'Peter', 'John'}





# we can also pass a range to the set() function
set5 = set(range(1, 11))
print(set5)
# OUTPUT:
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}





# we can also pass a dictionary to the set() function 
# but only the keys will be added to the set and not the values 
