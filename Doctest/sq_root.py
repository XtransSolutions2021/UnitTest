

def sqRoot(x):
    '''
    >>> sqRoot(-4)
    'This is a negative root'
    >>> sqRoot(4)
    2.0
    >>> sqRoot(0.6)
    0.7745966692414834
    >>> sqRoot(-6)
    'This is a negative root'
    >>>
    '''

    if not type(x) in [int, float]:
        result = "Please enter a number"
    elif x < 0:
        result = "This is a negative root"
    else:
        result = (x)**0.5
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()