import random

class Agent_hemilton_cycle():
    def __init__(self):
        self._state = 0 #state 0 is looking for the wall
        self._state_4_counter = 5
    
    def move(self, info_left, distance_left, info_forward, distance_forward, info_right, distance_right):
        if self._state < 3:
            if info_forward > -2 or distance_forward > 1:
                return 0
            else:
                self._state += 1
                return -1
        elif self._state == 3:
            self._state = 4
            return -1
        elif self._state == 4:
            if self._state_4_counter != 0:
                self._state_4_counter -= 1
                return 0
            elif info_right == -2 and distance_right == 1:
                self._state_4_counter = 5
                self._state = 0
                return 0
            else:
                self._state_4_counter = 5
                self._state = 5
                return 1
        elif self._state == 5:
            self._state = 2
            return 1
        
