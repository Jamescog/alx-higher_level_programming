#!/usr/bin/python3
"""
    Defines a Rectangle class
"""


class Rectangle:
    """
        defines a Rectangle class
     """
    def __init__(self, width=0, height=0):
        """Instatiates class with optinal attributes.
            atttributes:
                width - the width of the rectangle
                height - the height of the ractangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retirves the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of rectangle"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
