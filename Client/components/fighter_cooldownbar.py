class cooldownBar:
    def __init__(self, info, x, y, h, w, dir):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win
        self.rect = self.p.Rect((x, y), (h, w))
        self.direction = dir

        self.x = self.rect.x+1
        self.y = self.rect.y+1
        self.h = self.rect.height - 2
        self.w = self.rect.width - 2

        self.original_colour = (125, 128, 128)

        self.max = 0
        self.current = 0
        self.time = 0

    def render(self):
        temp = self.info[0].clock.get_time()

        if self.time > 0:
            self.time -= temp
            if self.direction == "left":
                self.current -= temp
            if self.direction == "right":
                self.current += temp

            self.p.draw.rect(self.win, (0, 0, 0), self.rect)
            m = (self.current / self.max) * self.w
            pp = self.p.Rect((self.x, self.y), (m, self.h))
            self.p.draw.rect(self.win, self.original_colour, pp)

            if self.direction == "right":
                self.render_lines()

        if self.current > self.max:
            self.cancel()

    def render_lines(self):
        x = self.rect.x
        y = self.rect.y
        bar_width = self.rect.width
        bar_height = self.rect.height
        bar_max = self.max

        for i in range(5):
            d = (1000*i / bar_max) * bar_width + x
            self.p.draw.line(self.win, (0, 0, 0), (d, y), (d, y + bar_height-2))

    def add(self, time):
        if self.time <= 0:
            self.time = time * 1000
            self.max = self.time
            if self.direction == "left":
                self.current = self.time

    def cancel(self):
        self.max = 0
        self.current = 0
        self.time = 0
        self.time = 0