#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    rect = []
    for i in range(0, list_length):
        try:
            m = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            m = 0
            continue
        except ZeroDivisionError:
            print("division by 0")
            m = 0
            continue
        except IndexError:
            print("out of range")
            m = 0
            continue
        finally:
            rect.append(m)
    return rect
