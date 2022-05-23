
class Label:
    def __init__(self, info, tt, pos):
        self.p = info[0].p
        self.win = info[0].win
        self.W = info[0].W
        self.H = info[0].H

        self.JETMONO = self.p.font.Font('assets/fonts/ARCADEPI.ttf', 30)

        self.pos = pos
        self.txt = self.JETMONO.render(tt, True, (0, 0, 0))
        self.text = self.JETMONO.render(tt, True, (255, 255, 0))

    def render(self):
        self.draw()

    def draw(self):
        for i in range(-2, 3):
            for j in range(-2, 3):
                textbox = self.txt.get_rect(center=(self.pos[0] + i, self.pos[1] + j))
                self.win.blit(self.txt, textbox)

        textbox = self.text.get_rect(center=self.pos)
        self.win.blit(self.text, textbox)


