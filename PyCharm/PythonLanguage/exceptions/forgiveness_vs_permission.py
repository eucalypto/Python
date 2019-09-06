# There is this concept of "It's easier to ask for forgiveness than for permission".
# But It looks like this is just the concept of exceptions.

my_list = [1, 2, 3]

try:
    print(my_list[3])
except IndexError as ie:
    print("Index error")
    raise ie
