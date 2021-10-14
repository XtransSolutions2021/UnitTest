# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test light sensor

#import RPi.GPIO as GPIO
import time
#import GPIO as GPIO

import nose
light = 33  # Board number

light_state = 0
def read_light(light_state):
    while True:
        if light_state == 0:
            print("Light Detected")
        elif light_state == 1:
            print("Light Not Detected")
        time.sleep(.3)
def test_add_integers():
    assert read_light(light_state) == 1


if __name__ == '__main__':  # Program starting from here
    nose.run()
