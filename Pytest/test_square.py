import math
import pytest



@pytest.mark.great
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5



@pytest.mark.great
def testsquare():
   num = 7
   assert 7*7 == 49


@pytest.mark.others
def test_equality():
   assert 10 == 11