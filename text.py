'''
Created on 29 sie 2013

@author: wukat
'''
from consts import WHITE, backgroundcolor
import pygame

class Text():
    def __init__(self, surface, text, size = 20, color = WHITE, bcolor = backgroundcolor, x = 0, y = 0):
        self.surface = surface
        self.size = size
        self.font = pygame.font.Font(None, self.size)
        self.color = color
        self.backgroundcolor = bcolor
        self.x = x
        self.y = y
        self.text = text
    
    def setSize(self, size):
        self.size = size
        self.font = pygame.font.Font(None, self.size)
    
    def setColors(self, color, bcolor):
        self.color = color
        self.backgroundcolor = bcolor
    
    def setXY(self, x, y):
        self.x = x
        self.y = y
        
    def changeText(self, text):
        self.text = text
        
    def dimensions(self):
        return self.font.size(self.text) 
        
    def show(self):
        self.surface.blit(self.font.render(self.text, 1, self.color, self.backgroundcolor), (self.x, self.y))
        
    
        