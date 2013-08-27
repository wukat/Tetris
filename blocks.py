'''
Created on 27 sie 2013

@author: wukat
'''

from game import size, margin, GREEN
import pygame

class SingleBlock():
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        
    def draw(self, x, y):
        pygame.draw.rect(self.surface, self.color, [x * size + margin - 1, y * size, size - 1, size - 1], 0)
        pygame.draw.rect(self.surface, GREEN, [x * size + margin - 1, y * size, size - 1, size - 1], 2)
        
class Block():
    def __init__(self, time):
        