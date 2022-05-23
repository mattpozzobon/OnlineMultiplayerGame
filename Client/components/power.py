import math
from math import atan2, degrees, pi

class Power:
    def __init__(self, info):
        self.info = info
        self.list = []
        self.f1_rect = None
        self.f2_rect = None
        self.init = False
        self.distance = None

    def dis(self):
        return self.f2_rect.midleft[0]-self.f1_rect.midright[0]

    def add(self, rect, facing, spell_level, spell_element):
        self.list.append(Spell(self.info, rect, facing, spell_level, self.distance, spell_element))

    def reset(self):
        self.list = []

    def first_time_running(self, f1, f2):
        self.init = True
        self.f1_rect = f1
        self.f2_rect = f2
        self.distance = self.dis()

    def render(self, f1, f2):
        if not self.init:
            self.first_time_running(f1, f2)

        if len(self.list) > 0:
            for spell in self.list:
                spell.render(f1, f2, self.list)

                if spell.delete:
                    self.list.remove(spell)

class Spell:
    def __init__(self, info, rect, facing, level, distance, element):
        self.c = info[4]
        self.p = info[0].p
        self.win = info[0].win
        self.W = info[0].W
        self.H = info[0].H

        self.ignore = False
        self.delete = False
        self.f1 = None
        self.f2 = None
        self.collision = []

        self.lib = self.library(distance, facing)
        self.element = element
        self.level = level
        self.distance = distance
        self.spell_info = self.lib[self.element][self.level]

        self.flag_shield = False
        self.dir = self.spell_info["dir"]
        self.vel = self.spell_info["speed"]
        self.health = self.spell_info["health"]
        self.type = self.spell_info["type"]
        self.facing = self.spell_info["dir"]
        self.size = self.spell_info["size"]
        self.sprite = PowerSprite(info, self.facing,  self.level, self.element, distance, self.size)
        self.rect = self.spell_pos(rect)

    def spell_pos(self, rect):
        if self.type == "meteor":
                x = rect.midtop[0]
                y = rect.midtop[1]-self.distance/2
                return self.p.Rect(x, y, 30, rect.height)

        if self.type == "lightning":
            y = rect.midtop[1] - self.distance * 0.3
            if self.dir == "left":
                x = rect.topright[0] + (self.distance+20)
                return self.p.Rect(x, y, 10, 10)
            if self.dir == "right":
                x = rect.topleft[0] - (self.distance+20)
                return self.p.Rect(x, y, 10, 10)

        if self.dir == "left":
            return self.p.Rect(rect.topright[0]+self.spell_info["pos_extra_x"], rect.topright[1]-self.spell_info["pos_extra_y"], 30, rect.height)
        return self.p.Rect(rect.topleft[0]-self.spell_info["pos_extra_x"], rect.topleft[1]-self.spell_info["pos_extra_y"], 30, rect.height)

    def move(self):
        if self.type == "projectile" and self.sprite.action == "moving":
            if self.dir == "left":
                self.rect.x  += self.vel
            if self.dir == "right":
                self.rect.x -= self.vel

        if self.type == "meteor" and self.sprite.action == "moving":
            if self.dir == "left":
                self.rect.x += self.distance * self.spell_info["speed"]
                self.rect.y += (self.distance/2) * self.spell_info["speed"]
            if self.dir == "right":
                self.rect.x -= self.distance * self.spell_info["speed"]
                self.rect.y += (self.distance / 2) * self.spell_info["speed"]

        if self.type == "lightning" and self.sprite.action == "moving" and not self.ignore:
            self.rect.height  += self.vel

        if self.type == "beam" and self.sprite.action == "moving":
            if self.dir == "left":
                self.rect = self.p.Rect(self.f1.midright[0], self.rect.y, self.f2.x - self.f1.midright[0] + 100, self.rect.height)
            if self.dir == "right":
                self.rect = self.p.Rect(self.f1.midright[0] - 100, self.rect.y, self.f2.midleft[0] - self.f1.midright[0], self.rect.height)

    def library(self, dis, fac):
        if dis is None:
            return
        lib = {
            "Fire": {
                1: {"type": "projectile", "health": 1, "damage": 10, "size": 2, "speed": int(dis * 0.010), "pos_extra_x": 0, "pos_extra_y": 0, "dir": fac},
                2: {"type": "projectile", "health": 2, "damage": 20, "size": 2, "speed": int(dis * 0.008), "pos_extra_x": 0, "pos_extra_y": 0, "dir": fac},
                3: {"type": "shield",     "health": 5, "damage": 0,  "size": 6, "speed": 0,                "pos_extra_x": 50,"pos_extra_y": 0, "dir": fac},
                4: {"type": "beam",       "health": 10, "damage": 40, "size": 3, "speed": int(dis),        "pos_extra_x": 0, "pos_extra_y": 0, "dir": fac},
            },
            "Earth": {
                1: {"type": "projectile", "health": 2, "damage": 10, "size": 5, "speed": int(dis * 0.005), "pos_extra_x": 0, "pos_extra_y": 0, "dir": fac},
                2: {"type": "projectile", "health": 3, "damage": 20, "size": 4, "speed": int(dis * 0.005), "pos_extra_x": 0, "pos_extra_y": 0, "dir": fac},
                3: {"type": "meteor",     "health": 1, "damage": 30, "size": 4, "speed": 0.01,             "pos_extra_x": 4, "pos_extra_y": 3, "dir": fac},
                4: {"type": "shield",     "health": 10, "damage": 0, "size": 5, "speed": int(dis),         "pos_extra_x": 80, "pos_extra_y": 0, "dir": fac},
            },
            "Thunder": {
                1: {"type": "projectile", "health": 1, "damage": 10, "size": 4, "speed": int(dis * 0.010), "pos_extra_x": 50, "pos_extra_y": 0, "dir": fac},
                2: {"type": "projectile", "health": 2, "damage": 20, "size": 5, "speed": int(dis * 0.008), "pos_extra_x": 0, "pos_extra_y": 0,  "dir": fac},
                3: {"type": "shield",     "health": 10, "damage": 0, "size": 6, "speed": 0,                 "pos_extra_x": 70, "pos_extra_y": 0,  "dir": fac},
                4: {"type": "lightning",  "health": 5,   "damage": 40, "size": 6, "speed": int(dis * 0.005),  "pos_extra_x": 0, "pos_extra_y": 0, "dir": fac},
            },
            "Water": {
                1: {"type": "projectile", "health": 1, "damage": 10, "size": 2, "speed": int(dis * 0.010), "pos_extra_x": 50, "pos_extra_y": 0, "dir": fac},
                2: {"type": "projectile", "health": 2, "damage": 20, "size": 2, "speed": int(dis * 0.008), "pos_extra_x": 0, "pos_extra_y": 0,  "dir": fac},
                3: {"type": "projectile", "health": 10, "damage": 50, "size": 4, "speed": int(dis * 0.004),"pos_extra_x": 0, "pos_extra_y": 0,  "dir": fac},
                4: {"type": "shield",     "health": 5, "damage": 0, "size": 3, "speed": 0,                  "pos_extra_x": 70, "pos_extra_y": 0, "dir": fac},
            },
            "Wind": {
                1: {"type": "projectile", "health": 1, "damage": 10, "size": 3, "speed": int(dis * 0.016), "pos_extra_x": 0, "pos_extra_y": 0, "dir": fac},
                2: {"type": "projectile", "health": 2, "damage": 20, "size": 3, "speed": int(dis * 0.014), "pos_extra_x": 20, "pos_extra_y": 0,  "dir": fac},
                3: {"type": "projectile", "health": 4, "damage": 50, "size": 10, "speed": int(dis * 0.012), "pos_extra_x": 0, "pos_extra_y": 0,  "dir": fac},
                4: {"type": "shield",     "health": 5, "damage": 0,  "size": 6,  "speed": 0,               "pos_extra_x": -50, "pos_extra_y": 0, "dir": fac},
            }
        }
        return lib

    def collision_w_different_bullet(self, spells):
        for spell in spells:
            if self == spell:
                return
            if spell.dir == self.dir:
                return
            if self.rect.colliderect(spell):
                if self not in spell.collision and spell not in self.collision:
                    spell.collision.append(self)
                    self.collision.append(spell)
                    self.change_level(spell)

    def change_level(self, spell):
        if spell.health > self.health:
            spell.health = spell.health - self.health
            self.health = 0
            self.ignore = True
            self.sprite.draw_hitting_effect()

        elif self.health > spell.health:
            self.health = self.health - spell.health
            spell.health = 0
            spell.ignore = True
            spell.sprite.draw_hitting_effect()
        else:
            self.health = 0
            spell.health = 0
            spell.ignore = True
            spell.sprite.draw_hitting_effect()
            self.ignore = True
            self.sprite.draw_hitting_effect()

    def collision_w_player(self):
        if self.type == "projectile" or self.type == "meteor" or self.type == "lightning":
            if self.dir == "left" and not self.ignore:
                if self.rect.colliderect(self.f2):
                    self.ignore = True
                    self.sprite.draw_hitting_effect()

            elif self.dir == "right" and not self.ignore:
                if self.rect.colliderect(self.f1):
                    self.ignore = True
                    self.sprite.draw_hitting_effect()
                    self.c.CLIENTMSG(["damage_received", self.spell_info["damage"], self.element])

        elif self.type == "beam":
            if self.dir == "right" and not self.ignore:
                if self.rect.colliderect(self.f1) and not self.ignore:
                    self.ignore = True
                    self.c.CLIENTMSG(["damage_received", self.spell_info["damage"], self.element])

        self.delete = self.sprite.delete

    def render(self, f1, f2, spells):
        self.f1 = f1
        self.f2 = f2
        #self.p.draw.rect(self.win, (0, 255, 0), self.rect)
        self.sprite.render(self.rect)
        self.move()
        self.collision_w_player()
        self.collision_w_different_bullet(spells)

