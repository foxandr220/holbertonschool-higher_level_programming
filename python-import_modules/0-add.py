#!/usr/bin/python3
add_0 = __import__("add_0")
add = add_0.add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
