print("+ = "+__name__)
from Client.components.box import Box
from Client.components.text import Text


class PopUpMessage:
    def __init__(self, info):
        self.info = info
        # info = ([pyga, self.positions, self.images, data])
        self.W = info[0].W
        self.H = info[0].H

        self.time = 0
        self.msg = ""
        self.pos_start = -40
        self.pos = self.pos_start

    def render(self):
        temp = self.info[0].clock.get_time()
        if self.time > 0:
            self.calculate()
            self.draw()
            self.time -= temp

    def add(self, msg, x):
        if self.time <= 0:
            self.reset()
            self.time = x*1000
            self.msg = msg

    def draw(self):
        pos = (self.W*0.28000,  (self.H*0.0)+self.pos, self.W*0.48833,  self.H*0.08000)
        Box(self.info, pos, 200).render()
        Text(self.info, self.msg, pos, 24).render()

    def calculate(self):
        if self.pos<20:
            self.pos +=1

    def reset(self):
        self.pos = self.pos_start

    def remove(self):
        self.time = 0


print("- = "+__name__)

