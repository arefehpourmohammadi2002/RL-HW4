import numpy as np


'''
in action array 0 means up, 1 means down 
2 means right and 3 means left
'''
class MDP:
    def __init__(self):
        self.states = np.zeros((48, 2), dtype=int)
        index = 0
        for i in range(4):
            for j in range(12):
                self.states[index] = [i, j]
                index += 1

        self.actions = np.arange(0, 4) 

    def env_reaction(self, state, action):

        reward = -1
        
        if action == 0 and state[0] != 3:
            state[0] += 1
        
        elif action == 1 and state[0] != 0:
            state[0] -= 1
        
        elif action == 2 and state[1] != 11:
            state[1] += 1

        elif action == 3 and state[1] != 0:
            state[1] -= 1 

        if state[0] == 0 and state[1] != 0 and state[1] != 11:
            state[0] = 0
            state[1] = 0
            reward = -100

        return reward, state
