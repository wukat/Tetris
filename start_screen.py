'''
Created on 28 sie 2013

@author: wukat
'''
from button import Button
from consts import backgroundcolor, screen_size, size, NROWS, WHITE
from pygame.locals import *
from text import Text
import pygame

class StartScreen():
    def __init__(self, surface):
        self.surface = surface
        self.position = (screen_size[0]//2 - 70, screen_size[1] - 0.8 * NROWS * size)
        self.start = Button(self.surface, "START", self.position[0] + 30, self.position[1] + 100, 30)
        self.quit = Button(self.surface, "QUIT", self.position[0] + 38, self.position[1] + 140, 30)
        self.starttext = Text(self.surface, "TETRIS", 50, WHITE, backgroundcolor, self.position[0], self.position[1])
        self.show()
        
    def show(self):
        self.surface.fill(backgroundcolor)
        self.starttext.show()
        self.start.draw()
        self.quit.draw()
        pygame.display.update()
        
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return 0
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.start.checkIfHover((x, y)):
                        return 1
                    if self.quit.checkIfHover((x, y)):
                        return 0
                elif event.type == MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    if self.start.checkIfHover((x, y)):
                        self.start.hover = 1
                    else:
                        self.start.hover = 0
                    self.start.drawBorder()
                    if self.quit.checkIfHover((x, y)):
                        self.quit.hover = 1
                    else:
                        self.quit.hover = 0
                    self.quit.drawBorder()
                                                
    