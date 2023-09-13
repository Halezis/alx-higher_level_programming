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
        self.__size = size

    def area(self):
        """calculates the current square area
        Returns: The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter for size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints to the stdout the square with '#"
        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()

