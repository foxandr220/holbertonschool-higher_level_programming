#!/usr/bin/python3
"""BaseGeometry class with area and integer_validator methods"""


class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """Calculate area of geometry

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value

        Args:
            name (str): The name of the value
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
