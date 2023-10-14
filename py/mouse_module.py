import usb_hid
from adafruit_hid.mouse import Mouse


mouse = Mouse(usb_hid.devices)


def send_mouse_left_press():
    mouse.press(Mouse.LEFT_BUTTON)


def send_mouse_left_release():
    mouse.release(Mouse.LEFT_BUTTON)


def send_mouse_right_press():
    mouse.press(Mouse.RIGHT_BUTTON)


def send_mouse_right_release():
    mouse.release(Mouse.RIGHT_BUTTON)
