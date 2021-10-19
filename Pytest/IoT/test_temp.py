import math
import pytest
#import temp
from past.builtins import raw_input

def test_greater_temp():
   temp = 100
   assert type(temp) == int
   assert temp > 40
   return temp


def test_humidity():
   humidity = 100
   assert type(humidity) == int

   assert humidity < 50
   return humidity
