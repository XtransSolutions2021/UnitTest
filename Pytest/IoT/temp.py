import time  # for delay functions
from past.builtins import raw_input

#arduino = serial.Serial('com4', 9600)  # Create Serial port object called arduinoSerialData
time.sleep(2)  # wait for 2 secounds for the communication to get established


#print(arduino.readline()) #read the serial data and print it as line
print("Enter 1 to 100")
def func1(temp):
    assert type(temp) == int
    assert humidity < 100
    return temp


def func2(humidity):
    assert type(humidity) == int
    assert humidity < 100
    return humidity

while 1:  # Do this in loop

    print("Enter Temperature_Value")
    temp = raw_input()# get input from user
    print("Enter Humidity_Value")
    humidity = raw_input()  # get input from user
    print("Temperature = "+str(temp)+", Humidity = "+str(humidity))
    if (temp >= '20'):  # if the value is 1
        #arduino.write('1')  # send 1
        print("Temperature High")
    else:
        print("Temperature Low")
        time.sleep(1)

    if (humidity >= '50'):  # if the value is 0
        #arduino.write('0')  # send 0
        print("Humidity Low")
    else:
        print("Humidity High")

        time.sleep(1)

    #if temp > '100' or humidity > '100':
       # print("Value Error: Please Enter The Value Between 1 to 100")


        #time.sleep(1)

