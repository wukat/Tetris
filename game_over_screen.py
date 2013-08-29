'''
Created on 29 sie 2013

@author: wukat
'''
from button import Button
from consts import screen_size, NROWS, size, WHITE, backgroundcolor
from start_screen import StartScreen
from text import Text
import pygame

class GameOverScreen(StartScreen):
    def __init__(self, surface):
        self.surface = surface
        self.position = (screen_size[0]//2 - 70, screen_size[1] - 0.8 * NROWS * size)
        self.quit = Button(self.surface, "QUIT", self.position[0] + 38, self.position[1] + 140, 30)
        self.start = Button(self.surface, "RESTART", self.position[0] + 30, self.position[1] + 100, 30)
        self.starttext = Text(self.surface, "GAME OVER", 50, WHITE, backgroundcolor, self.position[0], self.position[1])
        self.show()