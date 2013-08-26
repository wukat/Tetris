from pygame.locals import *
import os
import pygame
import sys
 
screen_size = [800, 600]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
               
class Game(object):
    def __init__(self):
        pygame.init()
        flag = DOUBLEBUF
  
        self.surface = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Tetris')
        
        self.gamestate = 1  # 1 - run, 0 - exit, -1 - pause
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
            if keys[K_s]:
                Block(self.surface)
                pygame.display.flip()
        self.game_exit()
         
class Block():
    def __init__(self, surface):
        pygame.draw.rect(surface, WHITE, [75, 10, 50, 20])
         
if __name__ == '__main__':
    Game()

