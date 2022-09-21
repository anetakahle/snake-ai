import random

class Agent_hamilton_cycle():
    """
    An `Agent_hamilton_cycle` is an agent which always wins. He follows a fixed path - Hamiltonian path - i.e. it passes each vertex exactly once and ends up where it started. (A vertex is in this case every position of the playground).

    Attributes
    ----------

    Methods
    -------
    move():
    based on the inner state, follow the appropriate orders
    """
    def __init__(self):
        self._state = 0 #state 0 is looking for the wall
        self._state_counter = 5
    
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
            if self._state_counter != 0:
                self._state_counter -= 1
                return 0
            elif info_right == -2 and distance_right == 1:
                self._state_counter = 5
                self._state = 0
                return 0
            else:
                self._state_counter = 5
                self._state = 5
                return 1
        elif self._state == 5:
            self._state = 2
            return 1
        
