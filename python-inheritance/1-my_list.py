#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """A class that inherits from list with sorted printing"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
