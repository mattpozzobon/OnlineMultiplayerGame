
class DisplayHands:
    def __init__(self, info):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]

        # [1]-1 Closed
        # [2]-1 Open
        # [3]-1 Finger
        self.left_hand = self.img.hands["Left"][0]
        self.right_hand = self.img.hands["Right"][0]

    def render(self):
        self.surface = self.p.Surface((self.left_hand.get_rect().w * 2 + 20, self.left_hand.get_rect().h), self.p.SRCALPHA)
        self.rect1 = self.surface.get_rect(center=(self.info[0].W / 2, self.info[0].H / 2))
        self.surface.blit(self.left_hand, (0, 0))
        self.surface.blit(self.right_hand, (self.left_hand.get_rect().w, 0))
        self.win.blit(self.surface, self.rect1)

    def set(self, hand, action):
        x = 0

        if action == "Open":
            x = 1
        if action == "Close":
            x = 0
        if action == "Pointer":
            x = 2

        if hand == "Left":
            self.left_hand = self.img.hands["Left"][x]
        if hand == "Right":
            self.right_hand = self.img.hands["Right"][x]

