# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test light sensor

#import RPi.GPIO as GPIO
import time
import GPIO as GPIO
import nose
light = 33  # Board number


def read_light():
    while True:
        light_state = input(light)
        if light_state == 0:
            print("Light Detected")
        elif light_state == 1:
            print("Light Not Detected")
        light_state = nose.run()
        time.sleep(.3)



if __name__ == '__main__':  # Program starting from here
    nose.run()
