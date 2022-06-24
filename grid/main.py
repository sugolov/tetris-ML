import gym
from GridGameEnvironment import GridEnv

if __name__ == "__main__":
    env = GridEnv()
    # env.reset()

    n_actions = env.action_space.n
    n_states = (env.observation_space["agent"].high[0] + 1)**2
    n_states = n_states * (n_states - 1)

    print(n_actions)
    print(n_states)
