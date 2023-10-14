
from function_map import func_map
from action_02 import getActions02
from action_03 import getActions03
from action_04 import getActions04
from action_05 import getActions05
import io_module
from util_module import wait, sleep, get_ms, relax, getRandms

allActionList = [getActions02, getActions04, getActions03, getActions04, getActions05]
actionList = []
i = 0

while True:
    if (io_module.is_on()):
        #actionList.append(getActions02(get_ms()))
        #actionList.append(allActionList[getRandms(0, len(allActionList) - 1)](get_ms())) 
        actionList.append(allActionList[i](get_ms()))
        #actionList.append(allActionList[3](get_ms()))
        i = i + 1
        
        if (i >= len(allActionList)):
            i = 0
 
        while actionList:
            newActionList = []
            for actions in actionList:
                current_ms = get_ms()
                newActions = [a for a in actions if a.ms > current_ms]
                for act in actions:
                    #print("c:" + str(current_ms) + ", act.ms:" + str(act.ms))
                    if (current_ms >= act.ms):
                        if act.cmdName in func_map:
                            #print(act.cmdName)
                            func_map[act.cmdName]()
                actions = [a for a in actions if a.ms > current_ms]
                if newActions:
                    newActionList.append(newActions)
            actionList = newActionList
            sleep(50)
            if (not io_module.is_on()):
                func_map["release_mouse_left"]()
                func_map["release_mouse_right"]()
                func_map["release_space"]()
                func_map["release_w"]()
                func_map["release_a"]()
                func_map["release_s"]()
                func_map["release_d"]()
                break
            #print(1)

    #wait()
    relax(150,500)
    #sleep(200)
    #print(0)



