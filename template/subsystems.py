import robotmap
import robotmath
import sensors
import gwrobolib

from nanpy import ArduinoApi, SerialManager, Servo, Ultrasonic
from time import sleep


# Connects the arduino and the raspberry pi through serial
try:
#    connection = SerialManager(device = '/dev/ttyACM0')
    connection = SerialManager()
    Arduino = ArduinoApi(connection = connection)
except:
    pass


class ExampleSubsystem(object):

    def __init__(self):
        pass
