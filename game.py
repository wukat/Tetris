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
       
# main class       
class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
        pygame.display.set_caption('Tetris by wukat')
        self.startScreen = StartScreen(self.surface)
        self.gamestate = self.startScreen.loop()  # 1 - run, 0 - exit, -1 - pause
        self.overScreen = GameOverScreen(self.surface)
        self.board = Board(self.surface)  # games board
        
        self.quit = Button(self.surface, "QUIT", screen_size[0] - 60, screen_size[1] - 30, 25)
        self.pause = Button(self.surface, "PAUSE", screen_size[0] - 76, screen_size[1] - 65, 25)
        self.gameOverText = Text(self.surface, "GAME OVER", True, 70, WHITE, backgroundcolor, screen_size[0] // 2, screen_size[1] * 3 / 8)
        
          
        while self.loop():  # loop returns 1 - play again, 0 - quit
            pass
        self.game_exit()

    def game_exit(self):
        pygame.quit()
                 
    def loop(self):
        self.board.reset()  # initialization of everything 
        self.pause.draw()
        self.quit.draw()
        self.acttime = 0
        self.hideMouse()
        pygame.key.set_repeat(100, 100)
        
        while self.gamestate:  # main loop
            if not self.readEvents():
                temp = pygame.time.get_ticks()  # get time
                if -(self.acttime - temp) > self.board.time:  # time
                    self.board.block.moveDown()
                    self.acttime = temp
                    self.board.checkBlock()  # check if blocks lays
                self.board.draw()
                
                if self.board.isGameOver():  # when the game is over gameoverscreen runs
                    self.gameOverText.show()
                    pygame.display.update()
                    pygame.time.wait(1000)
                    self.overScreen.show(self.board.point)
                    return self.overScreen.loop()  # loop return 1 or 0 - restart or quit
        return 0
        
    def hideMouse(self):  # if mouse under the board, hide
        x, y = pygame.mouse.get_pos()
        if x >= 0 and x <= NCOLS * size + 5 and y >= 0 and y <= NROWS * size + 5:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
            
    def readEvents(self):  # events
        flag = 0
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)) or (event.type == MOUSEBUTTONDOWN and self.quit.checkIfHover(pygame.mouse.get_pos())):
                self.gamestate = 0
                flag = 1
            elif (event.type == KEYDOWN and event.key == K_SPACE) or (event.type == MOUSEBUTTONDOWN and self.pause.checkIfHover(pygame.mouse.get_pos())):
                self.gamestate *= -1
                flag = 1
            elif (event.type == KEYDOWN and (event.key == K_w or event.key == K_UP)):
                self.board.block.rotate()
                flag = 1
            elif (event.type == KEYDOWN and (event.key == K_s or event.key == K_DOWN)):
                self.board.block.moveDown()
                flag = 1
            elif (event.type == KEYDOWN and (event.key == K_d or event.key == K_RIGHT)):
                self.board.block.move(1, 0)
                flag = 1
            elif (event.type == KEYDOWN and (event.key == K_a or event.key == K_LEFT)):
                self.board.block.move(-1, 0)
                flag = 1
            elif event.type == MOUSEMOTION:  # check if buttons are howered
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
                flag = 1
        self.board.actualize(self.board.check())  # actualization of the game (check if any rows are full)
        return flag
                          
if __name__ == '__main__':
    Game()
