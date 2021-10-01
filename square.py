import doctest
def square_area(x):
    """
    compute the area of a square
    >>> square_area(1)
    1
    >>>square_area(2)
    4
    >>> square_area(-1)
    """
    if x < 0 :
        return None
    return x ** 3

if __name__ == "__main__":
    doctest.testmod()