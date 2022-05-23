from Client.components.room import Room
from Client.components.scrollbar import ScrollBar
from Client.components.inputstr import InputStr
from Client.components.button import Button
from Client.components.label import Label


class DisplayRooms:
    def __init__(self, info, x):

        self.info = info
        self.p = info[0].p
        self.win = info[0].win

        self.pos =  (x[0]*1.02, x[1]*1.02)
        self.size = (x[2]*0.99, x[3]*0.98)
        self.colour = (255, 255, 255, 60)

        self.rect = self.p.Rect(self.pos, self.size)
        self.surface = self.p.Surface(self.rect.size, self.p.SRCALPHA)
        # white background
        self.p.draw.rect(self.surface, self.colour, self.surface.get_rect())
        self.render_right_rect()
        self.input = InputStr(self.info, (info[0].W*0.54083,  info[0].H*0.26000, info[0].W*0.27667,  info[0].H*0.07000), "Room name", "roomlabel")
        self.comfirm_button = Button(info, (info[0].W*0.55000,  info[0].H*0.34375, info[0].W*0.25750,  info[0].H*0.06875), "Comfirm", "comfirmroomcreation", square=0)
        self.label = Label(info, "Create Room:", (info[0].W*0.68, info[0].H*0.24))
        self.rooms = []

        self.rec_pos = []
        self.room_x = self.pos[0]*1.02
        self.room_y = self.pos[1]*1.02
        self.room_ycc = 0
        self.room_height = self.size[1] * 0.09
        self.room_width = self.size[0] * 0.5
        self.room_padding = self.size[1] * 0.02
        self.q = self.how_many_fit()
        self.scrollbar_value = [0, self.q]
        self.rooms_r = []
        self.scrollbar = ScrollBar(self.p, self.win, self.pos[0] + (self.size[0] * 0.52), self.pos[1] * 1.02, 20,self.size[1] * 0.98, self.q, len(self.rooms))
        self.create_rooms(self.rooms)

    def update(self, list):
        self.rooms = []
        self.scrollbar = []
        self.rooms_r = []
        self.rooms = list
        self.input.str = ""

        self.scrollbar = ScrollBar(self.p, self.win, self.pos[0] + (self.size[0] * 0.52), self.pos[1] * 1.02, 20,self.size[1] * 0.98, self.q, len(self.rooms))
        self.create_rooms(self.rooms)

    def render_right_rect(self):
        w = self.surface.get_rect().width
        h = self.surface.get_rect().height
        self.p.draw.rect(self.surface, (120, 120, 120, 255), (w*0.57, 0, w*0.43, h))

    def render(self):
        self.win.blit(self.surface, self.rect)
        self.scrollbar_render()
        self.rooms_render()
        self.input.render()
        self.comfirm_button.render()
        self.label.render()

    def rooms_render(self):
        until = len(self.rooms)
        count = 0

        for i in range(self.scrollbar_value[0], until):
            self.button = self.rooms_r[i].render(self.rec_pos[count])
            count += 1
            if count > self.q:
                count = 0

    def scrollbar_render(self):
        if self.q < len(self.rooms_r):
            self.scrollbar.render()


    def event(self, event):
        self.scrollbar_value = self.scrollbar.event(event)
        self.input.event(event)
        self.comfirm_button.event(event)

        for i in range(self.scrollbar_value[0], len(self.rooms)):
            self.rooms_r[i].event(event)

    def how_many_fit(self):
        count = 0
        y = self.pos[1] * 1.02
        self.rec_pos.append(y)
        while True:
            if y >= self.rect.bottomleft[1]:
                break

            y += self.room_height + self.room_padding
            self.rec_pos.append(y)
            count += 1
        return count-1

    def create_rooms(self, rooms):
        for room in rooms:
            if len(self.rooms_r) == 0:
                rect = self.p.Rect((self.room_x, self.room_y), (self.room_width, self.room_height))
                self.rooms_r.append(Room(self.info, self.p, self.win, rect, room[0], room[1]))
                self.room_ycc = self.room_y
            else:
                self.room_ycc += self.room_padding + self.room_height
                rect = self.p.Rect((self.room_x, self.room_ycc), (self.room_width, self.room_height))
                self.rooms_r.append(Room(self.info, self.p, self.win, rect, room[0], room[1]))


    def getinput(self):
        return self.input.str