'''
Created on 27 sie 2013

@author: wukat
'''

from consts import size, margin, GREEN, WHITE
import pygame

class SingleBlock():
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        
    def draw(self, x, y):
        pygame.draw.rect(self.surface, self.color, [x * size + margin - 1, y * size, size - 1, size - 1], 0)
        pygame.draw.rect(self.surface, GREEN, [x * size + margin - 1, y * size, size - 1, size - 1], 2)
        
class Block():
    def __init__(self, time, board, board_show):
        self.fields = [[], [], [], []]
        self.time = time
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
        else:
            for i in self.fields:
                self.board[i[0]][i[1]] = 1
    
    def moveRight(self):
        flag = False
        for i in self.fields:
            if self.board[i[0] + 1][i[1]]:
                flag = True
        if not flag:
            for i in self.fields:
                i[0] += 1
                
    def moveLeft(self):
        flag = False
        for i in self.fields:
            if self.board[i[0] - 1][i[1]]:
                flag = True
        if not flag:
            for i in self.fields:
                i[0] -= 1
                
    def canRotate(self):
        pass
             
    def rotate(self):
        pass
       
    def draw(self):
        pass
    
class LongBlock(Block):
    def __init__(self, time, board, board_show):
        Block.__init__(self, time, board, board_show)
        self.fields = [[5, -3], [5, -2], [5, -1], [5, 0]]
        self.color = WHITE
        
    def canRotate(self):
        if self.state == 0:
            return self.board[self.fields[1][0] - 1][self.fields[1][1]] + self.board[self.fields[1][0] + 1][self.fields[1][1]] +  self.board[self.fields[1][0] + 2][self.fields[1][1]]
        else:
            return self.board[self.fields[1][0]][self.fields[1][1] - 1] + self.board[self.fields[1][0]][self.fields[1][1] + 1] +  self.board[self.fields[1][0]][self.fields[1][1] + 2]    
    
    def rotate(self):
        if self.canRotate():
            if self.state == 0:
                self.fields = [(self.fields[1][0] - 1, self.fields[1][1]), (self.fields[1][0], self.fields[1][1]), (self.fields[1][0] + 1, self.fields[1][1]), (self.fields[1][0] + 2, self.fields[1][1])]
                self.state = 1
            elif self.state == 1:
                self.fields = [(self.fields[1][0],self.fields[1][1] - 1), (self.fields[1][0],self.fields[1][1]), (self.fields[1][0],self.fields[1][1] + 1), (self.fields[1][0],self.fields[1][1] + 2)]
                self.state = 0
    
    def draw(self):
        for i in self.fields:
            if i[0] >= 0 and i[1] >= 0 and i[1] < 18:
                self.board_show[i[0]][i[1]].color = self.color
                self.board_show[i[0]][i[1]].draw(i[0], i[1])
        pygame.display.flip()
        