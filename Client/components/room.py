from Client.components.button import Button

class Room:
    def __init__(self, info, p, win, rect, owner, label):
        self.info = info
        self.win = win
        self.p = p
        self.c = info[4]

        self.owner = owner
        self.label = label
        self.rect = rect
        self.y = rect.y
        self.join_button = Button(info, (rect.x, rect.y, info[0].W * 0.03917, info[0].H * 0.02375), "Join", ["joinroom", self.owner], square=0)

        self.myfont = self.p.font.SysFont('Comic Sans MS', 15)
        self.colour = (100, 100, 100, 250)
        self.text = self.myfont.render(self.label, True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (rect.center[0], rect.center[1])


    def render(self, x):
        self.rect.y = x
        self.textRect.y = x
        self.text = self.myfont.render(self.label, True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = ( self.rect.center[0],  self.rect.center[1])
        self.p.draw.rect(self.win, self.colour, self.rect)
        self.win.blit(self.text, self.textRect)
        self.join_button.render()

    def fhover(self):
        x, y = self.p.mouse.get_pos()
        self.colour = (100, 100, 100, 250)
        if self.rect.collidepoint(x, y):
            self.colour = (150, 150, 150, 250)

    def event(self, event):
        self.join_button.event(event)
        if event.type == self.p.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.c.CLIENTMSG(["joinroom", self.owner])
