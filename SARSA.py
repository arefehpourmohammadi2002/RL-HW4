import numpy as np
import random


class SARSA:
    def __init__(self, MDP, alpha, gama, num_episodes, epsilon):
        self.MDP = MDP
        self.Q_value = np.zeros((4, 12, 4))
        self.alpha = alpha
        self.gama = gama
        self.num_episodes = num_episodes
        self.epsilon = epsilon
        self.reward_sum = np.zeros((self.num_episodes + 1))

    def policy(self, state):
        prob = random.random()

        if prob <= self.epsilon:
            return random.randint(0, 3)
            
        return np.argmax(self.Q_value[state[0], state[1]])
    
    def SARSA(self):
        for episode in range(1, self.num_episodes+1):
            
            current_state = np.array([0, 0], dtype=int)
            action = self.policy(current_state)

            while True:  

                reward, next_state = self.MDP.env_reaction(current_state.copy(), action)
                next_action = self.policy(next_state)
                
                next_value = self.Q_value[next_state[0], next_state[1], next_action]
                current_value = self.Q_value[current_state[0], current_state[1], action]
                
                self.Q_value[current_state[0], current_state[1], action] = (current_value + self.alpha
                                                             * (reward + self.gama*next_value - current_value))
                
                current_state = next_state
                action = next_action

                self.reward_sum[episode] += reward 

                if next_state[0] == 0 and next_state[1] == 11:
                    break


                
