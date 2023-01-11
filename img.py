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


# pg.init()
# screen = pg.display.set_mode((200, 200))
# m = Image('images/1.jpeg')

# while True:
#     screen.blit(m.img, (10,10))
#     for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 sys.exit()
#     pg.display.update()


