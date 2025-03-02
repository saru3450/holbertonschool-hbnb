#!/usr/bin/python3


from .base import BaseModel


class Amenity(BaseModel):

    def __init__(self, name):
        """attibutes for the Class"""
        super().__init__()
        self.name = name

    @property
    def name(self):
        """
        Getter for the name attribute.

        Returns:
            str: The name of the amenity.
        """
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("The name must be a string.")
        if not value.strip():
            raise ValueError("The name cannot be empty.")
        if len(value) > 50:
            raise ValueError("The name cannot exceed 50 characters.")
        self._name = value.strip()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "__class__": self.__class__.__name__
        }
