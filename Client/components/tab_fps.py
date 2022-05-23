from Client.components.box import Box
from Client.components.text import Text

class TabFPS:
    def __init__(self, info, pos):
        # info = ([pyga, self.positions, self.images, data])
        self.win = info[0].win
        self.p = info[0].p
        self.pos = pos

        self.surface = self.p.Surface((pos[2], pos[3]), self.p.SRCALPHA)
        self.p.draw.rect(self.surface, (255, 255, 255, 120), self.surface.get_rect(), 0, 20)

        self.green = self.p.image.load("assets/tab/fps1.png").convert_alpha()
        #self.green = self.p.transform.scale(self.green, (25, 25))
        self.yellow = self.p.image.load("assets/tab/fps2.png").convert_alpha()
        #self.yellow = self.p.transform.scale(self.yellow, (25, 25))
        self.red = self.p.image.load("assets/tab/fps3.png").convert_alpha()
        #self.red = self.p.transform.scale(self.red, (32, 25))

    def render(self, txt):
        rect = self.green.get_rect(center=self.surface.get_rect().center)
        if int(txt) >= 50:
            self.surface.blit(self.green, rect)
        elif 30 >= int(txt) <= 49:
            self.surface.blit(self.yellow, rect)
        else:
            self.surface.blit(self.red, rect)
        self.win.blit(self.surface, (self.pos[0], self.pos[1]))
