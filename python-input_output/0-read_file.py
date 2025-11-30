#!/usr/bin/python3
"""
Function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """Reads a UTF8 text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
