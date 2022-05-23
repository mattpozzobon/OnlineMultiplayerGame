from components.player import Player

class Box2(object):
    def __init__(self, info, pos):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win

        self.x = pos[0]
        self.y = pos[1]
        self.w = pos[2]
        self.h = pos[3]


    def render(self):
        surface = self.p.Surface((self.w, self.h), self.p.SRCALPHA)
        lista = self.info[4].room_list

        y = 35
        y_distance = 60
        y_padding = 20

        for i in range(len(lista)):
            a = Player(self.info, y, lista[i][0], lista[i][1], lista[i][2])
            if len(lista[i]) > 3:
                a = Player(self.info, y, lista[i][0], lista[i][1], lista[i][2], lista[i][3])

            a.render(surface, 0)
            y += y_distance + y_padding

        self.win.blit(surface, (self.x, self.y))