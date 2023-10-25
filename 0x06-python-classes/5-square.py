#!/usr/bin/python3
"""Make a Square object."""


class Square:
    """
    Make a square.

    Examples
    --------
    >>> my_square = Square(3)
    >>> print(my_square.__dict__)
    {'_Square__size': 3}
    """
    def __init__(self, size=0):
        """
        Intialize a new instance.

        Arguments
        ---------
        size : int
            The size of the square

        Examples
        --------
        >>> my_square = Square(3)
        >>> print(my_square.__size)
        Traceback (most recent call last):
            ...
        AttributeError: 'Square' object has no attribute '__size'

        Examples
        --------
        >>> my_square = Square("3")
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
        >>> my_square = Square(-3)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Examples
        --------
        >>> my_square = Square(89)
        >>> print(my_square.size)
        89
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square to a given value.

        Examples
        --------
        >>> my_square = Square()
        >>> my_square.size(3)
        >>> my_square.size("3")
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
        >>> my_square.size = -3
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of a square.

        Examples
        --------
        >>> my_square = Square(5)
        >>> print(my_square.area())
        25
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print out the square object.

        Examples
        --------
        >>> my_square = Square(5)
        >>> my_square.my_print()
        #####
        #####
        #####
        #####
        #####
        >>> my_square.size = 0
        >>> my_square.my_print()
        <BLANKLINE>
        >>> my_square.size = 1
        >>> my_square.my_print()
        #
        """
        tail = '' if self.__size else '\n'
        line = '#' * self.__size + '\n'
        print(line * self.__size, end=tail)
