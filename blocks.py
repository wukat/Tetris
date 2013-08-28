'''
Created on 27 sie 2013

@author: wukat
'''

from consts import size, margin, GREEN, WHITE, NCOLS, NROWS, FAIR_GREEN, GREY, \
    roundcolor
import pygame

class SingleBlock():
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        
    def draw(self, x, y):
        pygame.draw.rect(self.surface, self.color, [x * size + margin - 1, y * size, size - 1, size - 1], 0)
        pygame.draw.rect(self.surface, roundcolor, [x * size + margin - 1, y * size, size - 1, size - 1], 2)
        
class Block():
    def __init__(self, board, board_show):
        self.fields = [[], [], [], []]
        self.state = 0
        self.board = board
        self.board_show = board_show
        
    def checkIfLays(self):
        flag = False
        for i in self.fields:
            if i[0] >= 0 and i[1] >= 0:
                if self.board[i[0]][i[1] + 1]:
                    flag = True
        return flag
    
    def moveDown(self):
        if not self.checkIfLays():
            for i in self.fields:
                i[1] += 1
    
    def move(self, x, y):
        flag = False
        for i in self.fields:
            if i[0] + x >= -1 and i[0] + x <= NCOLS + 1 and i[1] + y >= 0:
                if self.board[i[0] + x][i[1] + y]:
                    flag = True
        if not flag:
            for i in self.fields:
                i[0] += x
                i[1] += y
                
    def canRotate(self):
        pass
             
    def rotate(self):
        pass
       
    def draw(self, color):
        for i in self.fields:
            if i[0] >= 0 and i[1] >= 0:
                self.board_show[i[0]][i[1]].color = color
                self.board_show[i[0]][i[1]].draw(i[0], i[1])
        pygame.display.flip()
        return self.board_show
    
class LongBlock(Block):
    def __init__(self, board, board_show):
        Block.__init__(self, board, board_show)
        self.fields = [[NCOLS/2, -3], [NCOLS/2, -2], [NCOLS/2, -1], [NCOLS/2, 0]]
        self.color = FAIR_GREEN
        
    def cantRotate(self):
        if self.state == 0:
            if self.fields[1][0] >= 0 and self.fields[1][0] <= NCOLS - 2 and self.fields[1][1] >= 0:
                return self.board[self.fields[1][0] - 1][self.fields[1][1]] + self.board[self.fields[1][0] + 1][self.fields[1][1]] + self.board[self.fields[1][0] + 2][self.fields[1][1]]
            else: 
                return True
        else:
            if self.fields[1][1] >= 0 and self.fields[1][1] <= NROWS - 2:
                return self.board[self.fields[1][0]][self.fields[1][1] - 1] + self.board[self.fields[1][0]][self.fields[1][1] + 1] + self.board[self.fields[1][0]][self.fields[1][1] + 2]    
            else:
                return True
            
    def rotate(self):
        if not self.cantRotate():
            if self.state == 0:
                self.fields = [[self.fields[1][0] - 1, self.fields[1][1]], [self.fields[1][0], self.fields[1][1]], [self.fields[1][0] + 1, self.fields[1][1]], [self.fields[1][0] + 2, self.fields[1][1]]]
                self.state = 1
            elif self.state == 1:
                self.fields = [[self.fields[1][0], self.fields[1][1] - 1], [self.fields[1][0], self.fields[1][1]], [self.fields[1][0], self.fields[1][1] + 1], [self.fields[1][0], self.fields[1][1] + 2]]
                self.state = 0       
