import numpy as np
import random

class Solve:
    
    def __init__(self, MDP, alpha, gama, num_episodes, epsilon):
        self.MDP = MDP
        self.Q_value = np.zeros((4, 12, 4))
        self.alpha = alpha
        self.gama = gama
        self.num_episodes = num_episodes
        self.epsilon = epsilon
        self.q_learning_reward_sum = np.zeros((self.num_episodes + 1))
        self.sarsa_reward_sum = np.zeros((self.num_episodes + 1))

    def policy(self, state):
        prob = random.random()

        if prob <= self.epsilon:
            rand = random.randint(0, 3)
            return rand
            
        q_slice = self.Q_value[state[0], state[1]]
        max_indices = np.argwhere(q_slice == np.max(q_slice)).flatten()

        rand = random.randint(0, len(max_indices)-1)

        return max_indices[rand]
    
    def Q_learning(self):
        for episode in range(self.num_episodes+1):
            
            current_state = np.array([0, 0], dtype=int)
    
            while True:  
                
                action = self.policy(current_state)

                reward, next_state = self.MDP.env_reaction(current_state.copy(), action)

                max_value = np.max(self.Q_value[next_state[0], next_state[1]])
                
                current_value = self.Q_value[current_state[0], current_state[1], action]
                
                self.Q_value[current_state[0], current_state[1], action] = (current_value + self.alpha
                                                             * (reward + self.gama*max_value - current_value))
                
                current_state = next_state
                
                self.q_learning_reward_sum[episode] += reward

                if next_state[0] == 0 and next_state[1] == 11:
                    break
    
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

                self.sarsa_reward_sum[episode] += reward 

                if next_state[0] == 0 and next_state[1] == 11:
                    break