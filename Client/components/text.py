print("+ = "+__name__)


class Text:
    def __init__(self, info, text, pos, size):
        # info = ([pyga, self.positions, self.images, data])
        self.p =        info[0].p
        self.win =      info[0].win
        self.JETMONO = self.p.font.Font('assets/fonts/jetMono.ttf', size)
        self.t = text
        self.pos = pos
        self.font_size = size
        self.text = self.resize(size)
        self.text_pos = self.rect_center()

    def render(self, *args):
        self.render_on_the_go(args)
        self.win.blit(self.text, self.text_pos)

    def rect_center(self):
        px = self.pos[0] + (self.pos[2] / 2)
        py = self.pos[1] + (self.pos[3] / 2)
        pxx = self.text.get_width() / 2
        pyy = self.text.get_height() / 2
        return px-pxx, py-pyy


    def resize(self, size):
        text = self.JETMONO.render(self.t, True, (255, 255, 255))
        text_size = text.get_size()

        if size < 1:
            self.font_size = 1
            return text
        if int(text_size[0]) > int(self.pos[2]):
            return self.resize(size - 1)
        else:
            self.font_size = size
            return text

    def render_on_the_go(self, args):
        if args:
            for arg in args:
                self.text = self.JETMONO.render(str(arg), True, (255, 255, 255))


print("- = "+__name__)