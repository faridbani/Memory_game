import numpy as np
import pygame
import sys
from constats import *
from menu import Menu
import random
import string
from game import Game
from datetime import datetime

# init pygame and set a screen with background color
pygame.init()
screen = pygame.display.set_mode(w_size)
pygame.display.set_caption('Memory Game')
screen.fill(BG_COLOR)

font = pygame.font.SysFont("Arial", 20)
     
# The man function to start the game
def main():
    clock = pygame.time.Clock()
    game = Game(screen)
    game.draw_grid()
    game.laod_images()
    old_item = None
    start = datetime.now()
    while True:
        menu = Menu()
        screen.blit(menu.surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos #pygame.mouse.get_pos()
                if pos[1] > MENU_HITHT:
                    raw, col = (pos[1] - MENU_HITHT) // SQR_SIZE[1], pos[0] // SQR_SIZE[0]
                    choosed_item = (raw, col)
                    if game.mode == 'alfa':
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
                    print(pos)
                    print('reset :', menu.reset.rect)
                    print('alfa :', menu.alfa.rect)
                    print('img :', menu.img.rect)
                    if menu.reset.rect.collidepoint(pos): # menu.reset.rect.left < pos[0] < menu.reset.rect.right:
                        game.reset()
                    if menu.alfa.rect.collidepoint(pos): # menu.reset.rect.left < pos[0] < menu.alfa.rect.right:
                        game.mode = 'alfa'
                        game.reset()
                    if menu.img.rect.collidepoint(pos): # menu.img.rect.left < pos[0] < menu.img.rect.right:
                        game.mode = 'img'
                        game.reset()

                
        pygame.display.update()
main()
