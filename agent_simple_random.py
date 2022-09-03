import random

class Agent_simple_random():
    def __init__(self):
        pass

    def move(self, info_left, distance_left, info_forward, distance_forward, info_right, distance_right):

        if info_left == -1:
            return -1
        elif info_right == -1:
            return 1
        elif info_forward == -1:
            return 0

        possible_actions = []
        if not (info_forward != 0 and distance_forward == 1):
            possible_actions.append(0)
        if not (info_right != 0 and distance_right == 1):
            possible_actions.append(1)
        if not (info_left != 0 and distance_left == 1):
            possible_actions.append(-1)

        if len(possible_actions) == 0:
            return 0
        else:
            return random.choice(possible_actions)

