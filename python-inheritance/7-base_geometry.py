#!/usr/bin/python3
"""BaseGeometry class with area and integer_validator methods"""


class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """Calculate area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value"""
        if type(value) not in (int,) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
