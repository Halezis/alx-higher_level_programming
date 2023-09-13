#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initializes the class instance
        Args:
            size(int): The size of the square
        Returns: None
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the current square area
        Returns: The area of the square
        """
        return (self.__size) ** 2
