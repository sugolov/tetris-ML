import gym
import numpy as np
import random

import tensorflow as tf
import tensorflow.keras as tfk


# we train a model on the usual cartpole example

def model(input_shape, action_space):
    model = tfk.Sequential()
    model.add(tfk.Input(shape=input_shape))
    model.add(tfk.Dense(512, activation=tf.nn.relu,
                        initializers=tf.keras.initializers.he_uniform))
    model.add(tfk.Dense(256, activation=tf.nn.relu,
                        initializers=tf.keras.initializers.he_uniform))
    model.add(tfk.Dense(64, activation=tf.nn.relu,
                        initializers=tf.keras.initializers.he_uniform))
    model.add(tfk.Dense(action_space, activation=tf.nn.relu,
                        initializers=tf.keras.initializers.he_uniform))
    # mean squared error loss
    # default RMS prop parameters: https://pylessons.com/CartPole-reinforcement-learning

    model.compile(loss="mse", optimizer=tfk.optimizers.RMSprop(), metrics=["accuracy"])
    model.summary()

    return model


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
