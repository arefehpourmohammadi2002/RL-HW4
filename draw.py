import matplotlib.pyplot as plt

class Draw:

    def __init__(self, Q_learning_sum, SARSA_sum):
        self.Q_learning_sum = Q_learning_sum
        self.SARSA_sum = SARSA_sum

    def plot(self):

        plt.plot(self.Q_learning_sum, label='Q-learning')
        plt.plot(self.SARSA_sum, label='Sarsa')
        plt.ylim(-200, 0) 
        plt.xlabel('Episodes')
        plt.ylabel('Sum of rewards during episode')
        plt.legend()

        plt.savefig("compare.png")
