
class Background:
    def __init__(self, info):
        # ([pyga, self.positions, self.images, data])
        self.p      = info[0].p
        self.size   = info[0].SIZE
        self.W      = info[0].W
        self.H      = info[0].H
        self.img    = info[2]
        self.win    = info[0].win

        self.pic1 = self.p.transform.scale(self.img.img_pic1, self.size)
        self.pic2 = self.p.transform.scale(self.img.img_pic2, self.size)
        self.pic3 = self.p.transform.scale(self.img.img_pic3, self.size)
        self.pic4 = self.p.transform.scale(self.img.img_pic4, self.size)

        self.bg1 = 0
        self.bg2 = 0
        self.bg3 = 0
        self.bg4 = 0
        self.bg5 = 0

    def render(self):
        self.bg1 -= 0.5
        self.bg2 -= 0.2
        self.bg3 += 0.2
        self.bg4 -= 0.2

        self.win.blit(self.pic1, (self.bg1, 0))
        self.win.blit(self.pic1, (self.bg1 +self.W, 0))
        if self.bg1 <= -self.W:
            self.win.blit(self.pic1, (self.W + self.bg1, 0))
            self.bg1 = 0

        self.win.blit(self.pic2, (self.bg2, 0))
        self.win.blit(self.pic2, (self.W + self.bg2, 0))
        if self.bg2 <= -self.W:
            self.win.blit(self.pic2, (self.W + self.bg2, 0))
            self.bg2 = 0

        self.win.blit(self.pic3, (self.bg3, 0))
        self.win.blit(self.pic3, ((-self.W) + self.bg3, 0))
        if self.bg3 >= self.W:
            self.win.blit(self.pic3, ((-self.W) + self.bg3, 0))
            self.bg3 = 0

        self.win.blit(self.pic4, (self.bg4, 0))
        self.win.blit(self.pic4, (self.W + self.bg4, 0))
        if self.bg4 <= -self.W:
            self.win.blit(self.pic4, (self.W + self.bg4, 0))
            self.bg4 = 0

