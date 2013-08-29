'''
Created on 27 sie 2013

@author: wukat
'''

from blocks import SingleBlock, LongBlock, SquareBlock
from consts import BLACK, BLUE, WHITE, margin, size, NCOLS, NROWS, screen_size, \
    backgroundcolor
import pygame


class Board():
    def __init__(self, surface):
        self.surface = surface
        self.surface.fill(backgroundcolor)
        self.point = 0
        self.level = 1
        self.count = 0
        self.time = 1000
        self.board_show = {i : [SingleBlock(self.surface, BLACK, WHITE) for j in range(NROWS)] for i in range(NCOLS)}
        self.board = {i: [0 for j in range(NROWS + 1)] for i in range(-1, NCOLS + 1)}
        self.board[-1] = [1 for j in range(NROWS + 1)]
        self.board[NCOLS] = [1 for j in range(NROWS + 1)]
        for i in range(-1, NCOLS + 1):
            self.board[i][NROWS] = 1
        self.block = SquareBlock(self.board, self.board_show)
        self.draw()
        

    def draw(self):
        self.surface.fill(backgroundcolor, [0, 0, screen_size[0] - 110, screen_size[1]])
        for i in range(NROWS + 1):
            pygame.draw.line(self.surface, WHITE, [margin / 2 + 1, i * size], [NCOLS * size + margin / 2 + 1, i * size], 1)
        for i in range(NCOLS + 1):
            pygame.draw.line(self.surface, WHITE, [i * size + margin / 2 + 2, 0], [i * size + margin / 2 + 2, NROWS * size], 1)
            
        pygame.draw.line(self.surface, WHITE, [0, NROWS * size + margin / 2], [NCOLS * size + margin * 3 / 2, NROWS * size + margin / 2], margin)
        pygame.draw.line(self.surface, WHITE, [margin / 2, 0], [margin / 2, NROWS * size], margin)
        pygame.draw.line(self.surface, WHITE, [NCOLS * size + margin, 0], [NCOLS * size + margin, NROWS * size], margin)
        
        for i in range(NCOLS):
            for j in range(NROWS):
                if self.board[i][j]:
                    self.board_show[i][j].draw(i, j)
                    
        self.board_show = self.block.draw(self.block.color, self.block.color2)
        self.texts()
        pygame.display.update()
            
    def check(self, rows=set(range(NROWS))):
        temp = set()
        for i in rows:
            if sum(self.board[j][i] for j in range(NCOLS)) == NCOLS:
                temp.add(i)
        return temp
     
    def actualize(self, rows=set()):
        self.point += len(rows)**2 * 10 
        self.count += len(rows)
        if self.count // 10 + 1 - self.level:
            self.time *= 0.9
        self.level = self.count // 10 + 1
        for i in rows:
            pygame.draw.rect(self.surface, WHITE, [margin - 1, size * i, size * NCOLS, size], 0)
            for j in range(NCOLS):
                self.board[j][i] = 0
        pygame.display.update()
        for i in reversed(range(NROWS)):
            if sum(self.board[k][i] for k in range(NCOLS)) == 0:
                for j in reversed(range(0, i)):
                    if sum(self.board[k][j] for k in range(NCOLS)) != 0:
                        self.board = self.swapRows(i, j, self.board)
                        self.board_show = self.swapRows(i, j, self.board_show)
                        break
        if rows:
            pygame.time.wait(100)
        if self.block.checkIfLays():
            for i in self.block.fields:
                self.board[i[0]][i[1]] = 1
                self.board_show[i[0]][i[1]].color = self.block.color
            self.block = LongBlock(self.board, self.board_show)
            
    def isGameOver(self):
        for i in range(NCOLS):
            if self.board[i][0]:
                return True
        return False
    
    def swapRows(self, i, j, board):
        for k in range(NCOLS):
            board[k][i], board[k][j] = board[k][j], board[k][i]
        return board
    
    def texts(self):
        font = pygame.font.Font(None,20)
        scoretext = font.render("Score: " + str(self.point), 1, (255,255,255), backgroundcolor)
        leveltext = font.render("Level: " + str(self.level), 1, (255,255,255), backgroundcolor)
        gametext = font.render("Tetris", 1, (255,255,255), backgroundcolor)
        self.surface.blit(gametext, (NCOLS * size + 15, 10))
        self.surface.blit(scoretext, (NCOLS * size + 15, 30))
        self.surface.blit(leveltext, (NCOLS * size + 15, 50))
        
        