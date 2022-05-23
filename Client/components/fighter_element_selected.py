
class Element_Selected:
    def __init__(self, info, pos):
        self.p = info[0].p
        self.win = info[0].win
        self.img = info[2]

        self.pos = pos
        self.element_index = 0
        self.elements = None


        self.blank_element = self.img.spells_icons["Blank"][0]
        self.blank_rect = self.blank_element.get_rect()

        self.surface = self.p.Surface((self.blank_rect.w * 2, self.blank_rect.h), self.p.SRCALPHA)
        self.surface.blit(self.blank_element, (0, 0))
        self.surface.blit(self.blank_element, (self.blank_rect.w, 0))

    def render(self):
        rect = self.surface.get_rect(midtop=(self.pos[0], self.pos[1]+5))
        self.win.blit(self.surface, rect)

    def set_elements(self, elements):
        self.elements = elements

        self.surface = self.p.Surface((self.blank_rect.w * 2, self.blank_rect.h), self.p.SRCALPHA)
        self.surface.blit(self.blank_element, (0, 0))
        self.surface.blit(self.blank_element, (self.blank_rect.w, 0))

        element_1_img = self.img.spells_icons[self.elements[0]][0]
        element_2_img = self.img.spells_icons[self.elements[1]][1]

        self.surface.blit(element_1_img, (0, 0))
        self.surface.blit(element_2_img, (self.blank_rect.w, 0))

    def change_element(self, x):
        if x == 0:
            element_1_img = self.img.spells_icons[self.elements[0]][0]
            element_2_img = self.img.spells_icons[self.elements[1]][1]
        else:
            element_1_img = self.img.spells_icons[self.elements[0]][1]
            element_2_img = self.img.spells_icons[self.elements[1]][0]


        self.surface.blit(element_1_img, (0, 0))
        self.surface.blit(element_2_img, (self.blank_rect.w, 0))

