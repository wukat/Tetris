'''
Created on 29 sie 2013

@author: wukat
'''
from consts import WHITE, backgroundcolor
import pygame

class Text():
    def __init__(self, surface, text, center = False, size = 20, color = WHITE, bcolor = backgroundcolor, x = 0, y = 0):
        self.surface = surface
        self.center = center
        self.size = size
        self.font = pygame.font.Font(None, self.size)
        self.color = color
        self.backgroundcolor = bcolor
        self.text = text
        self.x = x
        self.y = y
        if center:
            width, height = self.dimensions()
            self.x -= width // 2
            self.y -= height // 2
            
    def setSize(self, size):
        width, height = self.dimensions()
        self.size = size
        self.font = pygame.font.Font(None, self.size)
        if self.center:
            self.actualizeXY(width, height)
    
    def setColors(self, color, bcolor):
        self.color = color
        self.backgroundcolor = bcolor
    
    def setXY(self, x, y):
        width, height = self.dimensions()
        self.x = x
        self.y = y
        if self.center:
            self.actualizeXY(width, height)
        
    def changeText(self, text):
        width, height = self.dimensions()
        self.text = text
        if self.center:
            self.actualizeXY(width, height)
        
    def dimensions(self):
        return self.font.size(self.text) 
        
    def show(self):
        self.surface.blit(self.font.render(self.text, 1, self.color, self.backgroundcolor), (self.x, self.y))
        
    def actualizeXY(self, width, height):
        width1, height1 = self.dimensions()
        self.x += (width - width1) // 2
        self.y += (height - height1) // 2
        