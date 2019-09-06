import os


def traditional_strategy(myfile):
    if os.access(myfile, os.R_OK):
        with open(myfile) as file:
            print(file.read())
    else:
        print(f"File {myfile} cannot be accessed")


def exceptional_strategy(myfile):
    try:
        file = open(myfile)
    except IOError as io:
        print(f"File {myfile} cannot be accessed")
    else:
        with file:
            print(file.read())


if __name__ == '__main__':
    myfile = "/tmp/tmpfile234.txt"

    traditional_strategy(myfile)
    exceptional_strategy(myfile)
