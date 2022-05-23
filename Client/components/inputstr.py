print("+ = "+__name__)

import re

class InputStr(object):
    def __init__(self, info, x, text, id, **args):
        # info = [pyga, self.positions, self.images, data, conn]
        self.info = info
        self.p = info[0].p
        self.win = info[0].win
        self.ARCADE = info[0].JETMONO
        self.img = info[2]
        self.data = info[3]

        self.offset_xx = 0
        self.rect = self.p.Rect(x[0], x[1], x[2], x[3])
        self.str = ""
        self.pos = (x[0], x[1])
        self.size = (x[2], x[3])
        self.label = text
        self.id = id
        self.textsurface = self.ARCADE.render(self.str, True, (255, 255, 255))
        self.x = self.pos[0] * 1.03
        self.y = self.pos[1] + (self.size[1] / 2) - (self.textsurface.get_height() / 2)
        self.img1 = self.p.transform.scale(self.img.img_input, self.size)
        self.img2 = self.p.transform.scale(self.img.img_input_focus, self.size)
        self.qt = 0
        self.flag = False
        self.fcheckinfo()
        self.colour = (110, 110, 110)
        self.counter = 500
        self.protect = False
        self.chat = False
        self.channel_number = 2
        self.get_arg(args)

    def get_arg(self, args):
        for arg, value in args.items():
            if arg == "protect":
                self.protect = value
            if arg == "offset_x":
                self.x += value
            if arg == "offset_y":
                self.offset_xx += value
            if arg == "chat":
                self.chat = value
            if arg == "channel":
                self.channel_number = value


    def render(self):
        self.finput()
        self.display()
        self.display_label()

    def render_bar(self):
        temp = self.info[0].clock.get_time()
        x = self.textsurface.get_width()
        y = self.textsurface.get_height()

        if self.counter >= 0:
            self.counter -= temp
            self.p.draw.line(self.win, (255, 255, 255), (self.x+x, self.y), (self.x+x, self.y+y))
        elif self.counter < 0:
            self.counter -= temp
            if self.counter <= -500:
                self.counter = 500


    def fcheckinfo(self):
        if self.data.check:
            if self.id == "login_nick":
                self.str = self.data.get("name")
            if self.id == "login_pass":
                self.str = self.data.get("password")

    def finput(self):
        if self.flag:
            self.win.blit(self.img1, self.pos)
            self.render_bar()
        else:
            self.win.blit(self.img2, self.pos)

    def event(self, event):
        self.write(event)
        self.clicked(event)
        self.fchat(event)


    def fchat(self, event):
        if event.type == self.p.KEYDOWN:
            if event.key == self.p.K_RETURN:
                if self.chat:
                    if len(self.str) > 0:
                        self.info[4].SERVERMSG({self.channel_number: ["msg", self.str]})
                        self.str = ""
                        self.flag = False
                    else:
                        self.flag = True




    def clicked(self, event):
        if event.type == self.p.MOUSEBUTTONUP:
            x, y = self.p.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.colour = (255, 255, 255)
                self.flag = True
            else:
                self.colour = (110, 110, 110)
                self.flag = False

    def display_label(self):
        try:
            if len(self.str) <= 0:
                txt = self.ARCADE.render(self.label, True, (110, 110, 110))
            self.win.blit(txt, (self.x, self.y))
        except:
            pass

    def display(self):
        if self.protect:
            self.textsurface = self.ARCADE.render(len(self.str)*"*", True, self.colour)
        else:
            self.textsurface = self.ARCADE.render(self.str, True, self.colour)

        if self.textsurface.get_width() > self.size[0]-(self.size[0]*0.15+self.offset_xx):
            if self.qt == 0:
                self.qt = len(self.str)

            if self.protect:
                self.textsurface = self.ARCADE.render(len(self.str[-self.qt:])*"*", True, self.colour)
            else:
                self.textsurface = self.ARCADE.render(self.str[-self.qt:], True, self.colour)


        self.win.blit(self.textsurface, (self.x, self.y))

    def write(self, event):
        if self.flag:

            if event.type == self.p.KEYDOWN:
                if event.key == self.p.K_BACKSPACE:
                    self.str = self.str[:-1]
                if event.key == self.p.K_RETURN:
                    pass
                else:
                   if self.chat:
                       self.str += str(event.unicode)
                   else:
                        if re.match("^[A-Za-z0-9_-]*$", event.unicode):
                            self.str += str(event.unicode)


print("- = "+__name__)