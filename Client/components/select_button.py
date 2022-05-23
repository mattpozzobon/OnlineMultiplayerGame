
class SelectButton(object):
    def __init__(self, info, screen, offset, x, y, w, h, type, champion):
        self.screen = screen
        self.offset = offset
        self.win = info[0].win
        self.c = info[4]
        self.p = info[0].p
        self.img = info[2]
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
        self.champion = champion[0]
        self.text = champion[2]
        self.flag = False

        self.title_colour = (127, 127, 127)
        self.body_colour = (127, 127, 127)

        self.text_colour_unclicked = (127, 127, 127)
        self.text_colour_clicked = champion[1]

        self.GREY = (127, 127, 127)
        self.WHITE = (255, 255, 255)

        self.text_to_render = champion[2]

        self.border = (121, 55, 35)
        self.image = self.get_img()
        self.rect = self.p.Rect(self.offset[0]+self.x, self.offset[1]+self.y, self.w - 2, self.h - 2)

        # MAIN BUTTON SURFACE AND HOVER
        self.button_surface = self.p.Surface((w, h), self.p.SRCALPHA)
        self.hover_surface = self.p.Surface((w, h), self.p.SRCALPHA)

        # IMAGE SURFACE
        self.image_size = w*0.8
        self.image_surface = self.p.Surface((self.image_size, self.image_size), self.p.SRCALPHA)

        # TITLE SURFACE
        self.text_w = self.button_surface.get_rect().width
        self.text_h = self.button_surface.get_rect().height
        self.title_surface = self.p.Surface((self.text_w - 20, (self.text_h) * 0.1), self.p.SRCALPHA)
        #self.title_surface.fill((160, 160, 160))

        # TEXT SURFACE
        self.text_w = self.button_surface.get_rect().width
        self.text_h = self.button_surface.get_rect().height
        self.text_surface = self.p.Surface((self.text_w-20, (self.text_h-40)/2), self.p.SRCALPHA)
        self.text_surface.fill((120, 120, 120))


        self.is_hovering = False
        self.button_surface_set()
        self.hover_surface_set()

    def get_img(self):
        if self.type == "character":
            return self.img.sprites[self.champion]["Portrait"][0]
        if self.type == "spell":
            return self.img.spells[self.champion]["Icon"][1]

    def render(self):
        self.screen.blit(self.button_surface, (self.x, self.y))
        self.line()
        self.fhover()

    def event(self, event):
        if event.type == self.p.MOUSEBUTTONUP:
            self.f_click()

    def f_click(self):
        x, y = self.p.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            if self.type == "character":
                self.c.CLIENTMSG(["character", self.champion])
                self.flag = True

            if self.type == "spell":
                self.c.CLIENTMSG(["spell", self.champion])

    def clicked(self):
        if self.type == "character":
            self.image = self.img.sprites[self.champion]["Portrait"][1]

        self.text_colour = self.text_colour_clicked
        self.border = (255, 255, 0)
        self.title_colour = self.text_colour_clicked
        self.body_colour = self.WHITE
        self.button_image_surface()
        self.button_title_surface()
        self.button_text_surface()

    def unclick(self):
        if self.type == "character":
            self.image = self.img.sprites[self.champion]["Portrait"][0]

        self.text_colour = self.text_colour_unclicked
        self.border = (121, 55, 35)
        self.title_colour = self.GREY
        self.body_colour = self.GREY
        self.button_image_surface()
        self.button_title_surface()
        self.button_text_surface()

    def fhover(self):
        x, y = self.p.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.screen.blit(self.hover_surface, (self.x, self.y))
            self.is_hovering = True
        else:
            self.is_hovering = False

    def hover_surface_set(self):
        rect3 = self.p.Rect(3, 3, self.w - 6, self.h - 6)
        self.p.draw.rect(self.hover_surface, (255, 255, 255, 15), rect3, 0, 6)

    def line(self):
        y = 10 + self.image_size + 5
        w = self.button_surface.get_rect().width
        self.p.draw.line(self.button_surface, self.border, (10, y), (w-10, y))
        self.p.draw.line(self.button_surface, self.border, (10, y-1), (w - 10, y-1))

        y = 10 + self.image_size + 10 + 20
        w = self.button_surface.get_rect().width
        self.p.draw.line(self.button_surface, self.border, (10, y), (w - 10, y))
        self.p.draw.line(self.button_surface, self.border, (10, y - 1), (w - 10, y - 1))

    def button_surface_set(self):
        rect1 = self.p.Rect(1, 1, self.w - 2, self.h - 2)
        rect2 = self.p.Rect(2, 2, self.w - 4, self.h - 4)
        rect3 = self.p.Rect(3, 3, self.w - 6, self.h - 6)
        self.p.draw.rect(self.button_surface, (36, 13, 15), rect1, 0, 6)
        self.p.draw.rect(self.button_surface, (75, 27, 23), rect2, 0, 6)
        self.p.draw.rect(self.button_surface, self.border, rect3, 1, 6)

        self.button_image_surface()
        self.button_title_surface()
        self.button_text_surface()

    def button_title_surface(self):
        ARCADE = self.p.font.Font('assets/fonts/arcade.ttf', 10)
        text = ARCADE.render(self.champion, False, self.title_colour)
        rect = text.get_rect()
        rect.center = self.title_surface.get_rect().center

        self.title_surface.blit(text, rect)

        y_offset = 10 + self.image_size
        self.button_surface.blit(self.title_surface, (10, y_offset))

    def button_image_surface(self):
        self.image_surface = self.p.Surface((self.image_size, self.image_size), self.p.SRCALPHA)
        rect = self.button_surface.get_rect()
        offset = (rect.width/2) - (self.image_size/2)

        image = self.p.transform.scale(self.image, (self.image_size, self.image_size))
        rect2 = image.get_rect()
        rect2.center = rect.center

        self.image_surface.blit(image, rect)
        self.button_surface.blit(self.image_surface, (offset, 10))

    def button_text_surface(self):
        self.text_surface = self.p.Surface((self.text_w - 20, (self.text_h / 2)), self.p.SRCALPHA)

        rect = self.text_surface.get_rect()
        offset = 10 + self.image_size + 15 + 30

        rect1 = self.p.Rect(1, 1, rect.w - 2, rect.h - 2)
        self.p.draw.rect(self.text_surface, (121, 55, 35), rect1, 0, 6)
        self.description(rect1)
        self.button_surface.blit(self.text_surface, (10, offset))

    def description(self, rect4):
        ARCADE = self.p.font.Font('assets/fonts/arcade.ttf', 12)
        if self.type == "character":
            text = ARCADE.render("SPECIAL ", False, self.body_colour)
        else:
            text = ARCADE.render("SPELLS", False, self.title_colour)
        rect = text.get_rect()
        rect.midtop = rect4.midtop
        rect.y += rect.y + 5
        self.text_surface.blit(text, rect)

        padding_x = 10
        padding_y = 30

        for i in range(len(self.text)):
            if self.text[i] == "line":
                w = self.text_surface.get_rect().width
                self.p.draw.line(self.text_surface, self.title_colour, (10, padding_y), (w - 10, padding_y))
                self.p.draw.line(self.text_surface, self.title_colour, (10, padding_y - 1), (w - 10, padding_y - 1))
                padding_y += 10
            else:
                ARCADE = self.p.font.Font('assets/fonts/arcade.ttf', 10)
                text = ARCADE.render(self.text[i], False, self.body_colour)
                self.text_surface.blit(text, (padding_x, padding_y))
                padding_y += 20
