#! /usr/bin/env python

catnames = []

while True:
    print('Please give a name of one of your cats. (Enter nothing to stop)')
    name = input()

    if name == '':
        break

    catnames += [name]

print('Thank you. So your cats are called ', end='')
for cat in catnames:
    print(cat, ",", end=' ')

print()
