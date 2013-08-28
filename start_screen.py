'''
Created on 28 sie 2013

@author: wukat
'''
from consts import backgroundcolor, screen_size, size, NROWS
import pygame

class StartScreen():
    def __init__(self, surface):
        self.surface = surface
        self.surface.fill(backgroundcolor)
        font = pygame.font.Font(None, 50)
        name = font.render("TETRIS", 1, (255,255,255), backgroundcolor)
        self.surface.blit(name, (screen_size[0]//2 - 70, screen_size[1] - 0.8 * NROWS * size))
        pygame.display.update()
        pygame.time.wait(1000)
        
    def button_start(self, tekst):
        