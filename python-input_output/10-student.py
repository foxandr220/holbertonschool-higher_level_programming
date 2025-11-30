#!/usr/bin/python3
"""
Class Student with filtering for JSON serialization.
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of Student instance.
        If attrs is a list of strings, only retrieve attributes in that list.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            # filter only requested attributes
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        # return full dictionary
        return self.__dict__.copy()
