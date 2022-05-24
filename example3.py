import gym
import gym_maze
import random
import time

env = gym.make('maze-v0')

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

class Agent_random():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("Action size:", self.action_size)
        
    def get_action(self):
        return random.choice(range(self.action_size))

class Agent_smart():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("Action size:", self.action_size)
        
    def get_action(self):
        return random.choice(range(self.action_size))


if __name__ == '__main__':
    agent_random = Agent_random(env)
    agent_smart = Agent_smart(env)

    episodes = 2
    for episode in range(1, episodes+1):
        state = env.reset()
        done = False
        score = 0 
        #first episode - random agent
        if (episode == 1):
            while not done:
                action = agent_random.get_action()
                env.render()
                n_state, reward, done, info = env.step(action)
                env.render()
                score+=reward
        #second episode - smart agent
        if (episode == 2):
            while not done:
                action = agent_smart.get_action()
                env.render()
                n_state, reward, done, info = env.step(action)
                env.render()
                score+=reward
    
        print('Episode:{} Score:{}'.format(episode, score))
    env.close()
    