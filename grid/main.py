import gym
import numpy
import random

# we train a model on the usual cartpole example

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state = env.reset()

    n = 10
    for i in range(n):
        action = env.action_space.sample()
        env.step(action)
        env.render()
    env.close()

    print(env.action_space)
    print(env.observation_space)

