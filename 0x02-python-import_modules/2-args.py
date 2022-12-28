#!/usr/bin/python3

if __name__ == '__main__':
    """print the number of and list of argument"""
    import sys
    # return the length of the argument
    if len(sys.argv[1:]) == 0:
        print(len(sys.argv[1:]), "arguments.")
    elif len(sys.argv[1:]) == 1:
        print(len(sys.argv[1:]), "argument:")
    else:
        print(len(sys.argv[1:]), "arugments:")
    # print the argument index and the argument
    for i in sys.argv[1:]:
        print("{}: {}".format(sys.argv.index(i), i))
