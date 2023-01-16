# Menu on the top of game
import pygame as pg
from constats import *


class Button:
    def __init__(self, text) -> None:
        font = pg.font.SysFont("Arial", 20)
        self.text = font.render(text, 1, LINE_COLOR, MENU_GB)
        self.size = self.text.get_size()
        self.rect = self.text.get_rect()
        #self.surface = pg.Surface(self.size)
        #self.surface.blit(self.text, (0, 0))
        #self.rect = self.surface.get_rect()

class Menu:
    def __init__(self) -> None:
        self.surface = pg.Surface((WIDTH, MENU_HITHT))
        self.surface.fill(MENU_GB)
        # Make a Reset button
        self.reset = Button("Reset")
        self.reset.rect = self.surface.blit(self.reset.text, (B_LEFT, B_TOP))
        # Make a mode A-Z for choose of Uppercase mode
        self.alfa = Button("A-Z")
        alfa_w = self.reset.text.get_width() + 2 * B_LEFT
        self.alfa.rect = self.surface.blit(self.alfa.text, (alfa_w, B_TOP))
         # Make a mode Dogs for choose of imgage mode
        self.img = Button("Dogs")
        dog_w = self.reset.text.get_width() + self.alfa.text.get_width() + 3 * B_LEFT
        self.img.rect = self.surface.blit(self.img.text, (dog_w, B_TOP))