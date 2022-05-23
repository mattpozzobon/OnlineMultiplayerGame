from Client.components.inputstr import InputStr
from Client.components.chatmessages import ChatMessages


class Chat:
    def __init__(self, info, x, id, channel):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win
        self.id = id

        self.pos =  (x[0]*1.02, x[1]*1.01)
        self.size = (x[2]*0.99, x[3]*0.85)

        self.channel = channel
        self.input = self.create_input()
        self.rect = self.p.Rect((self.pos[0], self.pos[1]), self.size)
        self.surface = self.p.Surface(self.rect.size, self.p.SRCALPHA)
        self.chat = ChatMessages(info, self.surface)

    def render(self):
        self.rect = self.p.Rect((self.pos[0], self.pos[1]), self.size)
        self.surface = self.p.Surface(self.rect.size, self.p.SRCALPHA)
        self.p.draw.rect(self.surface, (255, 255, 255, 40), self.surface.get_rect())
        self.chat.render(self.surface)
        self.win.blit(self.surface, self.rect)
        self.input.render()

    def update(self, player, msg):
        self.chat.addmsg(player, msg)

    def event(self, event):
        self.input.event(event)

    def create_input(self):
        info = (self.info[0].W*0.15333,  self.info[0].H*0.96375, self.info[0].W*0.46750,  self.info[0].H*0.03125)
        return InputStr(self.info, info, "", self.id, offset_x=20, offset_y=-50, chat=True, channel=self.channel)