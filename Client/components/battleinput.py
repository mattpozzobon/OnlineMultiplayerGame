class BattleRoomInput:
    def __init__(self, info, counter):
        self.p = info[0].p
        self.c = info[4]
        self.counter = counter

    def event(self, event):
        if self.counter.get() > 0:

            if event.type == self.p.KEYDOWN:
                if event.key == self.p.K_q:
                    self.c.CLIENTMSG(["change_element"])

                if event.key == self.p.K_w:
                    self.c.CLIENTMSG(["attack_start"])

                if event.key == self.p.K_a:
                    self.c.CLIENTMSG(["special"])

                if event.key == self.p.K_s:
                    self.c.CLIENTMSG(["Defense"])

                if event.key == self.p.K_d:
                    self.c.CLIENTMSG(["Charge"])

            if event.type == self.p.KEYUP:
                if event.key == self.p.K_w:
                    self.c.CLIENTMSG(["attack_release"])

                if event.key == self.p.K_s:
                    self.c.CLIENTMSG(["idle"])

                if event.key == self.p.K_d:
                    self.c.CLIENTMSG(["idle"])