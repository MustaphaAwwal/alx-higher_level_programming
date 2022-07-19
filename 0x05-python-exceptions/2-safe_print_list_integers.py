#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(0, x):
        j = my_list[i]
        try:
            print("{:d}".format(j), end="")
            i += 1
        except (ValueError, TypeError):
            i -= 1
            continue

    print()
    return i
