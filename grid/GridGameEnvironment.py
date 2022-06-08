from GridGame import GridGame
from GridGameInterface import GridGameInterface

import numpy as np
import gym
from gym import spaces
from typing import Optional

#not working for now, see
#https://www.gymlibrary.ml/content/environment_creation/


class GridEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 10}

    def __init__(self, n: int = 10, render_mode="human"):
        self.game = GridGame(n)

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, n - 1, shape=(2,), dtype=int),
                "target": spaces.Box(0, n - 1, shape=(2,), dtype=int),
            }
        )

        self._action_to_direction = {
            0: self.game.moveUp(),
            1: self.game.moveDown(),
            2: self.game.moveLeft(),
            3: self.game.moveRight(),
        }

        # self.renderer = Renderer(render_mode, self._render_frame)

    def reset(self, seed: int = None, return_info=False, options=None):
        self.game.resetBoard(seed)
        self.renderer.reset()
        self.renderer.render_step()
        observation = self._get_obs()
        info = self._get_info()
        return (observation, info) if return_info else observation

    def render(self, mode="human"):
        self.renderer.Render()

    def _render_frame(self):
        return GridGameInterface(self.game).drawGrid()

    def _get_obs(self):
        return {"agent": self.game.location, "target": self.game.target}

    def _get_info(self):
        return {"distance": np.linalg.norm(
            self.game.location - self.game.target, ord=1)
        }

    def step(self, action) -> Tuple[ObsType, float, bool, dict]:
        self._action_to_direction[action]
        self.game.location = np.clip(
            self.game.location + self._action_to_direction[action],
            0, self.game.dim - 1 )
        won = self.game.isWon()
        reward = 1 if won else 0
        obs = self._get_obs()
        info = self._get_info()
        # self.




