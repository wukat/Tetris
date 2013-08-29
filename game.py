from board import Board
from button import Button
from consts import screen_size, NCOLS, size, NROWS, WHITE, backgroundcolor
from game_over_screen import GameOverScreen
from pygame.locals import *
from start_screen import StartScreen
from text import Text
import os
import pygame
import sys
       
                        
class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
        pygame.display.set_caption('Tetris by wukat')
        self.startScreen = StartScreen(self.surface)
        self.gamestate = self.startScreen.loop()  # 1 - run, 0 - exit, -1 - pause
        self.overScreen = GameOverScreen(self.surface)
        self.board = Board(self.surface)
        self.quit = Button(self.surface, "QUIT", screen_size[0] - 60, screen_size[1] - 30, 25)
        self.pause = Button(self.surface, "PAUSE", screen_size[0] - 76, screen_size[1] - 65, 25)
        self.gameOverText = Text(self.surface, "GAME OVER", True, 70, WHITE, backgroundcolor, screen_size[0] // 2, screen_size[1] * 3/8)
        if self.gamestate:
            while self.loop():
                pass
        else:
            self.game_exit()

    def game_exit(self):
        pygame.quit()
                 
    def loop(self):
        self.board.reset()
        self.pause.draw()
        self.quit.draw()
        self.acttime = 0
        self.hideMouse()
        
        while self.gamestate:
            if self.readEvents() == 1:
                self.readKeys()
                
                if -(self.acttime - pygame.time.get_ticks()) > self.board.time:
                    self.board.block.moveDown()
                    self.acttime = pygame.time.get_ticks()
                    
                self.board.actualize(self.board.check())
                self.board.draw()
                
                if self.board.isGameOver():
                    self.gameOverText.show()
                    pygame.display.update()
                    pygame.time.wait(1000)
                    self.overScreen.show(self.board.point)
                    return self.overScreen.loop()       
        return 0
        
    def hideMouse(self):
        x, y = pygame.mouse.get_pos()
        if x >= 0 and x <= NCOLS * size + 5 and y >= 0 and y <= NROWS * size + 5:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
            
    def readEvents(self):
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)) or (event.type == MOUSEBUTTONDOWN and self.quit.checkIfHover(pygame.mouse.get_pos())):
                self.gamestate = 0
            elif (event.type == KEYDOWN and event.key == K_SPACE) or (event.type == MOUSEBUTTONDOWN and self.pause.checkIfHover(pygame.mouse.get_pos())):
                self.gamestate *= -1
            elif (event.type == KEYDOWN and (event.key == K_w or event.key == K_UP)):
                self.board.block.rotate()
            elif event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if self.quit.checkIfHover(pos):
                    self.quit.hover = 1
                else:
                    self.quit.hover = 0
                if self.pause.checkIfHover(pos):
                    self.pause.hover = 1
                else:
                    self.pause.hover = 0
                self.pause.drawBorder()
                self.quit.drawBorder()
                self.hideMouse()
                
        return self.gamestate
                
    def readKeys(self):
        keys = pygame.key.get_pressed()    
        if keys[K_s] or keys[K_DOWN]:
            self.board.block.moveDown()  
            pygame.time.wait(100)  
        elif keys[K_d] or keys[K_RIGHT]:
            self.board.block.move(1, 0)
            pygame.time.wait(100)
        elif keys[K_a] or keys[K_LEFT]:
            self.board.block.move(-1, 0)
            pygame.time.wait(100)
        
                          
if __name__ == '__main__':
    Game()