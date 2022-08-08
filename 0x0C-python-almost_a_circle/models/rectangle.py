#!/usr/bin/python3
"""
This script defines a rectange that inherits from Base class from base.py
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new rectangle
        Args:
            width (int): The width of the newly created rectangle
            height (int): The height of the newly created rectangle
            x int(): Represents the x-coordinate of the rectangle
            y int(): Represents the y-coordinate of the rectangle
        Raises:
            TypeError: If width and height are not type of int.
            ValueError: If width and height <= 0.
            TypeError: If x and y are not type of int.
            ValueError: If x < 0 or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """the method that computes the area"""
        return self.width * self.height

    def display(self):
        """public method that
        prints in stdout the rectangle with # character"""
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#" * self.width)]

    def update(self, *args, **kwargs):
        """Updates exsting rectangle with *args and **kwargs
        Args:
            *args (int): New no-keyword attributes:
                -1st argument: - id attribute
                -2nd argument: - width attribute
                -3rd argument: - height attribute
                -4th argument: - x attribute
                -5th argument: - y attribute
            **kwargs (dict): New key/value attributes
        """
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                else:
                    self.y = arg
                index += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Render out user friendly output"""
        return '[{}]  ({}) {}/{} - {}/{}'.format(__class__.__name__,
                                                 self.id, self.x, self.y,
                                                 self.width, self.height)
