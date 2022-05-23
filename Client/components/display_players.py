from Client.components.player import Player
from Client.components.scrollbar import ScrollBar

class DisplayPlayers:
    def __init__(self, info, x):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win
        self.pos = (x[0] * 1.005, x[1] * 1.03)
        self.size = (x[2] * 1, x[3] * 1)
        self.rect = self.p.Rect((self.pos[0], self.pos[1]), self.size)
        self.surface = self.p.Surface(self.rect.size, self.p.SRCALPHA)

        self.q = self.how_many_fit()
        self.c = 0

        self.players_final = []
        self.scrollbar = self.createscrollbar()
        self.scrollbar_value = 0


    def render(self):
        self.rect = self.p.Rect((self.pos[0], self.pos[1]), self.size)
        self.surface = self.p.Surface(self.rect.size, self.p.SRCALPHA)

        for player in self.players_final:
            player.render(self.surface, self.c)

        if len(self.players_final) > self.q:
            self.scrollbar.render()

        self.win.blit(self.surface, self.rect)

    def update(self, players):
        self.players_final = []
        y = 35
        y_distance = 60
        y_padding = 20
        for player in players:
            self.players_final.append(Player(self.info, y, player[0], player[1], player[2]))
            y += y_distance + y_padding

        self.scrollbar = self.createscrollbar()


    def event(self, event):
        self.scrollbar_value = self.scrollbar.event(event)
        self.c = -((self.scrollbar_value[0])*(20+60))


    def how_many_fit(self):
        h = self.surface.get_height()-30
        return round(h/(20+60))

    def createscrollbar(self):
        x = self.pos[0]+(self.size[0]*0.90)
        y = self.pos[1]+(self.size[1]*0.05)
        w = self.size[0]*0.05
        h = self.size[1]-(self.size[1]*0.07)
        return ScrollBar(self.p, self.win, x, y, w, h, self.q, len(self.players_final))