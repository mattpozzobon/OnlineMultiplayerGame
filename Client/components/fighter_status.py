class Status:
    def __init__(self, info):
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]

        # Loading and rescaling
        self.image0 = self.p.transform.scale(self.img.image0, (200, 20))
        self.image1 = self.p.transform.scale(self.img.image1, (100, 100))
        self.image2 = self.p.transform.scale(self.img.image2, (200, 20))
        self.image22 = self.p.transform.scale(self.img.image22, (200, 20))
        self.image3 = self.p.transform.scale(self.img.image3, (200, 20))
        self.image33 = self.p.transform.scale(self.img.image33, (200, 20))
        self.image4 = self.p.transform.scale(self.img.image4, (200, 20))
        self.image44 = self.p.transform.scale(self.img.image44, (200, 20))
        self.image5 = self.p.transform.scale(self.img.image5, (200, 20))

        # Size of frame + Bars
        self.W = self.image5.get_width() + self.image1.get_width()
        self.H = self.image1.get_height()

        # PORTRAITS
        self.left_p = "Black"
        self.right_p = "Black"

        # STATUS DAMAGE
        self.left_status_damage = ShowStatus(info, "left")
        self.right_status_damage = ShowStatus(info, "right")

        # LEFT SIDE
        self.surface = self.p.Surface((self.W, self.H), self.p.SRCALPHA)
        self.rect1 = self.surface.get_rect(topleft=self.pos("left", info[0].SIZE))
        self.surface.blit(self.image1, (0, 0))
        self.victory_1 = Victory(info, "left", self.rect1.bottomleft)

        # RIGHT SIDE
        self.surface2 = self.p.Surface((self.W, self.H), self.p.SRCALPHA)
        self.rect2 = self.surface2.get_rect(topright=self.pos("right", info[0].SIZE))
        self.surface2.blit(self.image1, (self.image5.get_width() - 2, 0))
        self.victory_2 = Victory(info, "right", self.rect2.bottomright)

        # BARS
        self.bar_lenght = self.image5.get_width()
        self.bar_ratio = 100 / self.bar_lenght
        self.bar_speed = 0.2

        # HEALTH
        self.left_cur_health = 100
        self.left_max_health = 100
        self.left_tar_health = 100

        self.right_cur_health = 100
        self.right_max_health = 100
        self.right_tar_health = 100

        # MANA
        self.left_cur_mana = 100
        self.left_max_mana = 100
        self.left_tar_mana = 100

        self.right_cur_mana = 100
        self.right_max_mana = 100
        self.right_tar_mana = 100

        # ENERGY
        self.left_cur_energy = 100
        self.left_max_energy = 100
        self.left_tar_energy = 100

        self.right_cur_energy = 100
        self.right_max_energy = 100
        self.right_tar_energy = 100

    def set_avatar(self, ll, pp):
        if ll is None:
            ll = "Black"

        if pp is None:
            pp = "Black"

        self.left_p = ll
        self.right_p = pp

        lp = self.img.sprites[self.left_p]["Portrait"][1]
        lp = self.p.transform.scale(lp, (90, 90))

        rp = self.img.sprites[self.right_p]["Portrait"][1]
        rp = self.p.transform.scale(rp, (90, 90))

        self.surface.blit(lp, (5, 5))
        self.surface2.blit(rp, (self.image5.get_width() + 3, 5))

    def reset(self):
        self.left_cur_health = 100
        self.left_max_health = 100
        self.left_tar_health = 100
        self.right_cur_health = 100
        self.right_max_health = 100
        self.right_tar_health = 100
        self.left_cur_mana = 100
        self.left_max_mana = 100
        self.left_tar_mana = 100
        self.right_cur_mana = 100
        self.right_max_mana = 100
        self.right_tar_mana = 100
        self.left_cur_energy = 100
        self.left_max_energy = 100
        self.left_tar_energy = 100
        self.right_cur_energy = 100
        self.right_max_energy = 100
        self.right_tar_energy = 100
        self.left_status_damage.reset()
        self.right_status_damage.reset()

    def reset_score(self):
        self.victory_1.reset()
        self.victory_2.reset()

    def render(self):
        self.health_bar("left")
        self.health_bar("right")
        self.mana_bar("left")
        self.mana_bar("right")
        self.energy_bar("left")
        self.energy_bar("right")
        self.win.blit(self.surface, self.rect1)
        self.win.blit(self.surface2, self.rect2)
        self.victory_1.render()
        self.victory_2.render()
        self.left_status_damage.render()
        self.right_status_damage.render()

    def send(self, x):
        self.left_status_damage.send(x)

    def set_info(self, lista):
        self.left_status_damage.add(self.left_tar_health, lista[0], "health")
        self.left_status_damage.add(self.left_tar_mana, lista[1], "mana")
        self.left_status_damage.add(self.left_tar_energy, lista[2], "energy")

        self.right_status_damage.add(self.right_tar_health, lista[3], "health")
        self.right_status_damage.add(self.right_tar_mana, lista[4], "mana")
        self.right_status_damage.add(self.right_tar_energy, lista[5], "energy")

        self.left_tar_health = lista[0]
        self.left_tar_mana = lista[1]
        self.left_tar_energy = lista[2]

        self.right_tar_health = lista[3]
        self.right_tar_mana = lista[4]
        self.right_tar_energy = lista[5]

    def energy_bar(self, side):
        t = self.image5.get_width()
        d = self.image5.get_width()
        if side == "left":
            self.energy1 = self.surface.blit(self.image5, (self.image1.get_width() - 2, 40))
            if self.left_cur_energy < self.left_tar_energy:
                self.left_cur_energy += self.bar_speed
                t = self.left_cur_energy / self.bar_ratio
                d = self.left_tar_energy / self.bar_ratio
                self.surface.blit(self.image44, self.energy1, (0, 0, d, 100))

            if self.left_cur_energy > self.left_tar_energy:
                self.left_cur_energy -= self.bar_speed
                t = self.left_tar_energy / self.bar_ratio
                d = self.left_cur_energy / self.bar_ratio
                self.surface.blit(self.image0, self.energy1, (0, 0, d, 100))
            self.surface.blit(self.image4, self.energy1, (0, 0, t, 100))
        if side == "right":
            self.energy2 = self.surface2.blit(self.image5, (0, 40))
            if self.right_cur_energy < self.right_tar_energy:
                self.right_cur_energy += self.bar_speed
                t = self.right_cur_energy / self.bar_ratio
                d = self.right_tar_energy / self.bar_ratio
                self.surface2.blit(self.image44, self.energy2, (0, 0, d, 100))

            if self.right_cur_energy > self.right_tar_energy:
                self.right_cur_energy -= self.bar_speed
                t = self.right_tar_energy / self.bar_ratio
                d = self.right_cur_energy / self.bar_ratio
                self.surface2.blit(self.image0, self.energy2, (0, 0, d, 100))
            self.surface2.blit(self.image4, self.energy2, (0, 0, t, 100))

    def mana_bar(self, side):
        t = self.image5.get_width()
        d = self.image5.get_width()
        if side == "left":
            self.mana1 = self.surface.blit(self.image5, (self.image1.get_width() - 2, 20))
            if self.left_cur_mana < self.left_tar_mana:
                self.left_cur_mana += self.bar_speed
                t = self.left_cur_mana / self.bar_ratio
                d = self.left_tar_mana / self.bar_ratio
                self.surface.blit(self.image33, self.mana1, (0, 0, d, 100))

            if self.left_cur_mana > self.left_tar_mana:
                self.left_cur_mana -= self.bar_speed
                t = self.left_tar_mana / self.bar_ratio
                d = self.left_cur_mana / self.bar_ratio
                self.surface.blit(self.image0, self.mana1, (0, 0, d, 100))
            self.surface.blit(self.image3, self.mana1, (0, 0, t, 100))
        if side == "right":
            self.mana2 = self.surface2.blit(self.image5, (0, 20))
            if self.right_cur_mana < self.right_tar_mana:
                self.right_cur_mana += self.bar_speed
                t = self.right_cur_mana / self.bar_ratio
                d = self.right_tar_mana / self.bar_ratio
                self.surface2.blit(self.image33, self.mana2, (0, 0, d, 100))

            if self.right_cur_mana > self.right_tar_mana:
                self.right_cur_mana -= self.bar_speed
                t = self.right_tar_mana / self.bar_ratio
                d = self.right_cur_mana / self.bar_ratio
                self.surface2.blit(self.image0, self.mana2, (0, 0, d, 100))
            self.surface2.blit(self.image3, self.mana2, (0, 0, t, 100))

    def health_bar(self, side):
        t = self.image5.get_width()
        d = self.image5.get_width()
        if side == "left":
            self.health1 = self.surface.blit(self.image5, (self.image1.get_width() - 2, 0))
            if self.left_cur_health < self.left_tar_health:
                self.left_cur_health += self.bar_speed
                t = self.left_cur_health / self.bar_ratio
                d = self.left_tar_health / self.bar_ratio
                self.surface.blit(self.image22, self.health1, (0, 0, d, 100))

            if self.left_cur_health > self.left_tar_health:
                self.left_cur_health -= self.bar_speed
                t = self.left_tar_health / self.bar_ratio
                d = self.left_cur_health / self.bar_ratio
                self.surface.blit(self.image0, self.health1, (0, 0, d, 100))
            self.surface.blit(self.image2, self.health1, (0, 0, t, 100))

        if side == "right":
            self.health2 = self.surface2.blit(self.image5, (0, 0))
            if self.right_cur_health < self.right_tar_health:
                self.right_cur_health += self.bar_speed
                t = self.right_cur_health / self.bar_ratio
                d = self.right_tar_health / self.bar_ratio
                self.surface2.blit(self.image22, self.health2, (0, 0, d, 100))

            if self.right_cur_health > self.right_tar_health:
                self.right_cur_health -= self.bar_speed
                t = self.right_tar_health / self.bar_ratio
                d = self.right_cur_health / self.bar_ratio
                self.surface2.blit(self.image0, self.health2, (0, 0, d, 100))
            self.surface2.blit(self.image2, self.health2, (0, 0, t, 100))

    def pos(self, side, size):
        if side == "left":
            x = size[0] * 0.01
            y = size[1] * 0.01
            return x, y
        else:
            x = size[0] * 0.99
            y = size[1] * 0.01
            return x, y

    def set_score(self, x):
        if x == 1:
            self.victory_1.set_score()
        if x == 2:
            self.victory_2.set_score()

