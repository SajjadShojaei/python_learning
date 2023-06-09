# -------------[For Loops]----------------
# for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:

for s in "Sajjad":
  print(s)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

friends = ['sajjad' , 'amir' , 'farid' , 'mohammad' , 'ali']
for items in friends:
    if items == 'mohammad':
        break
    print(items)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next: 

books = ["book1", "book2", "book3"]
for book in books:
  if book == "book2":
    continue
  print(book)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.  

for number in range(6):  # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
    print(number)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):    

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for x in range(2, 30, 3):
  print('->',x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

friends = ['sajjad' , 'amir' , 'farid' , 'mohammad' , 'ali']
for name in friends:
    print('hello ',name)
else:
    print('oh, finished!')

# Nested Loops
# A nested loop is a loop inside a loop.        

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)