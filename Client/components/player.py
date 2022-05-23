from Client.config.obj_images import Load

class Player:
    def __init__(self, info, y, name, wins, picture, *args):
        self.info = info
        self.p = info[0].p
        self.name = name
        self.wins = wins
        self.y = y

        self.img = info[2]
        self.avatars = Load.load_avatars(self.img)
        self.avatar = self.avatars[picture]

        self.colour = self.arguments(args)

        self.JETMONO = self.p.font.Font('assets/fonts/jetMono.ttf', 15)
        self.text = self.resize(self.name)
        self.text2 = self.JETMONO.render(str(self.wins), True, (0, 0, 0))


    def arguments(self, args):
        if "True" in args:
            return (255, 255, 0, 150)
        else:
            return (255, 255, 255, 150)


    def render(self, surface, c):
        d = surface.get_width()

        rect = self.p.Rect(d*0.2, self.y+0+c, d*0.7, 15)
        rect2 = self.p.Rect(d*0.2, self.y+15+c, d*0.7, 22)

        self.p.draw.rect(surface, self.colour,  rect)
        self.p.draw.rect(surface, self.colour, rect2)
        self.p.draw.line(surface, (0, 0, 0, 150), rect2.topleft, rect2.topright)
        self.p.draw.circle(surface, self.colour, rect.midleft, 30)
        self.p.draw.circle(surface, (120, 120, 120, 255), rect.midleft, 28)

        avatar_rect = self.avatar.get_rect()
        avatar_rect.center = rect.midleft

        surface.blit(self.avatar, avatar_rect)
        surface.blit(self.text, self.text.get_rect(midleft=(rect.midleft[0]+35, rect.midleft[1])))
        surface.blit(self.text2, self.text.get_rect(midleft=(rect2.midleft[0]+35, rect2.midleft[1])))

    def resize(self, name):
        if len(self.name) >= 12:
            return self.JETMONO.render(self.name[0:11]+"+", True, (0, 0, 0))
        return self.JETMONO.render(name, True, (0, 0, 0))