class Victory:
    def __init__(self, info, facing, pos):
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]
        self.facing = facing
        self.pos = pos
        self.score = 0

        blank_element = self.p.transform.scale(self.img.image505, (20, 20))

        self.blank_rect = blank_element.get_rect()
        self.surface = self.p.Surface((self.blank_rect.w * 2, self.blank_rect.h), self.p.SRCALPHA)
        self.surface.blit(blank_element, (0, 0))
        self.surface.blit(blank_element, (self.blank_rect.w, 0))
        self.rect = self.placing()

    def placing(self):
        if self.facing == "left":
            x = self.pos[0] + 50
            y = self.pos[1] - 12
            return self.surface.get_rect(center=(x, y))
        if self.facing == "right":
            x = self.pos[0] - 50
            y = self.pos[1] - 12
            return self.surface.get_rect(center=(x, y))

    def render(self):
        self.win.blit(self.surface, self.rect)

    def set_score(self):
        filled_img = self.p.transform.scale(self.img.image506, (20, 20))
        self.score += 1
        if self.score == 1:
            self.surface.blit(filled_img, (0, 0))
        if self.score == 2:
            self.surface.blit(filled_img, (self.blank_rect.w, 0))

    def reset(self):
        blank_element = self.p.transform.scale(self.img.image505, (20, 20))
        self.surface.blit(blank_element, (0, 0))
        self.surface.blit(blank_element, (self.blank_rect.w, 0))

