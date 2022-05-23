from Client.components.box import Box
from Client.components.text import Text

class TabPlayersOnline:
    def __init__(self, info):
        # info = ([pyga, self.positions, self.images, data])
        pos = info[1]
        self.box =   Box(info, pos.players_online_pos, 100)
        self.text =  Text(info, "Players Online: ", pos.players_online_pos, 12)

    def render(self, txt):
        self.box.render()
        self.text.render(txt)
        # net.SERVER_STATUS

