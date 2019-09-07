"""
This file explores a way to change directories to do something and come back with
the use of a context manager.
"""
import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        print("Starting new context")
        start_dir = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(start_dir)


with change_dir("dir1"):
    print(os.getcwd())
    print(os.listdir())

print('Back to original "context":')
print(os.getcwd())

with change_dir("dir2"):
    print(os.getcwd())
    print(os.listdir())
