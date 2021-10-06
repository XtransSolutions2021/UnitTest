from cal import Calculate
def add(self, x, y):
    """Takes two integers and adds them together to produce
    the result.
    >>> c = Calculate()
    >>> c.add(1, 4)
    6
    >>> c.add(24, 126)
    150
    >>> c.add(1.8, 1.9)
    Traceback (most recent call last):
    ...
    TypeError: Invalid type: <class 'float'> and <class 'float'>
    """
    if type(x) == int and type(y) == int:
        return x + y
    else:
        raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


if __name__ == "__main__":
 import doctest
 doctest.testmod(extraglobs={'c': Calculate()})
