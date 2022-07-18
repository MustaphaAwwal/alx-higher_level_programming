#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            count += 1
        if x <= count:
            print(x)
        else:
            print(count)
        for i in range(0, count):
            print("{:d}".format(my_list[i]), end="")
    except:
        pass
    print()
