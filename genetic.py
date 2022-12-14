import numpy as np
import math
import random
import copy

class Agent_genetic_3():
    """
    An `Agent_genetic_3` is an agent based on an artificial neural network (NN) with 1 hidden layer of 3 neurons. It is designed to evolve used a genetic algorithm - create a generation of randomly inicialized agents, select the best and created offspring (mutated copies) from them.
    
    Attributes
    ----------
    input_size : the lenght of the input information
    hidden_layers : a list of layers where on each position there is a number of neurons (at this moment we only have one layer of 3 neurons)
    weights : weights for each neuron
    biases : biases for neurons
    
    Methods
    -------
    forward():
    Evaluate the changes in the input while interacting with the NN. (Basically just a multiplication of matrices)
    create_input():
    Just change the input so that it is easier for the NN to learn
    move():
    pick the max value from the list returned by forward function. The index of the max - 1 will be the action we will take
    mutate():
    choose randomly either a weight or a bias and add a random number to its value
    """
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
        if info_left > 0:
            info_left = -2
        if info_right > 0:
            info_right = -2
        if info_forward > 0:
            info_forward = -2
            
        distance_left = 1/ distance_left
        distance_forward = 1/distance_forward
        distance_right= 1/distance_right
        
        
    
    def move(self, *args):
        input = self.create_input(*args)        
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
    
    