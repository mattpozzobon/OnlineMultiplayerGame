print("+ = "+__name__)


class Button(object):
    def __init__(self, info, x, text, id, **args):
        # info = ([pyga, self.positions, self.images, data, conn])
        self.info = info
        self.c = info[4]
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]

        self.rect = self.p.Rect(x[0], x[1], x[2], x[3])
        self.id = id
        self.txt = text
        self.pos = (x[0], x[1])
        self.size = (x[2], x[3])
        self.border = self.get_arg(args)

        h = self.size[1]
        w = self.size[0]

        self.button_surface = self.p.Surface((w, h), self.p.SRCALPHA)

        self.rect1 = self.p.Rect(1, 1, w-2, h-2)
        self.rect2 = self.p.Rect(2, 2, w-4, h-4)
        self.rect3 = self.p.Rect(3, 3, w-6, h-6)

        self.p.draw.rect(self.button_surface, (36, 13, 15), self.rect1, 0, 6)
        self.p.draw.rect(self.button_surface, (75, 27, 23), self.rect2, 0, 6)
        self.p.draw.rect(self.button_surface, (121, 55, 35), self.rect3, 1, 6)

        self.hover_surface = self.p.Surface((w, h), self.p.SRCALPHA)
        self.rect4 = self.p.Rect(3, 3, w-6, h-6)
        self.p.draw.rect(self.hover_surface, (255, 255, 255, 15), self.rect4, 0, 6)



    def render(self):
        self.fbutton()
        self.ftext()
        self.fhover()

    def get_arg(self, args):
        for arg, value in args.items():
            if arg == "square":
                return value
        return 50

    def fbutton(self):
        self.win.blit(self.button_surface, (self.pos[0], self.pos[1]))

    def ftext(self):
        font = self.info[0].ARCADE
        txt = font.render(self.txt, True, (0, 0, 0))
        text = font.render(self.txt, True, (255, 255, 255))
        pos = (self.pos[0] + (self.size[0] / 2), self.pos[1] + (self.size[1] / 2))

        for i in range(-2, 3):
            for j in range(-2, 3):
                textbox = txt.get_rect(center=(pos[0] + i, pos[1] + j))
                self.win.blit(txt, textbox)

        textbox = text.get_rect(center=pos)
        self.win.blit(text, textbox)


    def ready(self):
        self.p.draw.rect(self.button_surface, (255, 255, 0), self.rect3, 1, 6)

    def unready(self):
        self.p.draw.rect(self.button_surface, (121, 55, 35), self.rect3, 1, 6)

    def event(self, event):
        if event.type == self.p.MOUSEBUTTONUP:
            self.f_click()

    def fhover(self):
        x, y = self.p.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.win.blit(self.hover_surface, (self.pos[0], self.pos[1]))

    def f_click(self):
        x, y = self.p.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.c.CLIENTMSG([self.id])

print("- = "+__name__)