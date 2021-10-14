class Calculate(object):
    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    def test_add_integers():
        assert add(self, 5, 3) == 8


if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2.0, 2.0)
    print (result)

