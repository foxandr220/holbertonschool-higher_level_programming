#!/usr/bin/python3
"""
Class Student that defines a student by:
    - first_name
    - last_name
    - age
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of Student instance."""
        return self.__dict__
