from Client.components.select_button import SelectButton


class SelectFighter:
    def __init__(self, info):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win

        # MAIN SURFACE SIZE
        self.W = int(info[0].W*0.7)
        self.H = int(info[0].H*0.45)

        # MAIN SURFACE
        self.surface = self.p.Surface((self.W, self.H), self.p.SRCALPHA)
        rect1 = self.p.Rect(2, 2, self.W - 4, self.H - 4)
        rect2 = self.p.Rect(3, 3, self.W - 6, self.H - 6)
        self.p.draw.rect(self.surface, (0, 0, 0, 100), rect1, 0, 3)
        self.p.draw.rect(self.surface, (120, 120, 120, 50), rect2, 1, 2)

        # POS CENTER
        self.x = self.info[0].W / 2 - (self.W / 2)
        self.y = self.info[0].H * 0.25 - (self.H / 2)

        # SURFACE TO DRAW ON
        self.screen2 = self.p.Surface((self.W - (15 * 2), self.H - (15 * 2)), self.p.SRCALPHA)
        self.screen2_padding = 15
        self.screen2_h = self.screen2.get_height()
        self.screen2_w = self.screen2.get_width()

        # BUTTONS
        d = self.screen2_w / 6 - 10

        ofx = self.x + self.screen2_padding
        ofy = self.y + self.screen2_padding


        b1_info = ["Wizard",        (1, 163, 230),      ["-70 energy", "", "line",  "+30 mana"]]
        b2_info = ["Warlock",       (202, 40, 191),     ["-40 mana", "-40 energy", "line", "+20 health"]]
        b3_info = ["Fire Mage",     (255, 111, 0),      ["-10 health","", "line", "+30 mana", "+30 energy"]]
        b4_info = ["Dark Knight",   (0, 30, 56),        ["-10 health","", "line", "+50 mana"]]
        b5_info = ["Priest",        (255, 255, 255),    ["-70 energy","", "line", "+20 health"]]
        b6_info = ["Necromancer",   (135, 2, 87),       ["-50 energy","", "line", "+40 mana"]]
        self.b1 = SelectButton(info, self.screen2, (ofx, ofy), 0,        0, d, self.screen2_h, "character", b1_info)
        self.b2 = SelectButton(info, self.screen2, (ofx, ofy), (1*d)+10, 0, d, self.screen2_h, "character", b2_info)
        self.b3 = SelectButton(info, self.screen2, (ofx, ofy), (2*d)+20, 0, d, self.screen2_h, "character", b3_info)
        self.b4 = SelectButton(info, self.screen2, (ofx, ofy), (3*d)+30, 0, d, self.screen2_h, "character", b4_info)
        self.b5 = SelectButton(info, self.screen2, (ofx, ofy), (4*d)+40, 0, d, self.screen2_h, "character", b5_info)
        self.b6 = SelectButton(info, self.screen2, (ofx, ofy), (5*d)+50, 0, d, self.screen2_h, "character", b6_info)
        self.buttons = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6]
        self.clicked = None

    def render(self):
        self.surface.blit(self.screen2, (self.screen2_padding, self.screen2_padding))
        self.win.blit(self.surface, (self.x, self.y))
        self.render_buttons()

    def event(self, event):
        for b in self.buttons:
            b.event(event)

    def render_buttons(self):
        for b in self.buttons:
            b.render()

            if b.flag is True:
                b.flag = False
                self.clicked = b
            if b is self.clicked:
                b.clicked()
            else:
                b.unclick()