#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        first = 0
        for i in range(0, x):
            first += 1
        print(first)
        count = 0
        for i in range(0, count):
            print("{:d}".format(my_list[i]), end="")
    except:
        pass
    print()
