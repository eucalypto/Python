#!/usr/bin/env python

import sys

args = sys.argv[1:]  # sys.argv[0] gives usually the name of the python script

print(f"there are {len(sys.argv)} arguments given")

print(f"arguments given: {str(sys.argv)}")

name = "Gandalf the Grey"
breakfast = "Bacon and eggs"
amount = 3

order = f"{name} wants {amount} {breakfast} for breakfast."
print(order)
