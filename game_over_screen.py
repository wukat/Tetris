'''
Created on 29 sie 2013

@author: wukat
'''
from Crypto.Random import random
from button import Button
from consts import screen_size, WHITE, backgroundcolor, sentences
from start_screen import StartScreen
from text import Text
import pygame

class GameOverScreen(StartScreen):
    def __init__(self, surface):
        self.surface = surface
        self.quit = Button(self.surface, "QUIT", screen_size[0] // 2, screen_size[1] * 7/8, 30, True)
        self.start = Button(self.surface, "RESTART", screen_size[0] // 2, screen_size[1] * 6/8, 30, True)
        self.starttext = Text(self.surface, "GAME OVER", True, 50, WHITE, backgroundcolor, screen_size[0] // 2, screen_size[1] * 2/8)
        self.sadtext = Text(self.surface, random.choice(sentences), True, 30, WHITE, backgroundcolor, screen_size[0] // 2, screen_size[1] * 3/8)
        self.score = Text(self.surface, "Final score: 0", True, 30, WHITE, backgroundcolor, screen_size[0] // 2, screen_size[1] * 4/8)
        
    def show(self, score):
        StartScreen.show(self)
        self.showScore(score)
        pygame.display.update()
        
    def showScore(self, score):
        self.sadtext.changeText(random.choice(sentences))
        self.sadtext.show()
        self.score.changeText("Your final score: " + str(score))
        self.score.show()