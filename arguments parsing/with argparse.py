#!/usr/bin/env python

# Python 3.7.3
# Argparse test

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")

args = parser.parse_args()

print(args.echo)
