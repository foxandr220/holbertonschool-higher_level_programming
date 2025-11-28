#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry with validation."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raises an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer.
        Args:
            name (str): name of the parameter
            value (int): value to validate
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

