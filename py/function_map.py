

import keyboard_module
import mouse_module


def press_mouse_left():
    mouse_module.send_mouse_left_press()


def release_mouse_left():
    mouse_module.send_mouse_left_release()


def press_mouse_right():
    mouse_module.send_mouse_right_press()


def release_mouse_right():
    mouse_module.send_mouse_right_release()


def press_w():
    keyboard_module.send_w_press()


def release_w():
    keyboard_module.send_w_release()


def press_s():
    keyboard_module.send_s_press()


def release_s():
    keyboard_module.send_s_release()


def press_a():
    keyboard_module.send_a_press()


def release_a():
    keyboard_module.send_a_release()


def press_d():
    keyboard_module.send_d_press()


def release_d():
    keyboard_module.send_d_release()


def press_space():
    keyboard_module.send_space_press()


def release_space():
    keyboard_module.send_space_release()


func_map = {
    "press_mouse_left": press_mouse_left,
    "release_mouse_left": release_mouse_left,


    "press_mouse_right": press_mouse_right,
    "release_mouse_right": release_mouse_right,


    "press_w": press_w,
    "release_w": release_w,


    "press_s": press_s,
    "release_s": release_s,


    "press_a": press_a,
    "release_a": release_a,


    "press_d": press_d,
    "release_d": release_d,


    "press_space": press_space,
    "release_space": release_space,
}
