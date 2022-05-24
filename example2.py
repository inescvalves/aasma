import gym
import random
import time

env_name = "ALE/Venture-v5"
env = gym.make(env_name, render_mode='human')

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)
env.unwrapped.get_action_meanings()

class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("Action size:", self.action_size)
        
    def get_action(self):
        return random.choice(range(self.action_size))


if __name__ == '__main__':
    agent = Agent(env)

    episodes = 2
    for episode in range(1, episodes+1):
        state = env.reset()
        done = False
        score = 0 
    
        while not done:
            time.sleep(0.1)
            action = agent.get_action()
            n_state, reward, done, info = env.step(action)
            score+=reward
    
        print('Episode:{} Score:{}'.format(episode, score))
    env.close()
    