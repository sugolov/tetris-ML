from GridGame import GridGame
from GridGameInterface import GridGameInterface

import numpy as np
import gym
import pygame
from gym import spaces

class GridEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 10}

    def __init__(self, n: int = 10, render_mode="human"):
        self.dim = n
        self.game = GridGame(n)

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, n - 1, shape=(2,), dtype=int),
                "target": spaces.Box(0, n - 1, shape=(2,), dtype=int)
            }
        )
        # Used in render

        self.window = None
        self.clock = None

    def reset(self, seed: int = None, return_info=False, options=None):
        self.game.resetBoard(seed)
        self.render()
        observation = self._get_obs()
        info = self._get_info()
        return (observation, info) if return_info else observation

    def render(self, mode="human", s_dim=800):

        if self.window is None and mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((s_dim, s_dim))
        if self.clock is None and mode == "human":
            self.clock = pygame.time.Clock()

        self.window.fill((0, 0, 0))
        r_width = s_dim / self.dim

        rect_target = pygame.Rect(r_width * self.game.target[1],
                                  r_width * self.game.target[0],
                                  r_width, r_width)
        rect_location = pygame.Rect(r_width * self.game.location[1],
                                    r_width * self.game.location[0],
                                    r_width, r_width)
        pygame.draw.rect(self.window, (200, 0, 0), rect_target)
        pygame.draw.rect(self.window, (0, 0, 200), rect_location)
        pygame.display.update()
        pygame.time.wait(1000)


    def _get_obs(self):
        return {"agent": self.game.location, "target": self.game.target}

    def _get_info(self):
        return {"distance": np.linalg.norm(
            self.game.location - self.game.target, ord=1)
        }

    def step(self, action):

        match action:
            case 0:
                return self.game.moveLeft()
            case 1:
                return self.game.moveRight()
            case 2:
                return self.game.moveUp()
            case 3:
                return self.game.moveDown()

        won = self.game.isWon()
        reward = 1 if won else 0
        obs = self._get_obs()
        info = self._get_info()
        return obs, reward, won, info

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()