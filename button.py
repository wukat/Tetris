'''
Created on 28 sie 2013

@author: wukat
'''
from consts import roundbuttoncolor
import pygame

class Button():
    def __init__(self, surface, text, x, y, color):
        self.x = x
        self.y = y
        self.surface = surface
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.width, self.height = self.font.size(text) 
    
    def draw(self):
        name = self.font.render(self.text, 1, (255,255,255), self.color)
        self.surface.blit(name, (self.x, self.y))     
        pygame.draw.rect(self.surface, roundbuttoncolor, [self.x - 3, self.y - 3, self.width + 7, self.height + 4], 2)
        pygame.display.update()
        
    def checkIfPushed(self, mouse_pos):
        return mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.width and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.height
        