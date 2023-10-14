

from Action import Action


def getActions01(start_ms):
    return [
        Action(start_ms + 50 / 1000, "press_w"),
        Action(start_ms + 2050 / 1000, "release_w"),
    ]
