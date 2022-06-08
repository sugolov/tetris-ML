import numpy as np

class GridGame:
    TARGET_CONSTANT = 777
    AGENT_CONSTANT = 1

    def __init__(self, n):
        self.dim = n
        self.board = np.zeros((self.dim, self.dim))
        self.location = np.zeros(2)
        self.target = np.zeros(2)
        self.resetBoard()

    def resetBoard(self, seed=None):
        np.random.seed(seed)


        self.board = np.zeros((self.dim, self.dim))
        #self.target = (np.random.randint(0, self.dim, 2))
        self.target = np.array([0, 0])

        start_loc = (np.random.randint(0, self.dim, 2))

        while (start_loc == self.target).all():
            start_loc = (np.random.randint(0, self.dim, 2))

        self.location = start_loc

        # number representing target in board
        self.board[self.target[0], self.target[1]] = GridGame.TARGET_CONSTANT
        self.board[self.location[0], self.location[1]] = GridGame.AGENT_CONSTANT

    def moveUp(self):
        self.location = np.clip(self.location - np.array([1, 0]), 0, self.dim - 1)

    def moveDown(self):
        self.location = np.clip(self.location + np.array([1, 0]), 0, self.dim - 1)

    def moveLeft(self):
        self.location = np.clip(self.location - np.array([0, 1]), 0, self.dim - 1)

    def moveRight(self):
        self.location = np.clip(self.location + np.array([0, 1]), 0, self.dim - 1)

    def isWon(self):
        return (self.target == self.location).all()