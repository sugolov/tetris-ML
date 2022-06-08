import numpy as np
import pygame
import sys
from GridGame import GridGame


class GridGameInterface:
    # board options

    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    RED = (200, 0, 0)
    GREEN = (0, 200, 0)
    BLUE = (0, 0, 200)
    WINDOW_DIM = 800

    def __init__(self, game=GridGame(10)):
        self.game = game
        self.N_BLOCKS = game.dim

    def main(self):
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((self.WINDOW_DIM, self.WINDOW_DIM))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(self.BLACK)

        for _ in range(10):
            self.game.resetBoard()
            while not self.game.isWon():
                self.drawGrid()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        self.processKey(event)
                    if (self.game.location == self.game.target).all():
                        SCREEN.fill(self.WHITE)
                pygame.display.update()
            pygame.time.wait(1000)

    def drawGrid(self):
        blockWidth = self.WINDOW_DIM / self.N_BLOCKS
        for x in range(self.N_BLOCKS):
            for y in range(self.N_BLOCKS):
                rect = pygame.Rect(blockWidth * x,
                                   blockWidth * y,
                                   blockWidth, blockWidth)
                if (np.array([y, x]) == self.game.location).all():
                    pygame.draw.rect(SCREEN, self.BLUE, rect)
                elif (np.array([y, x]) == self.game.target).all():
                    pygame.draw.rect(SCREEN, self.RED, rect)
                else:
                    pygame.draw.rect(SCREEN, self.BLACK, rect, width=0)

    def processKey(self, event):
        match event.key:
            case pygame.K_LEFT:
                return self.game.moveLeft()
            case pygame.K_RIGHT:
                return self.game.moveRight()
            case pygame.K_UP:
                return self.game.moveUp()
            case pygame.K_DOWN:
                return self.game.moveDown()