class PowerSprite:
    def __init__(self, info, direction, level, element, distance, size):
        self.released_spell = False
        self.win = info[0].win
        self.img = info[2]
        self.p = info[0].p

        self.delete = False
        self.green_rect = None

        self.distance = distance
        self.element = element
        self.level = level
        self.direction = direction

        self.action = "casting"
        self.action_n = 1

        self.size = size
        self.img_position = "center"
        self.lightning = False
        self.lightning_n = 0
        self.beam = False
        self.beam_n = 0
        self.beam_list = []
        self.image_n_2 = None
        self.second_hit = False
        self.shield = False
        self.image_n = 0
        self.image_speed = 0.2
        self.image = self.img.spells[self.element]["level_" + str(level)][self.image_n]
        self.img_rect = self.image.get_rect()
        self.quantity = len(self.img.spells[self.element]["level_" + str(level)])-1

    def render(self, rect):
        self.green_rect = rect
        self.addspeed()
        self.thunder()
        self.fire()
        self.water()
        self.earth()
        self.wind()
        self.draw()
        self.draw_beam()

    def addspeed(self):
        if self.lightning:
            self.lightning_n += self.image_speed
        if self.second_hit:
            self.image_n_2 += self.image_speed
        if not self.beam:
            self.image_n += self.image_speed

    def draw(self):
        if not self.delete:
            if not self.beam:
                self.image = self.img.spells[self.element]["level_"+str(self.level)][int(self.image_n)]
                h, w = self.image.get_rect().size
                self.image = self.p.transform.scale(self.image, (h * self.size, w * self.size))

                if self.direction == "right":
                    self.image = self.p.transform.flip(self.image, True, False)

                if self.second_hit:
                    self.image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n_2)]
                    if self.direction == "right":
                        self.image = self.p.transform.flip(self.image, True, False)

                self.img_positionn()
                self.win.blit(self.image, self.img_rect)
            else:
                if self.action_n == 2:
                    self.image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n[0])]

                    h, w = self.image.get_rect().size
                    self.image = self.p.transform.scale(self.image, (h * self.size, w * self.size))

                    if self.direction == "right":
                        self.image = self.p.transform.flip(self.image, True, False)

                    if self.second_hit:
                        self.image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n_2)]
                        if self.direction == "right":
                            self.image = self.p.transform.flip(self.image, True, False)

                    self.img_positionn()
                    self.win.blit(self.image, self.img_rect)


    def img_positionn(self):
        if self.img_position == "water_ball":
            self.img_rect = self.image.get_rect()
            self.img_rect.center = self.green_rect.midbottom

        if self.img_position == "water_shield":
            if self.direction == "left":
                self.img_rect = self.image.get_rect()
                self.img_rect.midleft = self.green_rect.midleft

            if self.direction == "right":
                self.img_rect = self.image.get_rect()
                self.img_rect.midright = self.green_rect.midright

        if self.img_position == "top":
            self.img_rect = self.image.get_rect()
            self.img_rect.center = self.green_rect.midtop

        if self.img_position == "center":
            self.img_rect = self.image.get_rect()
            self.img_rect.center = self.green_rect.center

        if self.img_position == "bottom":
            self.img_rect = self.image.get_rect()
            self.img_rect.midbottom = self.green_rect.midbottom

    def draw_hitting_effect(self):
        self.action_n = -99

    def thunder(self):
        if self.element == "Thunder":
            if self.level == 1:
                self.casting_spell("center", "projectile",
                                   [0, 12, "casting", 0.2],
                                   [13, 18, "moving", 0.2],
                                   [19, self.quantity])

            if self.level == 2:
                self.casting_spell("center", "projectile",
                                   [0, 11, "casting", 0.2],
                                   [12, 20, "moving", 0.2],
                                   [21, self.quantity])

            if self.level == 3:
                self.casting_spell("center", "shield",
                                   [0, 6, "casting", 0.10],
                                   [7, 11, "casting", 0.10],
                                   [12, self.quantity],
                                   )

            if self.level == 4:

                self.cast_lightning()

    def wind(self):
        if self.element == "Wind":
            if self.level == 1:
                self.casting_spell("center", "projectile",
                                   [5, 7, "moving", 0.2],
                                   [5, 7, "moving", 0.2],
                                   [0, 4])

            if self.level == 2:
                self.casting_spell("center", "projectile",
                                   [0, 5, "casting", 0.2],
                                   [6, 8, "moving", 0.2],
                                   [9, self.quantity])

            if self.level == 3:
                self.casting_spell("bottom", "projectile",
                                   [0, 4, "casting", 0.2],
                                   [5, 10, "moving", 0.2],
                                   [11, self.quantity],
                                   )

            if self.level == 4:
                self.casting_spell("center", "shield",
                                   [0, self.quantity, "casting", 0.15],
                                   [0, self.quantity, "casting", 0.15],
                                   [0, self.quantity])

    def earth(self):
        if self.element == "Earth":
            if self.level == 1:
                self.casting_spell("center", "projectile",
                                   [0, 5, "moving", 0.2],
                                   [0, 5, "moving", 0.2],
                                   [6, self.quantity])

            if self.level == 2:
                self.casting_spell("bottom", "projectile",
                                   [0, self.quantity, "moving", 0.2],
                                   [0, self.quantity, "moving", 0.2],
                                   [0, self.quantity])

            if self.level == 3:
                self.casting_spell("bottom", "projectile",
                                   [7, 11, "casting", 0.1],
                                   [12, 12, "moving", 0.2],
                                   [13, self.quantity],
                                   )

            if self.level == 4:
                self.casting_spell("center", "shield",
                                   [0, 11, "casting", 0.1],
                                   [12, 17, "casting", 0.2],
                                   [18, self.quantity])

    def water(self):
        if self.element == "Water":
            if self.level == 1:
                self.casting_spell("center", "projectile",
                                   [15, 18, "casting", 0.2],
                                   [19, self.quantity, "moving", 0.2],
                                   [0, 14])

            if self.level == 2:
                self.casting_spell("water_ball", "projectile",
                                   [0, 8, "casting", 0.2],
                                   [9, 17, "moving", 0.2],
                                   [18, self.quantity])

            if self.level == 3:
                self.casting_spell("bottom", "projectile",
                                   [15, self.quantity, "casting", 0.2],
                                   [8, 14, "moving", 0.2],
                                   [0, 7])

            if self.level == 4:
                self.casting_spell("water_shield", "shield",
                                   [25, self.quantity, "casting", 0.2],
                                   [15, 24, "casting", 0.2],
                                   [0, 14])

    def fire(self):
        if self.element == "Fire":
            if self.level == 1:
                self.casting_spell("center", "projectile",
                                   [4, 7, "moving", 0.2],
                                   [4, 7, "moving", 0.2],
                                   [8, self.quantity])

            if self.level == 2:
                self.casting_spell("center", "projectile",
                                   [0, 5, "moving", 0.2],
                                   [6, 9, "moving", 0.2],
                                   [10, self.quantity])

            if self.level == 3:
                self.casting_spell("center", "shield",
                                   [10, self.quantity, "casting", 0.2],
                                   [6, 9, "casting", 0.2],
                                   [0, 5])

            if self.level == 4:
                self.casting_spell("center", "beam",
                                   [0, 7, "casting"],
                                   [16],
                                   [8])

    def cast_lightning(self):
        self.img_position = "top"
        if self.action_n == 1:
            self.image_n = 0
            self.action_n = 2

        if self.action_n == 2:
            if self.image_n >= 11:
                self.image_n = 12
                self.lightning_n = 31
                self.action_n = 3
                self.lightning = True

        if self.action_n == 3:
            self.action = "moving"
            if self.image_n >= 16:
                self.image_n = 12
            if self.lightning_n >= 36:
                self.lightning_n = 31

        if self.action_n == -99:
            self.image_n = 18
            self.lightning_n = 37
            self.action_n = -98

        if self.action_n == -98:
            if self.image_n >= 30:
                self.image_n = self.quantity

            if self.lightning_n >= self.quantity-1:
                self.lightning_n = self.quantity
                self.lightning = False

            if self.lightning_n >= self.quantity and self.image_n >= 30:
                self.delete = True


        if self.lightning:
            self.image = self.img.spells[self.element]["level_" + str(self.level)][int(self.lightning_n)]
            h, w = self.image.get_rect().size
            self.image = self.p.transform.scale(self.image, (h * self.size, w * self.size))
            self.img_rect = self.image.get_rect()
            self.img_rect.center = self.green_rect.midbottom
            self.win.blit(self.image, self.img_rect)

    def casting_spell(self, pos, spell_type, casting, idle, hit, *args):
        if spell_type == "projectile" or spell_type == "shield":
            self.img_position = pos
            if self.action_n == 1:
                self.image_n = casting[0]
                self.action_n = 2

            if self.action_n == 2:
                self.action = casting[2]
                self.image_speed = casting[3]
                if self.image_n >= casting[1]:
                    self.action_n = 3
                    self.image_n = idle[0]

            if self.action_n == 3:
                self.action = idle[2]
                self.image_speed = idle[3]
                if self.image_n >= idle[1]:
                    self.image_n = idle[0]

            if self.action_n == -99:
                self.action = "hit"
                self.image_n = hit[0]
                self.action_n = -98

            if self.action_n == -98:
                if args:
                    if args[0][0] == "hit2":
                        self.second_hit = True
                        self.image_n_2 = args[0][1]

                        if self.image_n >= hit[1] or self.image_n_2 >= args[0][2]:
                            self.delete = True

                elif self.image_n >= hit[1]:
                    self.delete = True

        if spell_type == "beam":
            self.beam = True
            self.img_position = "center"

            if self.action_n == 1:
                self.image_n = [casting[0], idle[0], hit[0]]
                self.action_n = 2

            if self.action_n == 2:
                self.action = "casting"
                self.image_n[0] += 0.05
                if self.image_n[0] >= casting[1]:
                    self.image_n[0] = -99
                    self.action_n = 3

            if self.action_n == 3:
                self.action = "moving"
                self.released_spell = True
                self.beam_list = self.create_beam(self.green_rect)
                self.action_n = 4
                self.beam_n = max([idle[0], hit[0]])

            if self.action_n == 4:
                x = 0.20
                self.image_n[1] += x
                self.image_n[2] += x
                self.beam_n += x
                if self.beam_n >= self.quantity:
                    self.delete = True

    def create_beam(self, rect):
        lista = []
        image = self.img.spells[self.element]["level_" + str(self.level)][4]
        h, w = image.get_rect().size
        image = self.p.transform.scale(image, (h * self.size, w * self.size))
        h, w = image.get_rect().size
        step = int(w / 2)

        if self.direction == "left":
            for x in range(rect.midleft[0]+50, int(self.distance*2), step):
                lista.append((x, rect.midleft[1]))
            return lista
        else:
            for x in range(rect.midright[0] - 50, int((rect.midright[0]-50)-self.distance*2), -step):
                lista.append((x, rect.midright[1]))
            return lista

    def draw_beam(self):
        if self.beam:
            if self.image_n[0] >= 0 and not self.delete:
                self.image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n[0])]
                if self.direction == "right":
                    self.image = self.p.transform.flip(self.image, True, False)
                self.win.blit(self.image, self.img_rect)


            if self.image_n[0] < 0 and not self.delete:
                if self.direction == "left":
                    if type(self.beam_list) == list:
                        for i in range(len(self.beam_list)):
                            image = None
                            if i == 0:
                                image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n[1])]
                            else:
                                image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n[2])]

                            h, w = image.get_rect().size
                            image = self.p.transform.scale(image, (h * self.size, w * self.size))
                            image_rect = image.get_rect()
                            image_rect.center = self.beam_list[i]
                            self.win.blit(image, image_rect)

                if self.direction == "right":
                    for i in range(len(self.beam_list)):
                        image = None
                        if i == 0:
                            image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n[1])]
                        else:
                            image = self.img.spells[self.element]["level_" + str(self.level)][int(self.image_n[2])]

                        h, w = image.get_rect().size
                        image = self.p.transform.scale(image, (h * self.size, w * self.size))
                        image = self.p.transform.flip(image, True, False)
                        image_rect = image.get_rect()
                        image_rect.center = self.beam_list[i]
                        self.win.blit(image, image_rect)




