#!/usr/bin/python3
"""
    Defines a Rectangle class
"""


class Rectangle:
    """
        defines a Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instatiates class with optinal attributes.
            atttributes:
                width - the width of the rectangle
                height - the height of the ractangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the reactangle"""
        if value < 0:
            raise ValueError("width must be >=0")
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        """Retirves the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of rectangle"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints object as string"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        else:
            r = []
            for h in range(self.__height):
                [r.append(str(self.print_symbol)) for w in range(self.__width)]
                if h != self.__height - 1:
                    r.append("\n")
            return ("".join(r))

    def __repr__(self):
        """return a string representation of rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """garbage collector that destroys an object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares 2 rectangles and returns the biggest
        based on the area
        rect_1: must be instance or Rectangle, otherwise raise value error
        rect_2: must be instance or Rectangle, otherwise raise value error
        return: rect_1 if rectangles are equal
        """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle with width and height == size"""
        return cls(size, size)
