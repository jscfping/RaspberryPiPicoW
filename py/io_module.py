

import board
from digitalio import DigitalInOut, Direction, Pull


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

sw = DigitalInOut(board.GP16)
sw.direction = Direction.INPUT
sw.pull = Pull.DOWN


gp17 = DigitalInOut(board.GP17)
gp17.direction = Direction.INPUT
gp17.pull = Pull.DOWN



gp18 = DigitalInOut(board.GP18)
gp18.direction = Direction.INPUT
gp18.pull = Pull.DOWN



def on_led():
    led.value = 1


def off_led():
    led.value = 0


def is_on():
    return sw.value

def is_gp17_on():
    return gp17.value

def is_gp18_on():
    return gp18.value
