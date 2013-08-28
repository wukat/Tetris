from blocks import LongBlock
from board import Board
from button import Button
from consts import screen_size, NCOLS, size, NROWS
from pygame.locals import *
from start_screen import StartScreen
import os
import pygame
import sys
       
                        
class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
        pygame.display.set_caption('Tetris by wukat')
        self.gamestate = StartScreen(self.surface).loop()  # 1 - run, 0 - exit, -1 - pause
        if self.gamestate:
            self.board = Board(self.surface)
            self.time = 1000
            self.quit = Button(self.surface, "QUIT", screen_size[0] - 60, screen_size[1] - 30, 25)
            self.quit.draw()
            self.loop()
        else:
            self.game_exit()

    def game_exit(self):
        pygame.quit()
                 
    def loop(self):
        self.acttime = 0
        while self.gamestate:
            for event in pygame.event.get():
                if self.gamestate == 1 and (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)) or (event.type == MOUSEBUTTONDOWN and self.quit.checkIfHover(pygame.mouse.get_pos())):
                    self.gamestate = 0
                elif (event.type == KEYDOWN and event.key == K_SPACE):
                    self.gamestate *= -1
                elif (event.type == KEYDOWN and (event.key == K_w or event.key == K_UP)):
                    self.board.block.rotate()
                elif event.type == MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    if self.quit.checkIfHover((x, y)):
                        self.quit.hover = 1
                    else:
                        self.quit.hover = 0
                    self.quit.drawBorder()
                    if x >= 0 and x <= NCOLS * size + 5 and y >= 0 and y <= NROWS * size + 5:
                        pygame.mouse.set_visible(False)
                    else:
                        pygame.mouse.set_visible(True)
                
            if self.gamestate == 1:
                keys = pygame.key.get_pressed()    
                if keys[K_s] or keys[K_DOWN]:
                    self.board.block.moveDown()    
                elif keys[K_d] or keys[K_RIGHT]:
                    self.board.block.move(1, 0)
                elif keys[K_a] or keys[K_LEFT]:
                    self.board.block.move(-1, 0)
                pygame.time.wait(100)
             
            self.board.draw()
            if -(self.acttime - pygame.time.get_ticks()) > self.time:
                self.board.block.moveDown()
                self.acttime = pygame.time.get_ticks()
            self.board.actualize(self.board.check())
            if self.board.isGameOver():
                self.gamestate = 0
                 
        self.game_exit()
                      
if __name__ == '__main__':
    Game()

