from blocks import LongBlock
from board import Board
from consts import screen_size
from pygame.locals import *
import os
import pygame
import sys
       
                        
class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
        pygame.display.set_caption('Tetris by wukat')
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
            
            if self.gamestate == 1:    
                keys = pygame.key.get_pressed()
                if keys:
                    if keys[K_s]:
                        self.board.block.moveDown()    
                    elif keys[K_d]:
                        self.board.block.move(1, 0)
                    elif keys[K_a]:
                        self.board.block.move(-1, 0)
                    elif keys[K_w]:
                        self.board.block.rotate()
                    pygame.time.wait(100)
                
                self.board.draw()
                self.board.block.moveDown()
                pygame.time.wait(200)
                self.board.actualize(self.board.check())
                
        self.game_exit()
                      
if __name__ == '__main__':
    Game()

