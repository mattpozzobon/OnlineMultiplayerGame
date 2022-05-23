from Client.components.fighter_cooldownbar import cooldownBar
from Client.components.fighter_sprite import Sprite
from Client.components.fighter_element_selected import Element_Selected

class Fighter:
    def __init__(self, info, power, pos, facing):
        self.info = info
        self.W = info[0].W
        self.H = info[0].H
        self.p = info[0].p
        self.c = info[4]
        self.win = info[0].win
        self.pos = (pos[0], pos[1])
        self.size = (pos[2], pos[3])
        self.rect = self.p.Rect(self.pos, self.size)
        self.power = power
        self.facing = facing


        self.sprite =       Sprite(self.info, self.facing, self.rect, "Black")

        self.elements_bar = Element_Selected(info, self.rect.midbottom)
        self.bar_cast =     cooldownBar(info, pos[0], pos[1]-50, pos[2], 15, "right")
        self.bar_cooldown = cooldownBar(info, pos[0], pos[1]-80,  pos[2], 15, "left")


    def render(self, enemy):
        #self.p.draw.rect(self.win, self.colour, self.rect)

        self.sprite.render(self.rect)

        if self.facing == "left":
            self.elements_bar.render()
            self.bar_cast.render()
            self.bar_cooldown.render()

    def set_character(self, name, elements):
        self.elements_bar.set_elements(elements)
        if name is not None:
            self.sprite = Sprite(self.info, self.facing, self.rect, name)

    def reset(self):
        self.sprite.setaction("Idle")

    def update(self, actions):
        try:
            if actions is None:
                return

            if actions[0][0] == "change_element":
                if actions[0][1] is not None:
                    self.elements_bar.change_element(actions[0][1])
                    self.bar_cooldown.add(1)
                    self.bar_cast.cancel()
                    self.sprite.setaction("Change_element")

            if actions[0] == "attack_start":
                self.bar_cast.add(4.5)
                self.sprite.setaction("Attack_start")

            if actions[0] == "melee_start":
                self.bar_cast.add(0.5)

            if actions[0] == "melee_release":
                self.bar_cooldown.add(3.5)

            if actions[0] == "damage_received":
                self.bar_cooldown.add(1)
                self.bar_cast.cancel()
                self.sprite.setaction("Hurt")

            if actions[0][0] == "attack_release":
                self.sprite.setaction("Attack_release")
                level = int(actions[0][1])
                element = str(actions[0][2])
                self.power.add(self.rect, self.facing, level, element)
                self.bar_cooldown.add(0.5)
                self.bar_cast.cancel()

            if actions[0] == "idle":
                self.sprite.setaction("Idle")

            if actions[0] == "special":
                self.sprite.setaction("special")

            if actions[0] == "Defense":
                self.bar_cast.cancel()
                self.bar_cooldown.add(1)
                self.sprite.setaction("Defense")

            if actions[0] == "damage_blocked":
                pass

            if actions[0] == "Charge":
                self.bar_cast.cancel()
                self.bar_cooldown.add(1)
                self.sprite.setaction("Charge")

            if actions[0] == "death":
                self.bar_cast.cancel()
                self.sprite.setaction("Death")
                self.bar_cast.cancel()

            if actions[0][0] == "fail":
                if len(actions[0]) >= 2:
                    self.bar_cast.cancel()

                    if actions[0][1] == "ShieldBroke":
                        self.sprite.setaction("FailShieldBroke")

                    if actions[0][1] == "Cooldown":
                        self.sprite.setaction("FailCooldown")

                    if actions[0][1] == "Spell":
                        self.sprite.setaction("FailSpell")
        except:
            pass