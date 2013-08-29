'''
Created on 27 sie 2013

@author: wukat
'''

from consts import size, margin, NCOLS, NROWS, SquareBlock
import pygame

class SingleBlock():
    def __init__(self, surface, color, color1):
        self.surface = surface
        self.color = color
        self.color1 = color1
        
    def draw(self, x, y):
        pygame.draw.rect(self.surface, self.color, [x * size + margin, y * size, size, size], 0)
        pygame.draw.rect(self.surface, self.color1, [x * size + margin - 1, y * size - 1, size, size], 2)
        
class Block():
    def __init__(self, board, board_show, specif):
        self.board = board
        self.board_show = board_show
        self.set(specif)
        
    def set(self, specif):
        self.fields = [[i for i in specif[0][j]] for j in range(4)]
        self.color = specif[1]
        self.color1 = specif[2]
        
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
        l = [1, 2, 0, 3]  # order of single blocks to be an axis of rotation
        for i in l:
            listOfFields = [[0, 0], [0, 0], [0, 0], [0, 0]]
            listOfFields[i] = self.fields[i]
            flag = True
            for j in range(4):
                if j != i:
                    x = self.fields[i][0] - self.fields[j][0]
                    y = self.fields[i][1] - self.fields[j][1]
                    listOfFields[j][0] = self.fields[i][0] + y
                    listOfFields[j][1] = self.fields[i][1] - x
                    if listOfFields[j][0] < 0 or listOfFields[j][0] > NCOLS - 1 or listOfFields[j][1] < 0 or listOfFields[j][1] > NROWS - 1:
                        flag = False    
                        break
            if flag:
                if not sum(self.board[listOfFields[k][0]][listOfFields[k][1]] for k in range(4)):
                    return listOfFields
        return False
                            
    def rotate(self):
        if not self.color == SquareBlock[1]:
            rot = self.canRotate()
            if rot:
                self.fields = rot       
       
    def draw(self):
        for i in self.fields:
            if i[0] >= 0 and i[1] >= 0:
                self.board_show[i[0]][i[1]].color = self.color
                self.board_show[i[0]][i[1]].color1 = self.color1
                self.board_show[i[0]][i[1]].draw(i[0], i[1])
        pygame.display.flip()
        return self.board_show