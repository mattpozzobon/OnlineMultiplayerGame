
class Counter:
    def __init__(self, info):
        self.p = info[0].p
        self.win = info[0].win
        self.W = info[0].W
        self.H = info[0].H

        self.JETMONO = self.p.font.Font('assets/fonts/ARCADEPI.ttf', 30)
        self.txt = None
        self.round = False
        self.round_number = 0

        self.round_pos = (self.W/ 2+5, self.H * 0.02 + 5)
        self.counter_pos = (self.W/2+5, self.H * 0.06+5)

    def render(self, txt):
        self.txt = str(txt)
        if self.txt == "0":
            self.txt = ""

        if self.round:
            self.draw(str(self.round_number), self.round_pos)

        self.draw(str(self.txt), self.counter_pos)

    def set_round(self, number):
        self.round = True
        self.round_number = number

    def draw(self, str, pos):
        txt = self.JETMONO.render(str, True, (0, 0, 0))
        text = self.JETMONO.render(str, True, (255, 255, 0))

        for i in range(-2, 3):
            for j in range(-2, 3):
                textbox = txt.get_rect(center=(pos[0] + i, pos[1] + j))
                self.win.blit(txt, textbox)

        textbox = text.get_rect(center=pos)
        self.win.blit(text, textbox)


