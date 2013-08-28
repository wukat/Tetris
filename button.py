'''
Created on 28 sie 2013

@author: wukat
'''
from consts import roundbuttoncolor, backgroundcolor
import pygame

class Button():
    def __init__(self, surface, text, x, y, fontSize):
        self.x = x
        self.y = y
        self.surface = surface
        self.text = text
        self.font = pygame.font.Font(None, fontSize)
        self.width, self.height = self.font.size(text) 
        self.hover = 0
    
    def draw(self):
        name = self.font.render(self.text, 1, (255,255,255), backgroundcolor)
        self.surface.blit(name, (self.x, self.y))     
        self.drawBorder()
        pygame.display.update()
        
    def checkIfHover(self, mouse_pos):
        return mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.width and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.height
        
    def drawBorder(self):
        if self.hover:
            pygame.draw.rect(self.surface, roundbuttoncolor, [self.x - 5, self.y - 5, self.width + 12, self.height + 9], 3)
        else:
            pygame.draw.rect(self.surface, backgroundcolor, [self.x - 5, self.y - 5, self.width + 12, self.height + 9], 3)
            pygame.draw.rect(self.surface, roundbuttoncolor, [self.x - 3, self.y - 3, self.width + 7, self.height + 4], 2)
        pygame.display.flip()