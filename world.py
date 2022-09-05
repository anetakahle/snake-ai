import random
import math
import numpy as np
from ipywidgets import interactive
from matplotlib import pyplot as plt


class World:

    def __init__(self, size=8):
        self.size = size
        self.game_over = False
        self.score = 0
        self.steps = 0
        self.obs = np.zeros((self.size, self.size), dtype=int)
        middle = [math.floor((self.size + 1) / 2) - 1, math.ceil((self.size + 1) / 2) - 1]
        y = random.randint(*middle)
        x = random.randint(*middle)
        self.obs[y, x] = 1  # head
        self.obs[y + 1, x] = 2  # body
        self.generate_apple()
        self.history = [self.obs.copy()]
        
    def generate_apple(self):
        if self.score < 30:
            y = random.randint(0, self.size - 1)
            x = random.randint(0, self.size - 1)
            while self.obs[y, x] != 0:
                y = random.randint(0, self.size - 1)
                x = random.randint(0, self.size - 1)
        else:
            possible_positions = []
            for y in range(self.size):
                for x in range(self.size):
                    if self.obs[y, x] == 0:
                        possible_positions.append([y, x])
            y, x = random.choice(possible_positions)
        self.obs[y, x] = -1

        
    def step(self, action):
        if self.steps >= 500:
            self.game_over = True
        if self.game_over:
            return
        new_head_x, new_head_y, tail = self.move(action, self.obs)

        if (new_head_x > self.size - 1) or (new_head_y > self.size - 1) or (new_head_x < 0) or (new_head_y < 0) or (
                self.obs[new_head_y, new_head_x] > 1):
            self.game_over = True
        else:
            if self.obs[new_head_y, new_head_x] == -1:
                self.score += 1
                if self.score > 61:
                    self.game_over = True
                else:
                    self.generate_apple()
            else:
                self.obs[tail[0], tail[1]] = 0
            self.obs[new_head_y, new_head_x] = 1
        self.steps += 1
        self.history.append(self.obs.copy())
        
    def move(self, action, obs):
        tail_value = 0
        for y in range(self.size):
            for x in range(self.size):
                if obs[y, x] == 1:
                    head = [y, x]
                    obs[y, x] += 1
                elif obs[y, x] == 2:
                    neck = [y, x]
                    obs[y, x] += 1
                elif obs[y, x] > 2:
                    body = [y, x]
                    obs[y, x] += 1
                if obs[y, x] > tail_value:
                    tail = [y, x]
                    tail_value = obs[y, x]

        y = head[0] - neck[0]
        x = head[1] - neck[1]
        look_dir = [y, x]

        look_dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        look_dir_index = look_dirs.index(look_dir)
        head_movement = None

        if action == -1:  # left
            head_movement = look_dirs[look_dir_index - 1]
        elif action == 0:  # forward
            head_movement = look_dirs[look_dir_index]
        elif action == 1:  # right
            if look_dir_index == 3:
                head_movement = look_dirs[0]
            else:
                head_movement = look_dirs[look_dir_index + 1]

        new_head_y = head[0] + head_movement[0]
        new_head_x = head[1] + head_movement[1] 
        return new_head_x, new_head_y, tail
        
        
    def view_3_end(self):
        if self.game_over:
            return 0, 0, 0, 0, 0, 0
        tail_value = 0
        for y in range(self.size):
            for x in range(self.size):
                if self.obs[y, x] == 1:
                    head = [y, x]
                elif self.obs[y, x] == 2:
                    neck = [y, x]
                elif self.obs[y, x] == -1:
                    apple = [y, x]
                # elif self.obs[y, x] > 2:
                #     body = [y, x]
                # if self.obs[y, x] > tail_value:
                #     tail = [y, x]
                #     tail_value = self.obs[y, x]

        y = head[0] - neck[0]
        x = head[1] - neck[1]
        look_dir = [y, x]

        look_dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        look_dir_index = look_dirs.index(look_dir)
        info_left = 0
        distance_left = 1
        info_forward = 0
        distance_forward = 1
        info_right = 0
        distance_right = 1

        for ii in range(1, 4):
            shift_left = look_dirs[look_dir_index - 1]
            pixel_left_y = head[0] + ii * (shift_left[0])
            pixel_left_x = head[1] + ii * (shift_left[1])
            if (pixel_left_x > self.size - 1) or (pixel_left_y > self.size - 1) or (pixel_left_x < 0) or (
                    pixel_left_y < 0):  # if we can still move
                if info_left == 0:
                    info_left = -2
                    distance_left = ii
                break
            if self.obs[pixel_left_y, pixel_left_x] != 0:
                if info_left == 0:
                    info_left = self.obs[pixel_left_y, pixel_left_x]
                    distance_left = ii

        for ii in range(1, 4):
            shift_forward = look_dirs[look_dir_index]
            pixel_forward_y = head[0] + ii * (shift_forward[0])
            pixel_forward_x = head[1] + ii * (shift_forward[1])
            if (pixel_forward_x > self.size - 1) or (pixel_forward_y > self.size - 1) or (pixel_forward_x < 0) or (
                    pixel_forward_y < 0):  # if we can still move
                if info_forward == 0:
                    info_forward = -2
                    distance_forward = ii
                break
            if self.obs[pixel_forward_y, pixel_forward_x] != 0:
                if info_forward == 0:
                    info_forward = self.obs[pixel_forward_y, pixel_forward_x]
                    distance_forward = ii

        for ii in range(1, 4):
            if look_dir_index == 3:
                shift_right = look_dirs[0]
            else:
                shift_right = look_dirs[look_dir_index + 1]
            pixel_right_y = head[0] + ii * (shift_right[0])
            pixel_right_x = head[1] + ii * (shift_right[1])
            if (pixel_right_x > self.size - 1) or (pixel_right_y > self.size - 1) or (pixel_right_x < 0) or (
                    pixel_right_y < 0):  # if we can still move
                if info_right == 0:
                    info_right = -2
                    distance_right = ii
                break
            if self.obs[pixel_right_y, pixel_right_x] != 0:
                if info_right == 0:
                    info_right = self.obs[pixel_right_y, pixel_right_x]
                    distance_right = ii
        return info_left, distance_left, info_forward, distance_forward, info_right, distance_right

    def show_step(self, step):
        plt.figure(2)
        plt.matshow(self.history[step])
        plt.show()
    
    def replay(self):
        interactive_plot = interactive(self.show_step, step=(0, len(self.history)-1))
        output = interactive_plot.children[-1]
        output.layout.height = '450px'
        return interactive_plot
    
    def __repr__(self):
        lll = []
        for y in range(self.obs.shape[0]):
            ll = []
            for x in range(self.obs.shape[1]):
                if self.obs[y, x] == 0:


                    ll.append('  ')
                elif self.obs[y, x] > 1:
                    ll.append('░░')
                elif self.obs[y, x] == 1:
                    ll.append('██')
                else:
                    ll.append('◯◯')
            lll.append(''.join(ll))
        world = '|\n'.join(lll)
        gameover = ' Game Over' if self.game_over else ''
        return f"{world}| score={self.score} steps={self.steps} {gameover}"


