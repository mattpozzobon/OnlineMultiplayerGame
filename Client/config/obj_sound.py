
class Load:
    def __init__(self, pyga):
        p = pyga.p

        self.round_1 =          p.mixer.Sound("assets/sound/round1.mp3")
        self.round_2 =          p.mixer.Sound("assets/sound/round2.mp3")
        self.round_3 =          p.mixer.Sound("assets/sound/round3.mp3")
        self.fight =            p.mixer.Sound("assets/sound/fight.mp3")
        self.player_1_wins =    p.mixer.Sound("assets/sound/player-1-wins.mp3")
        self.player_2_wins =    p.mixer.Sound("assets/sound/player-2-wins.mp3")

    def play(self, x):
        if x == 1:
            self.round_1.play()
        if x == 2:
            self.round_2.play()
        if x == 3:
            self.round_3.play()
        if x == 4:
            self.fight.play()
        if x == "won":
            self.player_1_wins.play()
        if x == "lost":
            self.player_2_wins.play()