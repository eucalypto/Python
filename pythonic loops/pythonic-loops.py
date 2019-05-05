#!/usr/bin/env python

# this is a non-pythonic loop (a c-like loop):

my_items = ["bacon", "eggs", "sausage",]

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

# The first non-pythonism is: the code manages the iteration variable 
# manually.
# 
# A better solution would be to use the range() builtin. Range() gives
# not a list but a faster immutable iterative object.

my_items = ["bacon", "eggs", "sausage",]

for i in range(len(my_items)):
    print(my_items[i])

# This is still not pythonic since python can iterate over the elements
# themselves in the most pythonic way:

my_items = ["bacon", "eggs", "sausage",]

for item in my_items:
    print(item)


# But what if you need to have an index also? Python can do that! With enumerate().

my_items = ["bacon", "eggs", "sausage",]

for i, item in enumerate(my_items):
    print(i, ": ", item)

# Wtih this we can conveniently iterate over dictionaries:

breakfast_wishes = {
    "Bob": "bacon",
    "Alice": "eggs",
    "Eve": "just coffee",
}

for name, breakfast in breakfast_wishes.items(): 
    print(name, "wants to have", breakfast, "for breakfast." )

