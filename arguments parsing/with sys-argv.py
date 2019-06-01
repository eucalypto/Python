#!/usr/bin/env python

import sys

args = sys.argv[1:]  # sys.argv[0] gives usually the name of the python script

print(f"there are {len(args)} arguments given")

for item in args:
    print(item)

# or:
print(f"arguments given: {str(args)}")
