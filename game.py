import pygame
import numpy as np
import string
import random

from constats import *

# The main Game class
class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
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
            pygame.draw.line(self.screen, LINE_COLOR, (0, x*size[1]+MENU_HITHT), (WIDTH, x*size[1]+MENU_HITHT), LINE_DICK)
        # Vertikal lines
        for y in range(G_WIDTH+1):
            pygame.draw.line(self.screen, LINE_COLOR, (y*size[0], MENU_HITHT), (y*size[0], HEIGHT+MENU_HITHT), LINE_DICK)
    
    # def find_item(self, item):
    #     items = np.where(self.grid == item)
    #     return tuple(items[0]), tuple(items[1])
    
    def heid_items(self, old, new):
        self.heid_item(old[0], old[1])
        self.heid_item(new[0], new[1])

    def heid_item(self, col, raw):
        pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(SQR_SIZE[0]*raw + LINE_DICK//2, SQR_SIZE[1]*col + LINE_DICK//2 + MENU_HITHT, SQR_SIZE[0] - LINE_DICK, SQR_SIZE[1] - LINE_DICK))
        
    def show_item(self, raw , col):
        font = pygame.font.Font('freesansbold.ttf', 72)
        text = font.render(self.grid[raw][col], True, RED, BG_COLOR)
        textRect = text.get_rect()
        textRect.center = (SQR_SIZE[0]*col + (SQR_SIZE[0] // 2), (SQR_SIZE[1]*raw + SQR_SIZE[1]//2 +MENU_HITHT))
        self.screen.blit(text, textRect)

    def reset(self):
        self.set_grid()
        self.screen.fill(BG_COLOR)
        self.draw_grid()

# game = Game()
# print(np.shape(game.grid))
