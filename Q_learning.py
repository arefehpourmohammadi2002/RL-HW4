import numpy as np

class QLearning:
    def __init__(self, MDP, alpha, gama):
        self.MDP = MDP
        self.Q_value = np.zeros((4, 11, 4))
        self.alpha = alpha
        self.gama = gama

    def Q_learning(self):
        for _ in range(num_episodes):
            
            current_state = np.array([0, 0], dtype= int)

            while next_state[0] != 0 and next_state[1] != 11:  

                action = with_E_greedy_algorithm(current_state)

                reward, next_state = self.MDP.env_reaction(current_state, action)

                max_value = np.max(self.Q_value, axis=2)
                current_value = self.Q_value[current_state[0], current_state[1], action]
                self.Q_value[current_state[0], current_state[1], action] = (current_value + self.alpha
                                                             * (reward + self.gama*max_value - current_value))
                
                current_state = next_state
                
