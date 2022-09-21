from world import World
from matplotlib import pyplot as plt
import numpy as np
import copy
import random
import math


class Manager_simple():
    """
    A simple manager which can run multiple games for a given agent and
    show the results.

    Attributes
    ----------
    scores : list of int
        scores of the games
    step_counts : list of int
        a list of the numbers of the steps in each game
    agent_class: class of the agents

    Methods
    -------
    play_games(n_games : int):
        Plays `n_games` games.
    plot():
        plots the scores of the games
    """
    def __init__(self, agent_class):
        self.scores = []
        self.step_counts = []
        self.agent_class = agent_class

    def play_games(self, n_games):
        for ii in range(n_games):
            agent = self.agent_class()
            w = World()
            w.game(agent)
            self.scores.append(w.score)
            self.step_counts.append(w.steps)

    def plot(self):
        plt.plot(self.scores, '.')
        plt.ylim(0,63)
        plt.ylabel('score')
        plt.xlabel('game')



class Breeder():
    """
    A `Breeder` manages the breeding of genetic agents - it selects those with the best fitness and modifies them according to their own mutation function. It creates varieties of these top agents and they form a new generation. Each agent in the generation plays its games and again we select the best ones and so on. It can also display the results.

    Attributes
    ----------
    n_agents : the number of agents per one generation
    select_percentage : the percentage of top agents to be chosen to pass on their "genes".
    games_per_agent : how many games does one agent play
    agent_class : class of the agents
    agents : the actual agents  in the current generation
    generation_scores : the average scores of  each agent in each generation
    generation_steps : the average number of steps of  each agent in each generation

    Methods
    -------
    play_round():
    play `games_per_agent` games for each agent from the generation
    breed(n_gens):
    central function coordinating playing games, selecting top agents, and creating their offspring
    select_agents():
    select `select_percentage` of those agents with the best score
    make_offspring():
    make copies of the best agents and mutate each of them 
    plot():
    create a graph of average generation scores on the y-axis and generations on the x-axis
    """
    def __init__(self, agent_class, n_agents):
        self.n_agents = n_agents
        self.select_percentage = 15
        self.games_per_agent = 100
        self.agent_class = agent_class
        self.agents = np.array([agent_class() for x in range(self.n_agents)])
        self.generation_scores = []
        self.generation_steps = []
        
    def breed(self, n_gens):
        for generation in range(n_gens):
            self.play_round()
            selected = self.select_agents()
            self.agents = self.make_offspring(selected)
            # print(generation, self.generation_scores[-1])
            
    def play_round(self):
        round_scores = []
        round_steps = []
        for agent in self.agents:
            agent_scores = []
            agent_steps = []
            for gg in range(self.games_per_agent):
                w = World()
                w.game(agent)
                agent_scores.append(w.score)
                agent_steps.append(w.steps)
            round_scores.append(agent_scores)
            round_steps.append(agent_steps)
            
        self.scores = np.array(round_scores)
        # print(self.scores)
        # print()
        self.steps = np.array(round_steps)
        self.generation_scores.append(self.scores.mean())
        self.generation_steps.append(self.steps.mean())

    def select_agents(self):
        n = int(math.ceil(self.select_percentage/100 * self.n_agents))
        mean_scores = self.scores.mean(axis=1)
        indices = np.argsort(mean_scores)[-n:]
        return self.agents[indices]
  
    def make_offspring(self, selected): 
        ll = [*selected]
        for x in range(self.n_agents-len(selected)):
            random_agent = copy.deepcopy(random.choice(selected))
            random_agent.mutate()
            ll.append(random_agent)
        return np.array(ll)

    def plot(self):
        scores = np.array(self.generation_scores)
        mean_scores = scores.mean()
        plt.plot(scores)
        plt.axhline(scores.mean(), c="k")
