from pygame.locals import *
import os
import pygame
import sys
 
size = 20
screen_size = [10*size + 100, 18*size + 3]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
       
                        
class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
        pygame.display.set_caption('Tetris')
        
        self.gamestate = 1  # 1 - run, 0 - exit, -1 - pause
        self.loop()
     
    def game_exit(self):
        pygame.quit()
                 
    def loop(self):
        while self.gamestate:
            for event in pygame.event.get():
                if self.gamestate == 1 and (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    self.gamestate = 0
                if (event.type == KEYDOWN and event.key == K_SPACE):
                    self.gamestate *= -1
                     
            keys = pygame.key.get_pressed()
            if keys[K_s]:
                Board(self.surface)
        self.game_exit()
         
        
class SingleBlock():
    def __init__(self, surface, color, x, y):
        self.surface = surface
        pygame.draw.rect(self.surface, color, [x * size, y * size, size, size], 0)
        pygame.draw.rect(self.surface, GREEN, [x * size, y * size, size, size], 2)
        
class Board():
    def __init__(self, surface):
        self.surface = surface
        self.board = {i : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(18)}
        self.draw()
        
        self.board[17] = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board[16] = [1, 9, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board[15] = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.draw()
        self.actualize(self.check())
        self.draw()
        
    def draw(self):
        self.surface.fill(BLUE)
        for i in range(19):
            pygame.draw.line(self.surface, WHITE, [0, i * size], [10 * size, i * size], 2)
        for i in range(11):
            pygame.draw.line(self.surface, WHITE, [i * size, 0], [i * size, 18 * size], 2)
        
        for i in range(18):
            for j in range(10):
                if self.board[i][j]:
                    SingleBlock(self.surface, BLACK, i, j)
        pygame.display.flip()        
            
    def check(self, rows = set(range(18))):
        temp = set()
        for i in rows:
            if sum(self.board[i]) == 10:
                temp.add(i)
        return temp
     
    def actualize(self, rows = set()):
        for i in rows:
            pygame.draw.rect(self.surface, WHITE, [0, size * i, size * 10, size], 0)
            self.board[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pygame.display.flip()
        for i in reversed(range(18)):
            if sum(self.board[i]) == 0:
                for j in reversed(range(0, i)):
                    if sum(self.board[j]) != 0:
                        self.board[i], self.board[j] = self.board[j], self.board[i]
                        break
        self.draw()
                
            
        


if __name__ == '__main__':
    Game()