class ShowStatus:
    def __init__(self, info, facing):
        self.info = info
        self.lista = []
        self.facing = facing
        self.pos = None
        self.get_pos()

    def get_pos(self):
        pos = self.info[1]
        if self.facing == "left":
            self.pos = pos.fighter1_pos
        else:
            self.pos = pos.fighter2_pos

    def reset(self):
        self.lista = []

    def render(self):
        if len(self.lista) > 0:
            for item in self.lista:
                item.render()
                if item.delete:
                    self.lista.remove(item)

    def add(self, old, new, category):
        if old != new:
            if old > new:
                self.lista.append(ShowStatusMod(self.info, "-", old-new, category, self.pos))
            if old < new:
                self.lista.append(ShowStatusMod(self.info, "+", new-old, category, self.pos))

    def send(self, x):
        self.lista.append(ShowStatusMod(self.info, "", x, "msg", self.pos))

class ShowStatusMod:
    def __init__(self, info, damage_type,  value, category, pos):
        self.info = info
        self.p = info[0].p
        self.win = info[0].win
        self.damage_type = damage_type
        self.category = category
        self.value = str(value)
        self.time = 0

        self.black = (0, 0, 0)
        self.white = self.colour()
        self.delete = False

        self.x = pos[0]
        self.y = pos[1]

    def colour(self):
        if self.category == "health":
            return (255,0,0)
        elif self.category == "mana":
            return (30,144,255)
        elif self.category == "msg":
            return (255, 255, 255)
        else:
            return (255, 255, 0)

    def render(self):
        self.check()
        self.draw()
        self.move()

    def move(self):
        self.y -= 1
        self.time += 1

    def check(self):
        if self.time >= 100:
            self.delete = True

    def draw(self):
        ARCADE = self.info[0].ARCADE

        string = self.damage_type + " " +self.value
        txt = ARCADE.render(string, True, self.black)

        for i in range(-2, 3):
            for j in range(-2, 3):
                textbox = txt.get_rect()
                textbox.center = (self.x + i, self.y + j)
                self.win.blit(txt, textbox)

        text = ARCADE.render(string, True, self.white)
        textbox = text.get_rect()
        textbox.center = (self.x, self.y)
        self.win.blit(text, textbox)
