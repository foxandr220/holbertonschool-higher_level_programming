#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            value = my_list[i]
            print("{:d}".format(value), end="")
            printed += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print()
    return printed
