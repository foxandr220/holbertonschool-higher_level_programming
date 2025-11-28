#!/usr/bin/python3
"""Function to check if object is instance of class or inherited class"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or its subclass

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is instance of a_class or its subclass
    """
    return isinstance(obj, a_class)
