import time

class PlayerFighter(object):
    def __init__(self, player):
        self.player = player

        self.elements = player.elements
        self.character = player.character
        self.element_index = 0

        self.name = player.get_name()
        self.health = 100
        self.mana = 100
        self.stamina = 100
        self.win = 0

        self.cooldown = time.time()
        self.startattack = time.time()
        self.lastattack = time.time()
        self.shoot = False

        self.test = False

        self.status = time.time()
        self.status_type = "idle"

    def get_cooldown(self):
        if (self.lastattack-time.time()) <= 0:
            return True
        return False

    def set_cooldown(self, x):
        self.lastattack = time.time()+x

    def start_attack(self):
        self.startattack = time.time()

    def cast_stamina(self, x):
        if self.stamina >= x:
            self.addStamina(-x)
            return True
        else:
            return False

    def cast(self, x):
        if self.mana >= x:
            self.addMana(-x)
            return True
        else:
            return False

    def spell_level(self):
        x = time.time() - self.startattack
        return int(x)

    def cooldown_start_melee(self, x):
        if self.get_cooldown():
            if self.check_stamina(10):
                self.start_attack()
                self.shoot = False
                return x[0]
        return "fail", "Cooldown", "Cooldown"

    def cooldown_start_spell(self, x):
        if self.get_cooldown():
            if self.check_mana(10):
                self.start_attack()
                self.shoot = False
                return x[0]
        return "fail", "Cooldown", "Cooldown"

    def cooldown_realease_melee(self, x):
        ti = (time.time() - self.startattack)
        if ti >= 0.5:
            if not self.shoot:
                if self.cast_stamina(20):
                    self.set_cooldown(3.5)
                    self.shoot = True
                    return x[0]
        return "fail", "Spell", "Cast too soon"

    def cooldown_realease_spell(self, x):
        ti = (time.time() - self.startattack)
        if not self.get_cooldown():
            return "fail", "Cooldown", "Interrupted"

        if self.status_type == "idle":
            return "fail", "Cooldown", "Need to recast"

        if ti <= 1:
            return "fail", "Spell", "Cast too soon"

        if ti >= 4.5:
            return "fail", "Spell", "Cast too late"

        if not self.shoot:
            sp = self.spell_level()
            if self.cast(sp * 10):
                self.set_cooldown(0.5)
                self.shoot = True
                return x[0], sp, self.elements[self.element_index]

    def defense(self, x):
        if self.get_cooldown() and self.check_mana(5):
            self.addMana(-5)
            self.set_cooldown(1)
            return x[0]
        return "fail", "Cooldown"

    def charging(self, x):
        if self.get_cooldown():
            self.set_cooldown(1)
            return x[0]
        return "fail", "Cooldown", "Cooldown"

    def damage(self, x):
        if self.status_type == "Defense":
            self.addStamina(-x[1])
            return "damage_blocked"
        else:
            if self.status_type == "attack_start":
                self.set_cooldown(1)
                self.status_type = "idle"
            self.addHealth(-x[1])
            return x[0]

    def change_element(self, x):
        if self.get_cooldown() and self.check_stamina(50):
            self.addStamina(-50)
            self.set_cooldown(1)

            self.element_index += 1
            if self.element_index >= len(self.elements):
                self.element_index = 0
            return x[0], self.element_index
        else:
            return "fail", "Cooldown", "Need Stamina"

    def special(self, x):
        if self.get_cooldown():
            char = self.player.character_att()
            gain = char[self.player.character].get("gain")
            lose = char[self.player.character].get("lose")

            for item in lose:
                if item == "mana":
                    if not self.check_mana(lose[item]):
                        return "fail", "Cooldown", "Not enough Mana"

                elif item == "health":
                    if not self.check_health(lose[item]):
                        return "fail", "Cooldown", "Not enough Health"

                elif item == "energy":
                    if not self.check_stamina(lose[item]):
                        return "fail", "Cooldown", "Not enough Energy"


            for item in lose:
                if item == "mana":
                    self.addMana(-lose[item])
                elif item == "health":
                    self.addHealth(-lose[item])
                elif item == "energy":
                    self.addStamina(-lose[item])

            for item in gain:
                if item == "mana":
                    self.addMana(gain[item])
                elif item == "health":
                    self.addHealth(gain[item])
                elif item == "energy":
                    self.addStamina(gain[item])

            return x[0]

        else:
            return "fail", "Cooldown", "Cooldown"


    def action(self, action):
        print(action)
        if action[0] == "change_element":
            action[0] = self.change_element(action)
            self.status_type = "idle"
            return

        if action[0] == "damage_received":
            action[0] = self.damage(action)
            return

        if action[0] == "attack_release":
            action[0] = self.cooldown_realease_spell(action)
            self.status_type = "idle"
            return

        if action[0] == "Charge":
            action[0] = self.charging(action)

        if action[0] == "Defense":
            action[0] = self.defense(action)

        if action[0] == "special":
            action[0] = self.special(action)
            self.status_type = "idle"
            return

        if action[0] == "attack_start":
            action[0] = self.cooldown_start_spell(action)

        self.status_type = action[0]

    def render(self):
        if (time.time() - self.status) >= 0.5 and self.get_cooldown():
            self.status = time.time()

            if self.status_type == "idle":
                self.addStamina(5)

            if self.status_type == "Charge":
                self.addMana(10)

            if self.status_type == "Defense":
                if self.check_mana(5):
                    self.addMana(-5)
                else:
                    self.status_type = "idle"
                    self.test = True

    def check_health(self, x):
        if self.health >= x+1:
            return True
        return False

    def check_mana(self, x):
        if self.mana >= x:
            return True
        return False

    def check_stamina(self, x):
        if self.stamina >= x:
            return True
        return False

    def addHealth(self, x):
        self.health += x
        if self.health < 0:
            self.health = 0
        if self.health > 100:
            self.health = 100

    def addMana(self, x):
        self.mana += x
        if self.mana < 0:
            self.mana = 0
        if self.mana > 100:
            self.mana = 100

    def addStamina(self, x):
        self.stamina += x
        if self.stamina < 0:
            self.stamina = 0
        if self.stamina > 100:
            self.stamina = 100

    def getStamina(self):
        return self.stamina

    def setStamina(self, x):
        self.stamina = x

    def getHealth(self):
        return self.health

    def setHealth(self, x):
        self.health = x

    def getMana(self):
        return self.mana

    def setMana(self, x):
        self.mana = x

    def reset(self):
        self.health = 100
        self.mana = 100


    def getWin(self):
        return self.win

    def setWin(self, x):
        self.win = x

    def __eq__(self, other):
        return ((self.health) == (other.health))

    def __ne__(self, other):
        return not (self.health == other.health)

    def __lt__(self, other):
        return ((self.health) < (other.health))

    def __gt__(self, other):
        return ((self.health) > (other.health))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

