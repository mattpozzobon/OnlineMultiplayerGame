print("+ = "+__name__)
from Client.config import obj_posistion, obj_images, obj_sound
from Client.config import obj_create


class Load:
    def __init__(self, data, pyga, conn):
        self.positions =    obj_posistion.Load(pyga)
        self.images =       obj_images.Load(pyga)
        self.sounds =       obj_sound.Load(pyga)
        self.components =   obj_create.Load([pyga, self.positions, self.images, data, conn, self.sounds])

print("- = "+__name__)