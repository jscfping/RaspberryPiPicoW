

from Action import Action


def getActions03(start_ms):
    return [
    Action(start_ms + 0, "press_s"),
    
    
    Action(start_ms + 400, "press_mouse_left"),
    Action(start_ms + 500, "release_mouse_left"),
    
    
    Action(start_ms + 700, "press_mouse_left"),
    Action(start_ms + 800, "release_mouse_left"),
    
    
    Action(start_ms + 1100, "press_mouse_left"),
    Action(start_ms + 1111, "press_a"),
    Action(start_ms + 1200, "release_mouse_left"),
    Action(start_ms + 1255, "release_s"),
    Action(start_ms + 1355, "press_w"),
    
    
    Action(start_ms + 1300, "press_mouse_right"),
    Action(start_ms + 1400, "release_mouse_right"),
    
    
    Action(start_ms + 1455, "press_d"),
    Action(start_ms + 1465, "release_w"),
    Action(start_ms + 1500, "press_mouse_right"),
    Action(start_ms + 1600, "release_mouse_right"),
    Action(start_ms + 1666, "release_a"),
    Action(start_ms + 1777, "press_s"),
    
    
    Action(start_ms + 1900, "press_mouse_right"),
    Action(start_ms + 2000, "release_mouse_right"),
    
    
    Action(start_ms + 2300, "press_mouse_right"),
    Action(start_ms + 2400, "release_mouse_right"),
    Action(start_ms + 2477, "release_d"),
    
    
    Action(start_ms + 2500, "press_mouse_right"),
    Action(start_ms + 2600, "release_mouse_right"),
    
    
    Action(start_ms + 2800, "press_space"),
    Action(start_ms + 2900, "release_space"),
    Action(start_ms + 3333, "release_s"),
    
    
    ]
