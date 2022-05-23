from Client.components.select_button import SelectButton

class SelectElement:
    def __init__(self, info):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win

        # MAIN SURFACE SIZE
        self.W = int(info[0].W*0.7)
        self.H = int(info[0].H*0.55)

        # MAIN SURFACE
        self.surface = self.p.Surface((self.W, self.H), self.p.SRCALPHA)
        rect1 = self.p.Rect(2, 2, self.W - 4, self.H - 4)
        rect2 = self.p.Rect(3, 3, self.W - 6, self.H - 6)
        self.p.draw.rect(self.surface, (0, 0, 0, 100), rect1, 0, 3)
        self.p.draw.rect(self.surface, (120, 120, 120, 50), rect2, 1, 2)

        # POS CENTER
        self.x = self.info[0].W / 2 - (self.W / 2)
        self.y = self.info[0].H * 0.35 - (self.H / 2)

        # SURFACE TO DRAW ON
        self.screen2 = self.p.Surface((self.W - (15 * 2), self.H - (15 * 2)), self.p.SRCALPHA)
        self.screen2_padding = 15
        self.screen2_h = self.screen2.get_height()
        self.screen2_w = self.screen2.get_width()

        # BUTTONS
        d = self.screen2_w / 5 - 10

        ofx = self.x + self.screen2_padding
        ofy = self.y + self.screen2_padding

        #["-70 energy", "", "line", "+30 mana"]]
        info_b1 = ["Fire",     (207, 87, 60),
                   ["1 Fireball",
                    "2 Flaming Mouth",
                    "3 Fire Shield",
                    "4 Hell Laser",
                    "line",
                    "Speed:      [3/5]",
                    "Damage:    [3/5]",
                    "Quality:   [3/5]"]]
        info_b2 = ["Water",    (31, 126, 222),
                   ["1 Water Missile", "2 Water Ball",    "3 Waterspout",  "4 Portal", "line","Speed:   [3/5]",
                    "Damage:  [3/5]",
                    "Quality: [3/5]"]]
        info_b3 = ["Thunder",  (232, 193, 112),
                   ["1 Electric Dart", "2 Thunder Orb",   "3 Bless Shield","4 Sky Blast", "line","Speed:   [3/5]",
                    "Damage:  [3/5]",
                    "Quality: [3/5]"]]
        info_b4 = ["Earth",    (122, 72, 65),
                   ["1 Spike",         "2 Earth Saw",     "3 Meteor",      "4 Earth Golem", "line","Speed:   [3/5]",
                    "Damage:  [3/5]",
                    "Quality: [3/5]"]]
        info_b5 = ["Wind",     (168, 202, 88),
                   ["1 Wind Leaf",     "2 Boomerang",     "3 Tornado",     "4 Protection", "line","Speed:   [3/5]",
                    "Damage:  [3/5]",
                    "Quality: [3/5]"]]

        self.b1 = SelectButton(info, self.screen2, (ofx, ofy), 0,        0, d, self.screen2_h, "spell", info_b1)
        self.b2 = SelectButton(info, self.screen2, (ofx, ofy), (1*d)+10, 0, d, self.screen2_h, "spell", info_b2)
        self.b3 = SelectButton(info, self.screen2, (ofx, ofy), (2*d)+20, 0, d, self.screen2_h, "spell", info_b3)
        self.b4 = SelectButton(info, self.screen2, (ofx, ofy), (3*d)+30, 0, d, self.screen2_h, "spell", info_b4)
        self.b5 = SelectButton(info, self.screen2, (ofx, ofy), (4*d)+40, 0, d, self.screen2_h, "spell", info_b5)

        self.buttons = [self.b1, self.b2, self.b3, self.b4, self.b5]

    def render(self):
        self.render_buttons()
        self.surface.blit(self.screen2, (self.screen2_padding, self.screen2_padding))
        self.win.blit(self.surface, (self.x, self.y))

    def event(self, event):
        for b in self.buttons:
            b.event(event)

    def render_buttons(self):
        for b in self.buttons:
            b.render()

    def selected_elements(self, lista):
        for b in self.buttons:
            b.unclick()

        for b in self.buttons:
            for element in lista:
                if b.champion == element:
                    b.clicked()


