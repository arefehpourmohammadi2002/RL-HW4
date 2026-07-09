
import numpy as np

class MDP:
    def __init__(self):
        self.states = np.zeros((4, 12), dtype=int)
        self.actions = np.arange(0, 4) # 0: up, 1: down, 2: right, 3:left
    
    def reward(self, state, action):

        reward = -1
        if (state[0] == 1 and state[1] != 0 and state[1] != 11 
            and action == 1): # the next state is in the cliff 
            state[0] = 0
            state[1] = 0
            reward = -100

        elif state[0] == 1 and state[1] == 11 and action == 1: # if entering the goal cell
            state[0] = 0
            state[1] = 11
            reward =  0

        elif action == 0 and state[0] != 3: # acttion is up 
            state[0] += 1
        
        elif action == 1 and state[0] != 0: # acttion is down 
            state[0] -= 1
        
        elif action == 2 and state[1] != 11: # acttion is right
            state[1] += 1

        elif action == 3 and state[1] != 0: # acttion is left
            state[1] -= 1 

        return reward, state
