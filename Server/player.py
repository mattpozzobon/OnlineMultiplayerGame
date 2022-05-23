import json
from datetime import datetime

class Player(object):
    def __init__(self, name, nickname, access, score, picture, conn, addr):
        self.name = name
        self.nickname = nickname
        self.score = score
        self.access = access
        self.picture = picture
        self.conn = conn
        self.addr = addr


        self.game = None
        self.character = "Black"
        self.elements = []

    def character_att(self):
        char = {
            "Black":        {"gain": {"mana": 30},                   "lose": {"energy": 70}},
            "Wizard":       {"gain": {"mana": 30},                   "lose": {"energy": 70}},
            "Warlock":      {"gain": {"health": 20},                 "lose": {"mana": 40, "energy": 40}},
            "Fire Mage":    {"gain": {"mana": 30, "energy": 30},     "lose": {"health": 10}},
            "Dark Knight":  {"gain": {"mana": 50},                   "lose": {"health": 10}},
            "Priest":       {"gain": {"health": 20},                 "lose": {"energy": 70}},
            "Necromancer":  {"gain": {"mana": 40},                   "lose": {"energy": 50}},
        }
        return char


    def get_game(self):
        return self.game

    def set_game(self, game):
        self.game = game

    def update_score(self, x):
        self.score += x

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def set_score(self, x):
        self.score = x

    def get_score(self):
        return self.score

    def set_conn(self, conn):
        self.conn = conn

    def data_send(self, msg):
        self.conn.sendall(json.dumps(msg).encode())

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)