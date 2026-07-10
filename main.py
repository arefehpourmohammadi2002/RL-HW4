from MDP import MDP
from Q_learning import QLearning
from SARSA import SARSA
from draw import Draw
import numpy as np

alpha = 0.1
gama = 1 
num_episodes = 500
epsilon = 0.1
n_runs = 100

q_curve = np.zeros(num_episodes)
s_curve = np.zeros(num_episodes)

for run in range(n_runs):
    MDP_obj = MDP()

    Q_learning_obj = QLearning(MDP_obj, alpha, gama, num_episodes, epsilon)
    Q_learning_obj.Q_learning()

    SARSA_obj = SARSA(MDP_obj, alpha, gama, num_episodes, epsilon)
    SARSA_obj.SARSA()

    q_curve += Q_learning_obj.reward_sum[1:]
    s_curve += SARSA_obj.reward_sum[1:]

q_curve /= n_runs
s_curve /= n_runs

draw_now = Draw(q_curve, s_curve)
draw_now.plot()

for state in MDP_obj.states:
    print(state)
    print(np.argmax(Q_learning_obj.Q_value[state[0], state[1]]))
    print(np.argmax(SARSA_obj.Q_value[state[0], state[1]]))



