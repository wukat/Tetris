from board import Board
from pygame.locals import *
import os
import pygame
import sys
 
size = 35
screen_size = [10 * size + 100, 18 * size + 3]
margin = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
       
                        
class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
        pygame.display.set_caption('Tetris')
        
        self.gamestate = 1  # 1 - run, 0 - exit, -1 - pause
        self.board = Board(self.surface)
        self.loop()
        
     
    def game_exit(self):
        pygame.quit()
                 
    def loop(self):
        while self.gamestate:
            for event in pygame.event.get():
                if self.gamestate == 1 and (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    self.gamestate = 0
                if (event.type == KEYDOWN and event.key == K_SPACE):
                    self.gamestate *= -1
                     
            keys = pygame.key.get_pressed()
        self.game_exit()
                      
if __name__ == '__main__':
    Game()

