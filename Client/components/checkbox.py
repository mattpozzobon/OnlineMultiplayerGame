print("+ = "+__name__)


class CheckBox(object):
    def __init__(self, info, x):
        # info = ([pyga, self.positions, self.images, data])
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]
        self.data = info[3]

        self.status =       self.data.check
        self.pos =          (x[0], x[1])
        self.size =         (x[2], x[3])
        self.box =          self.p.transform.scale(self.img.img_check_blank, self.size)
        self.inner_box =    self.p.transform.scale(self.img.img_check_inner, self.size)

    def render(self):
        self.fbutton()

    def f_status(self):
        return self.status

    def event(self, event):
        if event.type == self.p.MOUSEBUTTONUP:
            mouse = self.p.mouse.get_pos()
            if self.pos[0] <= mouse[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse[1] <= self.pos[1] + self.size[1]:
                if self.status == False:
                    self.data.check = True
                    self.status = True
                else:
                    self.data.check = False
                    self.status = False

    def fbutton(self):
        self.win.blit(self.box, self.pos)
        if self.status:
            self.win.blit(self.inner_box, self.pos)


print("+ = "+__name__)