from world import World
from matplotlib import pyplot as plt
import numpy as np
import copy
import random
import math


class Manager_simple():
    """
    A simple manager which can run multiple games for a given agent and
    show the resuts.

    Attributes
    ----------
    scores : list of int
        scores of the games
    step_counts : list of int
        a list of the numbers of the steps in each game
    agent_class: class object
        class of the agents

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
            self.agents = self.make_offsprings(selected)
            print(generation, self.generation_scores[-1])
            
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
  
    def make_offsprings(self, selected): 
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
