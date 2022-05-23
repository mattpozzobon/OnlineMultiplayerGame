print("+ = "+__name__)


class Box(object):
    def __init__(self, info, rect, x, **args):
        # info = ([pyga, self.positions, self.images, data])
        self.p = info[0].p
        self.win = info[0].win

        self.border_round = 25
        self.r = rect
        self.c = (0, 0, 0, x),
        self.shape_surf = self.p.Surface(self.p.Rect(rect).size, self.p.SRCALPHA)
        self.get_arg(args)
        self.p.draw.rect(self.shape_surf, self.c, self.shape_surf.get_rect(), 0,  self.border_round)

    def render(self):
        self.win.blit(self.shape_surf, self.r)

    def get_arg(self, args):
        for arg, value in args.items():
            if arg == "border_round":
                self.border_round = value
            if arg == "colour":
                self.c = value



print("- = "+__name__)