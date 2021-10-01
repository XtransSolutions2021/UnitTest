#import
from doctest import testmod

#function with doctest
def cube_cal(num):
  '''
  cube_cal function calculate te cube of the user input
  >>> cube_cal(3) 
  27
  '''
  result=num*(num*num)
  return result

#invoking
if __name__ == '__main__':
  testmod(name ='cube_cal', verbose = True)