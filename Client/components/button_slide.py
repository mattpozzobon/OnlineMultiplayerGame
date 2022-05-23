print("+ = "+__name__)
from pygame import gfxdraw

class ButtonSlide(object):
    def __init__(self, info, x, text, id, img):
        # info = ([pyga, self.positions, self.images, data, conn])
        self.p =    info[0].p
        self.win =  info[0].win
        self.pos =  (x[0], x[1])
        self.size = (x[2], x[3])
        self.c = info[4]

        self.id = id
        self.x_start =  0
        self.x_max =    100
        self.x_curr =   0
        self.flag = None

        self.m_colour = (255, 255, 255, 160)
        self.status = 1
        self.ARCADE = info[0].JETMONO
        self.imgg = self.ARCADE.render(text, True, (0, 0, 0))
        self.rect = 0
        self.img = img

    def render(self):
        self.render_rects()
        self.move_forward()
        self.hover()
        self.render_img()
        self.render_txt()


    def event(self, event):
        if event.type == self.p.MOUSEBUTTONUP:
            x, y = self.p.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.click()

    def click(self):
        self.status *= -1
        self.c.CLIENTMSG([self.id])
        if self.status == 1:
            self.m_colour = (255, 255, 255, 160)
        else:
            self.m_colour = (255, 255, 255, 80)


    def render_rects(self):
        rect_b = self.p.Rect(0, self.pos[1], self.size[0] + self.x_curr, self.size[1])
        s2 = self.p.Surface(rect_b.size, self.p.SRCALPHA)
        self.rect = rect_b
        self.p.draw.rect(s2, self.m_colour, s2.get_rect(), border_bottom_right_radius=50,border_top_right_radius=50)
        self.win.blit(s2, rect_b)

    def render_txt(self):
        if self.x_curr >= self.x_max:
            txt_rect = self.imgg.get_rect()
            txt_rect.centerx = self.rect.centerx - (txt_rect.width/2)
            txt_rect.centery = self.rect.centery
            self.win.blit(self.imgg, txt_rect)

    def render_img(self):
        img_rect = self.img.get_rect()
        img_rect.centerx = (img_rect.width/2)+self.x_curr+5
        img_rect.centery = self.rect.centery
        self.win.blit(self.img, img_rect)


    def hover(self):
        x, y = self.p.mouse.get_pos()
        self.flag = False
        if self.rect.collidepoint(x, y):
            self.flag = True


    def move_forward(self):
        if self.flag:
            if self.x_curr <= self.x_max:
                self.x_curr += 4
        if not self.flag:
            if self.x_curr >= self.x_start:
                self.x_curr -= 4


print("- = "+__name__)