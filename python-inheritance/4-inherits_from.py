#!/usr/bin/python3
"""Function to check if object inherits from a class"""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class (but is not exact instance)

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj inherits from a_class but is not exact instance
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
