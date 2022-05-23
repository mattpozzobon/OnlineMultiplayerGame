print("+ = "+__name__)
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Load:
    def __init__(self, config):

        self.p = pygame
        self.p.init()
        self.p.display.set_caption('SpellCaster')
        self.programIcon = self.p.image.load('assets/icon.png')
        self.p.display.set_icon(self.programIcon)

        self.p.event.set_allowed([self.p.KEYDOWN, self.p.KEYUP, self.p.QUIT])

        self.cursor_normal = self.p.cursors.Cursor(self.p.SYSTEM_CURSOR_ARROW)
        self.cursor_text = self.p.cursors.Cursor(self.p.SYSTEM_CURSOR_IBEAM)

        # SCREEN
        self.W = config.getresolution()[0]
        self.H = config.getresolution()[1]

        self.SIZE = (self.W, self.H)
        self.FPS = 60
        self.RUN = True

        # CONFIG
        self.flags = self.p.HWSURFACE | self.p.DOUBLEBUF
        self.win = self.p.display.set_mode(self.SIZE, self.flags)
        self.clock = self.p.time.Clock()

        # FONTS
        self.FONT_SIZE = 15
        self.COMICSAN =     self.p.font.SysFont('Comic Sans MS', self.FONT_SIZE)
        self.JETMONO =      self.p.font.Font('assets/fonts/jetMono.ttf', self.FONT_SIZE)
        self.ARCADE =       self.p.font.Font('assets/fonts/arcade.ttf', self.FONT_SIZE)


print("- = "+__name__)