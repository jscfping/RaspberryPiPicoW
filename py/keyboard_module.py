import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)


def send_key_press(key):
    keyboard.press(key)


def send_key_release(key):
    keyboard.release(key)


def send_w_press():
    send_key_press(Keycode.W)


def send_w_release():
    send_key_release(Keycode.W)


def send_s_press():
    send_key_press(Keycode.S)


def send_s_release():
    send_key_release(Keycode.S)


def send_a_press():
    send_key_press(Keycode.A)


def send_a_release():
    send_key_release(Keycode.A)


def send_d_press():
    send_key_press(Keycode.D)


def send_d_release():
    send_key_release(Keycode.D)


def send_space_press():
    send_key_press(Keycode.SPACE)


def send_space_release():
    send_key_release(Keycode.SPACE)
