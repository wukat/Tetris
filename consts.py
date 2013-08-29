'''
Created on 27 sie 2013

@author: wukat
'''
NROWS = 20
NCOLS = 12 
size = 20
screen_size = [NCOLS * size + 125, NROWS * size + 3]
margin = 5


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN1 = (0, 255, 0)
RED = (204, 0, 0)
FAIR_BLUE = (51, 102, 204)
PINK = (255, 51, 102)
PURPLE = (204, 51, 153)
FAIR_GREEN = (61, 245, 0)
GREEN = (0, 184, 46)
YELLOW = (255, 204, 0)
ORANGE = (255, 102, 0)
DARK_PURPLE = (135, 31, 120)
GREY = (95, 95, 95)
DARK_BLUE = (64, 0, 245)
ELSE_BLUE = (112, 219, 255)
BROWN = (184, 46, 0)
SOME_YELLOW = (255, 204, 51)
SOME_ELSE_YELLOW = (204, 255, 51)
AND_LAST_ONE = (255, 204, 51)

backgroundcolor = FAIR_BLUE
roundbuttoncolor = ORANGE

LongBlock = ([[NCOLS / 2, -3], [NCOLS / 2, -2], [NCOLS / 2, -1], [NCOLS / 2, 0]], FAIR_GREEN, GREEN)
SquareBlock = ([[NCOLS / 2 + 1, -1], [NCOLS / 2, -1], [NCOLS / 2 + 1, 0], [NCOLS / 2, 0]], PINK, RED) 
LBlock = ([[NCOLS / 2, -2], [NCOLS / 2, -1], [NCOLS / 2, 0], [NCOLS / 2 + 1, 0]], YELLOW, ORANGE)  
revLBlock = ([[NCOLS / 2 + 1, -2], [NCOLS / 2 + 1, -1], [NCOLS / 2 + 1, 0], [NCOLS / 2, 0]], PURPLE, DARK_PURPLE)  
ZBlock = ([[NCOLS / 2 - 1, -1], [NCOLS / 2, -1], [NCOLS / 2, 0], [NCOLS / 2 + 1, 0]], BROWN, SOME_YELLOW)  
revZBlock = ([[NCOLS / 2 - 1, 0], [NCOLS / 2, 0], [NCOLS / 2, -1], [NCOLS / 2 + 1, -1]], ELSE_BLUE, DARK_BLUE)
SBlock = ([[NCOLS / 2 - 1, 0], [NCOLS / 2, 0], [NCOLS / 2 + 1, 0], [NCOLS / 2, -1]], SOME_ELSE_YELLOW, AND_LAST_ONE)

Blocks = [LongBlock, SquareBlock, LBlock, revLBlock, ZBlock, revZBlock, SBlock]
