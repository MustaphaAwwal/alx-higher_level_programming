#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
    try:
        m = 0
        for i in mylist:
            m += 1
        if x <= m:
            print(x)
        elif x >= m:
            x = m
            print(m)
        for i in mylist:
            print(i, end="")
    except (ValueError, NameError):
        print('no')
