'''
Created on 27 sie 2013

@author: wukat
'''

from blocks import SingleBlock
from game import BLACK, BLUE, WHITE, margin, size
import pygame

class Board():
    def __init__(self, surface):
        self.surface = surface
        self.board = {i : [SingleBlock(self.surface, BLACK) for j in range(10)] for i in range(18)}
        self.board1 = {i : [0 for j in range(10)] for i in range(18)}
        self.draw()

    def draw(self):
        self.surface.fill(BLUE)
        for i in range(19):
            pygame.draw.line(self.surface, WHITE, [margin / 2 + 1, i * size], [10 * size + margin / 2 + 1, i * size], 1)
        for i in range(11):
            pygame.draw.line(self.surface, WHITE, [i * size + margin / 2 + 2, 0], [i * size + margin / 2 + 2, 18 * size], 1)
            
        pygame.draw.line(self.surface, WHITE, [0, 18 * size + margin / 2], [10 * size + margin * 3 / 2, 18 * size + margin / 2], margin)
        pygame.draw.line(self.surface, WHITE, [margin / 2, 0], [margin / 2, 18 * size], margin)
        pygame.draw.line(self.surface, WHITE, [10 * size + margin, 0], [10 * size + margin, 18 * size], margin)
        
        for i in range(18):
            for j in range(10):
                if self.board1[i][j]:
                    self.board[i][j].draw(j, i)
        pygame.display.flip()        
            
    def check(self, rows=set(range(18))):
        temp = set()
        for i in rows:
            if sum(self.board1[i]) == 10:
                temp.add(i)
        return temp
     
    def actualize(self, rows=set()):
        for i in rows:
            pygame.draw.rect(self.surface, WHITE, [margin - 1, size * i, size * 10, size], 0)
            self.board1[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pygame.display.flip()
        for i in reversed(range(18)):
            if sum(self.board1[i]) == 0:
                for j in reversed(range(0, i)):
                    if sum(self.board1[j]) != 0:
                        self.board1[i], self.board1[j] = self.board1[j], self.board1[i]
                        self.board[i], self.board[j] = self.board[j], self.board[i]
                        break
        if rows:
            pygame.time.Clock().tick(1)
        self.draw()