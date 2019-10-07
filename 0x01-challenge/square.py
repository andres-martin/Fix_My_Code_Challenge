#!/usr/bin/python3
"""
documentation
"""


class Square:
    ''' Square class '''

    width = 0
    height = 0

    def __init__(self, width, height):
        ''' initializer for attributes '''
        self.width = width
        self.height = height

    def __wh_validator(self, name, value):
        ''' comments '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        ''' comments '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' comments '''
        self.__wh_validator("width", value)
        self.__width = value

    @property
    def height(self):
        ''' comments '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' comments '''
        self.__wh_validator("height", value)
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square calculates area """
        return self.width * self.height

    def permiter_of_my_square(self):
        ''' Perimeter of Square '''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        ''' str representation of instance '''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
