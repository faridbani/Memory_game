import numpy as np
import pygame
import sys
from constats import *
import random
import string
from game import Game
from datetime import datetime

# init pygame and set a screen with background color
pygame.init()
screen = pygame.display.set_mode(w_size)
pygame.display.set_caption('Memory Game')
screen.fill(BG_COLOR)
m_screen = pygame.Surface((WIDTH, MENU_HITHT))
m_screen.fill(BG_COLOR)

font = pygame.font.SysFont("Arial", 20)

class Button:
    def __init__(self, text) -> None:
        self.text = font.render(text, 1, LINE_COLOR, BG_COLOR)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
    
    def show(self):
        self.surface.blit(self.text, (0, 0))
        m_screen.blit(self.surface, (10, 10))
        
# The man function to start the game
def main():
    clock = pygame.time.Clock()
    game = Game(screen)
    game.draw_grid()
    reset_button = Button("Reset")
    game.laod_images()
    old_item = None
    start = datetime.now()
    while True:
        screen.blit(m_screen, (0, 0))
        reset_button.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] > MENU_HITHT:
                    raw, col = (pos[1] - MENU_HITHT) // SQR_SIZE[1], pos[0] // SQR_SIZE[0]
                    choosed_item = (raw, col)
                    if game.mode == 'alf':
                        choosen_value = (game.grid[raw, col])
                    elif game.mode == 'img':
                        choosen_value = (game.grid[raw, col]).id
                    game.show_item(raw, col)
                    pygame.display.update()
                    if old_item == None:
                        old_item = choosed_item
                        old_value = choosen_value
                    else:
                        if old_value == choosen_value:
                            game.ocopate_grid[choosed_item] = 1
                            game.ocopate_grid[old_item] = 1
                            if game.completed():
                                end = datetime.now()
                                res = end - start
                                game.show_Comp(res)
                        else:
                            pygame.time.wait(1000)
                            game.heid_items(old_item, choosed_item)
                        old_item = None
                else:
                    if 10 < pos[0] < reset_button.size[0]:
                        game.reset()

                
        pygame.display.update()
main()
