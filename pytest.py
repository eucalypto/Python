#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import fileinput
# fileinput is used to read the input. It can be stdin or a file.




# The for loop goes through the lines of the input. Here it just
# prints them to stdout
for edge_list_raw in fileinput.input():
    print(edge_list_raw.strip())

