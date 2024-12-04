import board
import time
import pwmio
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn

pot = AnalogIn(board.A1)
blue = pwmio.PWMOut(board.D2, frequency=5000, duty_cycle=0)
green = pwmio.PWMOut(board.D3, frequency=5000, duty_cycle=0)


while True:
    blue.duty_cycle = pot.value
    green.duty_cycle = 65535 - pot.value
