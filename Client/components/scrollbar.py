
class ScrollBar:
    def __init__(self, p, win, x, y, w, h, q, total):
        self.p = p
        self.win = win
        self.h = h
        self.q = q
        self.total = total

        self.x = x
        self.y=y

        self.flag = None
        self.mouse_drag_pos = 0

        self.value = [0, q]
        self.bar_rect = self.p.Rect(x, y, w, h)
        self.y_offset = self.bar_rect.y
        self.slider = self.p.Rect(0, 0, 0, 0)

    def render(self):
        try:
            self.slider = self.p.Rect(self.bar_rect.x, self.y_offset, self.bar_rect.width, self.q*(self.h/self.total))
            self.p.draw.rect(self.win, (125, 125, 125), self.bar_rect)
            self.p.draw.rect(self.win, (85, 85, 85), self.slider)
        except:
            pass

    def calculate(self, q, total):
        try:
            y = int(abs(self.y-(self.slider.y+q*(self.h/total)))/self.h*total)
            x = y-q

            if x < 0:
                return [0, q]
            if y > total:
                return [total-q, total]

            return [x, y]
        except:
            pass

    def event(self, event):
        x, y = self.p.mouse.get_pos()
        if event.type == self.p.MOUSEBUTTONDOWN:
            if self.slider.collidepoint(event.pos):
                self.flag = False
                self.mouse_drag_pos = event.pos[1]

            elif self.bar_rect.collidepoint(event.pos) and self.flag:
                if y < self.slider.centery:
                    self.y_offset = y
                if y > self.slider.centery:
                    self.y_offset = y - self.slider.h
                self.value = self.calculate(self.q, self.total)

        elif event.type == self.p.MOUSEBUTTONUP:
            self.flag = True


        elif event.type == self.p.MOUSEMOTION and self.flag == False:
            diff = self.mouse_drag_pos - event.pos[1]
            self.mouse_drag_pos = event.pos[1]
            self.y_offset -= diff

            if self.y_offset <= self.y:
                self.y_offset = self.y

            if self.y_offset+self.slider.height >= self.y + self.h:
                self.y_offset = self.y + self.h - self.slider.height
            self.value =  self.calculate(self.q, self.total)
        return self.value





