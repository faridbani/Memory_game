# Class Image hold images with properties
import pygame as pg
import sys
import re

class Image:
    def __init__(self, img) -> None:
        self.img = pg.image.load(img).convert()
        self.img = pg.transform.scale(self.img, (100, 100))
        #py.Surface.convert(self.img)
        #self.id = img
        self.id = int(re.search(r'\d+', img)[0])




