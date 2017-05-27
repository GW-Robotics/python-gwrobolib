import pygame
import serial

from time import sleep

pygame.init()
pygame.joystick.init()

_joystick = pygame.joystick.Joystick(0)
_joystick.init()

ser = serial.Serial('COM7', baudrate = 9600, timeout = 0.5)

raw_input('Type something to start')

last_value = [0.0,0.0,0.0,0]

while True:
    pygame.event.pump()
    values = "[{0:.2f},{1:.2f},{2:.2f},{3:d}]\n".format(-_joystick.get_axis(1), _joystick.get_axis(0), _joystick.get_axis(4), _joystick.get_button(5))

    if not last_value == values:
        ser.write(values)
        print values

    last_value = values
        
    sleep(0.1)
