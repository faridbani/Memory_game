import numpy as np
import pygame
import sys
from constats import *
import random
import string

# init pygame and set a screen with background color
pygame.init()
screen = pygame.display.set_mode(w_size)
pygame.display.set_caption('Memory Game')
screen.fill(BG_COLOR)

# The main Game class
class Game:
    def __init__(self) -> None:
        self.player = 1
        self.grid = []
        # initial the grid
        self.set_grid()        
    
    # A randome choice function, return a posible squre to choose
    def rand_choice(self):
        choiced = []
        i = 0
        while i < ITEMS:
            item = random.choice(string.ascii_uppercase)
            if not item in choiced:
                choiced.append(item)
                choiced.append(item)
                i += 1
        return choiced

    # Uses Numpy to set the grid with given width and hiegt
    def set_grid(self):
        l = self.rand_choice()
        random.shuffle(l)
        self.grid = np.array(l).reshape((G_HEIGHT,G_WIDTH))

    # draws the grid on the screen
    def draw_grid(self):
        size = SQR_SIZE
        # Horizontal lines
        for x in range(G_HEIGHT+1):
            pygame.draw.line(screen, LINE_COLOR, (0, x*size[1]), (WIDTH, x*size[1]), LINE_DICK)
        # Vertikal lines
        for y in range(G_WIDTH+1):
            pygame.draw.line(screen, LINE_COLOR, (y*size[0], 0), (y*size[0], HEIGHT), LINE_DICK)
    
    # def find_item(self, item):
    #     items = np.where(self.grid == item)
    #     return tuple(items[0]), tuple(items[1])
    
    # def heid_items(self, old, new):
    #     self.heid_item(old[0], old[1])
    #     self.heid_item(new[0], new[1])

    def heid_item(self, col, raw):
        pygame.draw.rect(screen, BG_COLOR, pygame.Rect(SQR_SIZE[0]*raw + LINE_DICK//2, SQR_SIZE[1]*col + LINE_DICK//2, SQR_SIZE[0] - LINE_DICK, SQR_SIZE[0] - LINE_DICK))
        
    def show_item(self, raw , col):
        font = pygame.font.Font('freesansbold.ttf', 72)
        text = font.render(self.grid[raw][col], True, RED, BG_COLOR)
        textRect = text.get_rect()
        textRect.center = (SQR_SIZE[0]*col + (SQR_SIZE[0] // 2), (SQR_SIZE[1]*raw + SQR_SIZE[1]//2))
        screen.blit(text, textRect)
    def is_same_item(self, item):
        pass
    # def show_items(self, item):
    #     items = self.find_item(item)
    #     x1, x2 = items[0]
    #     y1, y2 = items[1]
    #     print(self.grid)
    #     print(items)
    #     print('x1:', x1,'y1:', y1)
    #     print('x2:', x2,'y2:', y2)
    #     font = pygame.font.Font('freesansbold.ttf', 72)
    #     text = font.render(self.grid[x1][y1], True, RED, BG_COLOR)
    #     textRect = text.get_rect()
    #     textRect.center = (SQR_SIZE[0]*y1 + (SQR_SIZE[0] // 2), (SQR_SIZE[1]*x1 + SQR_SIZE[1]//2))
    #     screen.blit(text, textRect)
    #     text = font.render(self.grid[x2][y2], True, RED, BG_COLOR)
    #     textRect = text.get_rect()
    #     textRect.center = (SQR_SIZE[0]*y2 + (SQR_SIZE[0] // 2), (SQR_SIZE[1]*x2 + SQR_SIZE[1]//2))
    #     screen.blit(text, textRect)
        

def main():
    clock = pygame.time.Clock()
    game = Game()
    game.draw_grid()

    old_item = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                raw, col = pos[1] // SQR_SIZE[1], pos[0] // SQR_SIZE[0]
                choosed_item = (raw, col)
                choosen_value = game.grid[raw, col]
                game.show_item(raw, col)
                pygame.display.update()
                if old_item == None:
                    old_item = choosed_item
                    old_value = choosen_value
                else:
                    if not (old_value == choosen_value):
                        pygame.time.wait(1000)
                        game.heid_items(old_item, choosed_item)
                        #pygame.display.update()
                    old_item = None
                        

                
        pygame.display.update()
main()

# game = Game()
# print(len(game.grid))

