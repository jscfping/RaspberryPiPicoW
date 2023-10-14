

import board
from digitalio import DigitalInOut, Direction, Pull


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

sw = DigitalInOut(board.GP16)
sw.direction = Direction.INPUT
sw.pull = Pull.DOWN


def on_led():
    led.value = 1


def off_led():
    led.value = 0


def is_on():
    return sw.value
