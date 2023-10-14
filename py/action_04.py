

from Action import Action

#SD
def getActions04(start_ms):
    return [
    Action(start_ms + 0, "press_w"),
    
    Action(start_ms + 100, "press_mouse_left"),
    Action(start_ms + 200, "release_mouse_left"),
    
    Action(start_ms + 300, "press_mouse_right"),
    Action(start_ms + 400, "release_mouse_right"),
    
    Action(start_ms + 500, "release_w"),
    Action(start_ms + 530, "press_s"),
    Action(start_ms + 800, "press_space"),
    Action(start_ms + 900, "release_space"),
    Action(start_ms + 1000, "release_s"),
    
    Action(start_ms + 1300, "press_w"),
    Action(start_ms + 2100, "release_w")
    
    ]
