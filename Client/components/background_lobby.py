
class BackgroundLobby:
    def __init__(self, info, n):
        # ([pyga, self.positions, self.images, data])
        self.p      = info[0].p
        self.size   = info[0].SIZE
        self.img    = info[2]
        self.win    = info[0].win

        self.n = n
        self.dict = {
            1: self.p.transform.scale(self.img.img_lobby_1, self.size),
            2: self.p.transform.scale(self.img.img_lobby_2, self.size),


            5: self.p.transform.scale(self.img.img_battle_1, self.size),
            6: self.p.transform.scale(self.img.img_battle_2, self.size),
            7: self.p.transform.scale(self.img.img_battle_3, self.size),
        }

    def render(self):

        self.win.blit(self.dict.get(self.n), (0, 0))
