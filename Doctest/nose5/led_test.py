import nose
from Doctest.nose5.led import func



def test_led_true():
    assert func(1) == True

def test_led_false():
    assert func(0) == False



if __name__ == '__main__':  # Program starting from here
    nose.run()
