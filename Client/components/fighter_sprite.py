from Client.components.fighter_auras import Aura

class Sprite():
    def __init__(self, info, facing, rect, name):
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]

        # RUNNING
        self.facing = facing
        self.rect = rect
        self.sprites = self.img.sprites[name]
        self.current_sprite = 0
        self.action = "Idle"

        self.image = self.sprites[self.action][self.current_sprite]
        self.aura = Aura(info, self.rect)

    def render(self, rect):
        self.rect = rect
        self.update()
        self.draw()
        self.aura.render(self.rect)

    def setaction(self, action):
        if action == "special":
            self.aura.start("Special")

        elif action == "FailSpell":
            self.aura.flag = False
            self.action = "Fail"
            self.aura.start("Fail")

        elif action == "FailShieldBroke":
            self.aura.flag = False

        elif action == "FailCooldown":
            self.aura.start("Fail")

        elif action == "Defense" or action == "Charge" or action == "Change_element":
            self.aura.start(action)
        else:
            self.aura.flag = False
            self.action = action

    def actions(self):
        q = len(self.sprites[self.action])
        if self.action == "Attack_start":
            if self.current_sprite >= q:
                self.current_sprite = 2

        elif self.action == "Attack_release":
            if self.current_sprite >= q:
                self.current_sprite = 0
                self.action = "Idle"

        elif self.action == "Hurt":
            if self.current_sprite >= q:
                self.current_sprite = 0
                self.action = "Idle"

        elif self.action == "Fail":
            if self.current_sprite >= q:
                self.current_sprite = 0
                self.action = "Idle"

        elif self.action == "Death":
            if self.current_sprite >= q:
                self.current_sprite = q-1

        elif self.action == "Idle":
            if self.current_sprite >= q:
                self.current_sprite = 0

    def update(self):
        self.current_sprite += 0.2
        self.actions()
        img = self.sprites.get(self.action)[int(self.current_sprite)]
        if self.facing == "right":
            self.image = self.p.transform.flip(img, True, False)
        else:
            self.image = img

    def draw(self):
        rect = self.image.get_rect()
        rect.midbottom = self.rect.midbottom
        self.win.blit(self.image, rect)