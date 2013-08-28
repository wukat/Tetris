'''
Created on 28 sie 2013

@author: wukat
'''
from button import Button
from consts import backgroundcolor, screen_size, size, NROWS
import pygame
from pygame.locals import *

class StartScreen():
    def __init__(self, surface):
        self.surface = surface
        self.position = (screen_size[0]//2 - 70, screen_size[1] - 0.8 * NROWS * size)
        self.start = Button(self.surface, "START", self.position[0] + 30, self.position[1] + 100, backgroundcolor)
        self.quit = Button(self.surface, "QUIT", self.position[0] + 38, self.position[1] + 140, backgroundcolor)
        self.show()
        
    def show(self):
        self.surface.fill(backgroundcolor)
        font = pygame.font.Font(None, 50)
        name = font.render("TETRIS", 1, (255,255,255), backgroundcolor)
        self.surface.blit(name, self.position)
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
                    if self.start.checkIfPushed((x, y)):
                        return 1
                    if self.quit.checkIfPushed((x, y)):
                        return 0
                                                
    