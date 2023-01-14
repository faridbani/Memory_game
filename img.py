# Class Image hold images with properties
import pygame as pg
import sys
import re

class Image:
    def __init__(self, img, id=0) -> None:
        self.img = pg.image.load(img).convert()
        self.img = pg.transform.scale(self.img, (100, 100))
        self.rect = self.img.get_rect()
        self.id = id
