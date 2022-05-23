
class Aura:
    def __init__(self, info, rect):
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]

        # RUNNING
        self.rect = rect
        self.sprites = self.img.auras
        self.current_sprite = 0
        self.action = None
        self.image = None
        self.flag = True
        self.run = True

    def render(self, rect):
        if self.action is not None and self.run:
            self.rect = rect
            self.update()
            self.draw()
            self.current_sprite += 0.2

    def start(self, a):
        self.current_sprite = 0
        self.flag = True
        self.run = True
        self.action = a

    def update(self):
        self.actions()
        img = self.sprites.get(self.action)[int(self.current_sprite)]
        self.image = img

    def actions(self):
        if self.action == "Defense":
            if self.current_sprite >= len(self.sprites.get(self.action)):
                self.current_sprite = 0
                if self.flag is False:
                    self.run = False
                    self.flag = True

        if self.action == "Charge":
            if self.current_sprite >= len(self.sprites.get(self.action)):
                self.current_sprite = 0
                if self.flag is False:
                    self.run = False
                    self.flag = True

        if self.action == "Change_element":
            if self.current_sprite >= len(self.sprites.get(self.action)):
                self.current_sprite = 0
                self.run = False
                self.flag = True

        if self.action == "Special":
            if self.current_sprite >= len(self.sprites.get(self.action)):
                self.current_sprite = 0
                self.run = False
                self.flag = True

        if self.action == "Fail":
            if self.current_sprite >= len(self.sprites.get(self.action)):
                self.current_sprite = 0
                self.run = False
                self.flag = True

    def draw(self):
        rect = self.image.get_rect()
        rect.center = self.rect.center
        if self.run:
            self.win.blit(self.image, rect)