import pygame
import numpy as np
import string
import random
from img import Image

from constats import *
from glob import glob

# The main Game class
class Game:
    def __init__(self, screen) -> None:
        self.mode = "img" # modes are 'alf' for upercases or 'img' for images 
        self.screen = screen
        self.player = 1
        self.grid = []
        # initial the grid
        self.set_grid()        
    
    def laod_images(self):
        img_files = glob(IMG_PATH)
        print(img_files)
        images = []
        for i in range(1, ITEMS + 1):
            m = Image(img_files[i-1], i)
            images.append(m)
            images.append(m)
        random.shuffle(images)
        return images

    # # A randome choice function, return a posible squre to choose
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
        self.ocopate_grid = np.zeros((G_HEIGHT, G_WIDTH), np.int32)
        if self.mode == 'alf':
            l = self.rand_choice()
        elif self.mode == 'img':
            l = self.laod_images()
        else:
            print('Somthing is wrong with mode!')
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
    
    def heid_items(self, old, new):
        self.heid_item(old[0], old[1])
        self.heid_item(new[0], new[1])

    def heid_item(self, col, raw):
        pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(SQR_SIZE[0]*raw + LINE_DICK//2, SQR_SIZE[1]*col + LINE_DICK//2 + MENU_HITHT, SQR_SIZE[0] - LINE_DICK, SQR_SIZE[1] - LINE_DICK))
        
    def show_item(self, raw , col):
        if self.mode == 'alf':
            font = pygame.font.Font('freesansbold.ttf', 72)
            text = font.render(self.grid[raw][col], True, RED, BG_COLOR)
            textRect = text.get_rect()
            textRect.center = (SQR_SIZE[0]*col + (SQR_SIZE[0] // 2), (SQR_SIZE[1]*raw + SQR_SIZE[1]//2 +MENU_HITHT))
            self.screen.blit(text, textRect)
        elif self.mode == 'img':
            img = self.grid[raw][col]
            self.screen.blit(img.img, (SQR_SIZE[0]*col + LINE_DICK//2, SQR_SIZE[1]*raw + MENU_HITHT + LINE_DICK//2))
        else:
            print('Somthing is wrong with mode!')

    def show_Comp(self, res):
        m = res.seconds // 60
        s = res.seconds % 60
        font = pygame.font.SysFont("Arial", 28)
        text = font.render(f"Completed in  {m} minutes and {s} second", True, COMP_COLOR, BG_COLOR)
        t_rect = text.get_rect()
        t_rect.center = (WIDTH // 2, (HEIGHT+MENU_HITHT) // 2)
        self.screen.blit(text, t_rect)


    def reset(self):
        self.set_grid()
        self.screen.fill(BG_COLOR)
        self.draw_grid()

    def completed(self):
        for r in self.ocopate_grid:
            for c in r:
                if c == 0:
                    return False
        return True
