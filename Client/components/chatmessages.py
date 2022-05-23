class ChatMessages:
    def __init__(self, info, surface):
        self.p = info[0].p
        self.JETMONO = self.p.font.Font('assets/fonts/jetMono.ttf', 15)
        self.messages = []


        self.h_letter = self.JETMONO.size("H")[1]*1.20

        self.x = surface.get_width() * 0.01
        self.y = surface.get_height() * 0.02
        self.w = surface.get_width() - (surface.get_width() * 0.02)
        self.h = surface.get_height() - (surface.get_height() * 0.04)

    def addmsg(self, player, msg):
        msg = [player, msg]
        self.messages.append(msg)

    def render(self, surface):
        if len(self.messages) > 50:
            self.messages = self.messages[1:]

        count = self.h
        for msg in reversed(self.messages):
            text = self.JETMONO.render(msg[0]+": "+msg[1], True, (255, 255, 255, 255))
            count -= self.h_letter
            surface.blit(text, (self.x, self.y+count))