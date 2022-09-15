import numpy as np
import math
import random
import copy

class Agent_genetic_3():
    def __init__(self):
        self.input_size = 6
        self.output_size = 3
        self.nodes = {} #key id, val object
        
        # self.input_output_nodes = [] #dfs
        
        self.create_minimal_graph(self.input_size, self.output_size)
        
        
        
    def create_minimal_graph(size_in, size_out):
        
        for i in range(size_in):
            node = Node(id=i, input_, children=[range(size_in, size_in + size_out)])
            self.nodes[i] = node

        for i in range(size_in, size_in + size_out):
            node = Node(id=i, output_, parents=[range(size_in)])
            self.nodes[i] = node
  

        
    def forward(self, inputs):
        #dfs
        prerequsities_acomplished = [*[range(self.input_size)]]
        individual_prerequisites = [] #parents
        priority_quene = [] #id, parents
        outputs = []
        
        for i in range(self.input_size):
            in_node = self.nodes[i]
            for idx, child in enumerate(in_node.children):
                child.parents_b += [inputs[i]]
                child.parents_w += [in_node.children_w[idx]]
                if child.id not in priority_quene:
                    priority_quene.append(child.id)
                    individual_prerequisites.append(child.parents)
                
        while len(priority_quene) != 0:
            for i in len(priority_quene):
                for j in individual_prerequisites[i]:
                    if j not in prerequsities_acomplished:
                        return # chceme se vratit do vnejsiho foru
                    node = priority_quene.pop(i)
                    for prereq in individual_prerequisites.pop(i):
                        if not prereq in prerequsities_acomplished:
                            prerequsities_acomplished.append(prereq)
                    
                    input_ = 0
                    for i in len(node.parents_b):
                        input_ += node.parents_b[i] * node.parents_w[i]
                    
                    input_ += node.bias
                    input_ = node.use_activ_f(node.activ_f, input_)
                    
                    
                    
                    if len(node.children) != 0:
                        for idx, child in enumerate(in_node.children):
                            child.parents_b += [input_]
                            child.parents_w += [node.children_w[idx]]
                            
                            if child.id not in priority_quene:
                                priority_quene.append(child.id)
                                individual_prerequisites.append(child.parents)
                    
                    
                    else:
                        outputs.append((node.id, input_))
        
        outputs = outputs.sort(key=lambda i:i[0])
        outputs = [tup[1] for tup in outputs]
        return outputs
            
            
    
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
        return res
    
    def mutate(self):
        # pridat neuron, zmenit vahu, zmenit bias, vynulovat vahu nebo bias, smazat hranu
    
    
    
class Node():
    __init__(self, id, type, parents, children):
        self.id = 0
        self.type = type
        self.parents = [] #pro spravny pruchod acyklickeho grafu
        self.parents_b = [] #actually inputs/biases :ddd 
        self.parents_w = []
        
        self.bias = 0
        self.activ_f = "identity"
        self.children = [] 
        self.weights_c = []
        
        self.create_minimal_graph(type, parents, children)
        
    def create_minimal_graph(self, type, parents, children):        
        
        if type == input_:
            self.weights_c.append(0.01 * np.random.randn(len(self.children)))
            self.bias = 0
            
        else:
            self.bias = 0.01 * np.random.randn(1)
            self.parents = parents
            # elif type == output_:
            #     self.weights_p.append(0.01 * np.random.randn(len(self.parents)))
            # self.activ_f = "relu"

            
    def use_activ_f(self, activ_f, input_):
        pass
        
        
        