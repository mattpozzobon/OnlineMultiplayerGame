print("+ = "+__name__)


class CreativeMode:
    def __init__(self, info):
        # info = ([pyga, self.positions, self.images, data])
        self.p = info[0].p
        self.win = info[0].win
        self.JETMONO = info[0].JETMONO
        self.fps = 0
        self.drag = False
        self.x = 0
        self.y = 0
        self.flag = False
        self.rulerr = -1

    def event(self, event):

        if event.type == self.p.KEYUP:
            if event.key == self.p.K_1:
                self.flag = False
                self.rulerr *= -1

        if event.type == self.p.KEYDOWN:
            if event.key == self.p.K_1:
                print(self.fps)
                self.flag = True

        if event.type == self.p.MOUSEBUTTONUP:
            self.drag = False

        if event.type == self.p.MOUSEBUTTONDOWN:
            if self.drag == False:
                mouse = self.p.mouse.get_pos()
                self.x = mouse[0]
                self.y = mouse[1]
            self.drag = True


    def render(self):
        self.dragg()
        self.display()
        self.ruler()

    def dragg(self):
        if self.drag:
            mouse = self.p.mouse.get_pos()
            c1 = (mouse[0] - self.x)
            c2 = (mouse[1] - self.y)
            self.p.draw.rect(self.win, (0, 255, 0), (self.x, self.y, c1, c2), 1)
            ppx = (self.x / 1200 * 100) / 100
            ppy = (self.y / 800 * 100) / 100
            psx = (c1 / 1200 * 100) / 100
            psy = (c2 / 800 * 100) / 100
            psy = (c2 / 800 * 100) / 100

            if self.flag:
                fps = str("(W*%.5f, " % ppx + " H*%.5f, " % ppy + "W*%.5f, " % psx + " H*%.5f)" % psy)
                self.fps = fps
            sa = str(" (X*%.5f, " % ppx + " Y*%.5f, " % ppy + "W*%.5f, " % psx + " H*%.5f)" % psy)
            text_fps = self.JETMONO.render(sa, True, (0, 255, 0))
            self.win.blit(text_fps, (10, 25))


    def display(self):
        mouse = self.p.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]
        self.p.draw.line(self.win, (255, 255, 255), (x, 0), (x, 1200))
        self.p.draw.line(self.win, (255, 255, 255), (0, y), (1200, y))

        ppx = (x / 1200 * 100) / 100
        ppy = (y / 800 * 100) / 100

        fps = str("POS: W*%.3f," % ppx + " H*%.3f, " % ppy)
        text_fps = self.JETMONO.render(fps, True, (0, 255, 0))
        self.win.blit(text_fps, (10, 10))


    def ruler(self):
        if self.rulerr>0:
            for i in range(0,1201,50):
                self.p.draw.line(self.win, (255, 255, 255), (i, 0), (i, 800))
            for i in range(0, 801, 50):
                self.p.draw.line(self.win, (255, 255, 255), (0, i), (1200, i))


print("- = "+__name__)