import numpy as np
import math
import random
import copy

class Agent_genetic_3():
    def __init__(self):
        self.input_size = 6
        self.hidden_layers = [3]
        self.weights = []
        self.biases = []
        self._create_layer(self.input_size, self.hidden_layers[0])
        self._create_layer(self.hidden_layers[0], 3)
        self._zip = list(zip(self.weights, self.biases))

    def _create_layer(self, n_inputs, n_neurons):
        self.weights.append(0.01 * np.random.randn(n_inputs, n_neurons))
        self.biases.append(0.01 * np.random.randn(n_neurons))

    # def _create_layer(self, n_inputs, n_neurons):
    #     self.weights.append(np.ones([n_inputs, n_neurons]))
    #     self.biases.append(np.ones(n_neurons))

    def forward(self, inputs):
        activations = inputs
        for weights, biases in self._zip:
            activations = activations @ weights + biases
            activations = 1 / (1 + math.e ** (-activations))
        return activations

    
    def create_input(self, info_left, distance_left, info_forward, distance_forward, info_right, distance_right):
        pass
    
    def move(self, *args):
        input = np.array(args)
        output = self.forward(input)
        res = output.argmax() - 1
        # print(res)
        return res
    
    def mutate(self):
        mutation_type = random.randint(0,1)
        if mutation_type == 0:
            idx1 = random.randint(0, len(self.weights)-1)
            idx2 = random.randint(0, len(self.weights[idx1])-1)
            idx3 = random.randint(0, len(self.weights[idx1][idx2])-1)
            self.weights[idx1][idx2, idx3] += 0.01 * np.random.randn(1)
        else:
            idx1 = random.randint(0, len(self.biases)-1)
            idx2 = random.randint(0, len(self.biases[idx1])-1)
            self.biases[idx1][idx2] += 0.01 * np.random.randn(1)
    
    