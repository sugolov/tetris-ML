import gym
import numpy
import random

# we train a model on the usual cartpole example





if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state = env.reset()

    n = 100
    # 0, move left
    # 1, move right

    for i in range(n):
        action = env.action_space.sample()
        next_state, reward, done, info = env.step(action)
        print(i, next_state, reward, done, info, action)
        env.render()

    env.close()

    print(env.action_space)
    print(env.observation_space)

