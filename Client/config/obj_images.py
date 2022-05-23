print("+ = "+__name__)
import glob

class Load:
    def __init__(self, pyga):
        p = pyga.p
        self.p = pyga.p

        self.img_check_blank =  p.image.load("assets/login_menu/checkbox.png").convert_alpha()
        self.img_check_inner =  p.image.load("assets/login_menu/checkbox_inner.png").convert_alpha()
        self.img_input =        p.image.load("assets/login_menu/input.png").convert_alpha()
        self.img_input_focus =  p.image.load("assets/login_menu/input_focus.png").convert_alpha()

        self.img_pic5 =         p.image.load("assets/login_menu/btn_normal.png").convert_alpha()
        self.img_pic6 =         p.image.load("assets/login_menu/btn_hover.png").convert_alpha()
        self.img_pic7 =         p.image.load("assets/login_menu/btn_press.png").convert_alpha()

        self.img_lobby_users =  p.image.load("assets/users.png").convert_alpha()
        self.img_lobby_rooms =  p.image.load("assets/rooms.png").convert_alpha()
        self.img_lobby_chat =   p.image.load("assets/chat.png").convert_alpha()
        self.img_lobby_logout = p.image.load("assets/logout.png").convert_alpha()

        self.img_lobby_1 =      p.image.load("assets/background_lobby/1.png").convert_alpha()
        self.img_lobby_2 =      p.image.load("assets/background_lobby/2.png").convert_alpha()


        self.img_battle_1 =     p.image.load("assets/background_battleroom/1.png").convert_alpha()
        self.img_battle_2 =     p.image.load("assets/background_battleroom/2.png").convert_alpha()
        self.img_battle_3 = p.image.load("assets/background_battleroom/3.png").convert_alpha()

        self.image0 =           p.image.load("assets/fighter_status/target.png").convert_alpha()
        self.image1 =           p.image.load("assets/fighter_status/border.png").convert_alpha()
        self.image2 =           p.image.load("assets/fighter_status/health.png").convert_alpha()
        self.image22 =          p.image.load("assets/fighter_status/health2.png").convert_alpha()
        self.image3 =           p.image.load("assets/fighter_status/mana.png").convert_alpha()
        self.image33 =          p.image.load("assets/fighter_status/mana2.png").convert_alpha()
        self.image4 =           p.image.load("assets/fighter_status/energy.png").convert_alpha()
        self.image44 =          p.image.load("assets/fighter_status/energy2.png").convert_alpha()
        self.image5 =           p.image.load("assets/fighter_status/blank.png").convert_alpha()

        self.image505 =           p.image.load("assets/fighter_status/Blank_win.png").convert_alpha()
        self.image506 =           p.image.load("assets/fighter_status/Active_win.png").convert_alpha()

        self.sprites = self.load_character()
        self.effects = self.load_effects()
        self.spells = self.load_spells()
        self.auras = self.load_auras()
        self.avatars = self.load_avatars()
        self.hands = self.load_hands()
        self.spells_icons = self.load_spells_icons()


    def load_hands(self):
        folders = ["Left", "Right"]
        sprites = {}

        for hand in folders:
            lista = []
            for filename in glob.glob("assets/hands/" + hand + '/*.png'):
                img = self.p.image.load(filename).convert_alpha()
                lista.append(img)
            sprites[hand] = lista
        return sprites

    def load_spells_icons(self):
        folders = ["Blank", "Fire", "Water", "Earth", "Wind", "Thunder"]
        sprites = {}

        for element in folders:
            lista = []
            for filename in glob.glob("assets/Spells/Icons/" + element + '/*.png'):
                img = self.p.image.load(filename).convert_alpha()
                lista.append(img)
            sprites[element] = lista
        return sprites

    def load_avatars(self):
        imgs = []
        for filename in glob.glob("assets/avatars/*.png"):
                img = self.p.image.load(filename).convert_alpha()
                img = self.p.transform.scale(img, (32, 32))
                imgs.append(img)
        return imgs

    def load_spells(self):
        folders = ["Fire", "Water", "Earth", "Wind", "Thunder"]
        subfolder = ["Icon", "level_1", "level_2", "level_3", "level_4"]

        element_list = {}

        for element in folders:
            spell_list = {}
            for spell in subfolder:
                imgs = []
                for filename in glob.glob("assets/Spells/"+element+'/'+spell+'/*.png'):
                    img = self.p.image.load(filename).convert_alpha()
                    imgs.append(img)
                spell_list[spell] = imgs
            element_list[element] = spell_list

        return element_list

    def load_auras(self):
        load = ["Charge", "Defense", "Change_element", "Fail", "Special"]
        sprites = {}

        for action in load:
            lista = []
            for filename in glob.glob("assets/Auras/" + action +'/*.png'):
                img = self.p.image.load(filename).convert_alpha()
                h, w = img.get_rect().size
                img = self.p.transform.scale(img, (h * 4, w * 4))
                lista.append(img)

            sprites[action] = lista
        return sprites

    def load_effects(self):
        spells = ["Explosion", "Explosion_2"]
        lista = {}

        for spell in spells:
            listaa = []
            img = self.p.image.load("assets/Spells/" + spell + ".png").convert_alpha()
            h = img.get_height()
            w = img.get_width()
            total = w / h

            for i in range(1, int(total)):
                rect = self.p.Rect(i * int(h), 0, int(h), int(h))
                listaa.append(img.subsurface(rect))

            lista[spell] = listaa
        return lista


    def load_character(self):
        folders = ["Dark Knight", "Warlock", "Wizard", "Black", "Fire Mage", "Necromancer", "Priest"]
        subfolder = ["Portrait", "Attack", "Attack_start", "Attack_release", "Idle", "Death", "Hurt", "Fail"]

        characters = {}

        for character in folders:
            spell_list = {}
            for actions in subfolder:
                imgs = []
                for filename in glob.glob("assets/Characters/" + character + '/' + actions + '/*.png'):
                    img = self.p.image.load(filename).convert_alpha()
                    h, w = img.get_rect().size
                    img = self.p.transform.scale(img, (h * 4, w * 4))
                    imgs.append(img)
                spell_list[actions] = imgs
            characters[character] = spell_list

        return characters

print("- = "+__name__)