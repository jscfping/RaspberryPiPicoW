


from function_map import func_map
import io_module
from util_module import wait, sleep, get_ms, relax, getRandms
import io_module



gp17_pressed = False
gp18_pressed = False

while True:
    if io_module.is_gp17_on() and not gp17_pressed:
        io_module.on_led()
        func_map["press_mouse_left"]()
        gp17_pressed = True
    elif not io_module.is_gp17_on() and gp17_pressed:
        io_module.off_led()
        func_map["release_mouse_left"]()
        gp17_pressed = False
        
        
     
    if io_module.is_gp18_on() and not gp18_pressed:
        io_module.on_led()
        func_map["press_mouse_right"]()
        gp18_pressed = True
    elif not io_module.is_gp18_on() and gp18_pressed:
        io_module.off_led()
        func_map["release_mouse_right"]()
        gp18_pressed = False   
        
        
    relax(20,20)