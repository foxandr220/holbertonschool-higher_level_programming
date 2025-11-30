#!/usr/bin/python3
"""
Class Student that defines a student with:
- first_name
- last_name
- age
Includes JSON serialization and reloading.
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of a Student instance.
        If attrs is a list of strings, only return those attributes.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using json dict.
        json keys = attribute names
        json values = the new values for attributes
        """
        for key, value in json.items():
            setattr(self, key, value)
