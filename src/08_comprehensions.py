"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []

for n in range(1,6):
   y.append(n)

# y = list(map(lambda n:n, range(1,6)))

y = list(n for n in range(1,6))
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []

#for n in range(0,10):
#    y.append(n ** 3)

y = list(map(lambda n: n** 3, range(0,10)))

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []

# for word in a:
#     big_word = word.upper()
#     y.append(big_word)

# y = list(map(lambda word : word.upper(), a))

z = lambda word: word.upper()
y = list(map(z,a))

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
"1,2,3,4"
"1" "2" "3" "4"

# x = [1, 2, 3, 4, 5, 6]

# What do you need between the square brackets to make it work?
y = [int(num) for num in x if int(num) % 2 == 0]

print(y)