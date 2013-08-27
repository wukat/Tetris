from blocks import LongBlock, Block
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
        self.block = LongBlock(0, self.board.board1, self.board.board)
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
            
            self.board.draw()         
            keys = pygame.key.get_pressed()
            if keys[K_s]:
                self.block.moveDown()
                self.block.draw()
                pygame.time.Clock().tick(1)
            elif keys[K_d]:
                self.block.moveRight()
                self.block.draw()
                pygame.time.Clock().tick(1)
            elif keys[K_a]:
                self.block.moveLeft()
                self.block.draw()
                pygame.time.Clock().tick(1)
            elif keys[K_w]:
                self.block.rotate()
                self.block.draw()
                pygame.time.Clock().tick(1)
            if self.block.checkIfLays():
                self.block = LongBlock(0, self.board.board1, self.board.board)
        self.game_exit()
                      
if __name__ == '__main__':
    Game()

