from messages import MESSAGE_ALL
from gameroom import GameRoom
from gamerooms import GameRooms
from player import Player

import json

class KeyPass(object):
    def __init__(self):
        self.gamerooms = None
        self.lobby = None
        self.net = None
        self.data = None
        self.player = None
        self.conn = None
        self.addr = None

    def start(self, net, data, conn, player):
        self.player = player
        self.net = net
        self.data = data
        self.conn = conn
        self.gamerooms = net.gamerooms
        self.lobby = net.lobby
        self.run()

    def run(self):
        print(f"{self.net.time()} [PLAYER: {self.player.name}] {self.data}")
        self.get_key(int(list(self.data.keys())[0]))

    def get_key(self, key):

        # STATUS
        if key == -1000:
            self.conn.sendall(json.dumps({-1000: "Online"}).encode())

        # LOGOUT
        if key == -1:
            self.conn.close()
            self.update_lobby()

        # UPDATE LOBBY
        if key == 0:
            self.lobby.send_message_all(self.get_msg(0))

        # SEND MSG ROOM
        if key == 1:
            msg = self.data.get(str(1))
            self.gamerooms.send_all(self.player, self.get_msg(1, player=self.player.name, msg=msg))

        # SEND MSG LOBBY
        if key == 2:
            msg = self.data.get(str(2))
            self.lobby.send_message_all(self.get_msg(2, player=self.player.name, msg=msg))
            self.update_lobby()

        if key == 3 and self.data['3'][0] == "create":
            r = self.gamerooms.create(self.player, self.data['3'][1])
            self.update_lobby()

        if key == 3 and self.data['3'][0] == "character":
            character = self.data['3'][1]
            self.gamerooms.set_character(self.player, character)

        if key == 3 and self.data['3'][0] == "spell":
            element = self.data['3'][1]
            self.gamerooms.set_element(self.player, element)

        if key == 3 and self.data['3'][0] == "join":
            ownerid = self.data['3'][1]
            if self.gamerooms.join(self.player, ownerid):
                self.gamerooms.update(self.player)
            self.update_lobby()

        if key == 3 and self.data['3'] == "remove":
            self.gamerooms.close(self.player)
            #self.player.conn.sendall(json.dumps({3: [{"flag": 4}, {"msg": "BACK TO LOBBY"}]}).encode())
            self.update_lobby()

        if key == 3 and self.data['3'] == "kick":
            self.gamerooms.kick(self.player) # kick the guest
            self.update_lobby()

        if key == 3 and self.data['3'] == "ready":
            self.gamerooms.ready(self.player)

        if key == 5:
            if self.data['5'][0] != None:
                self.gamerooms.fightaction(self.player, self.data['5'])


    def get_msg(self, x, **kwargs):
        msg = {
                0: {0: [{"players": self.lobby.client_get()}, {"rooms": self.gamerooms.get_rooms()}, {"msg": "ATT!"}]},
                1: {1: [{"player": kwargs.get('player', None)}, kwargs.get('msg', None)]},
                2: {2: [{"player": kwargs.get('player', None)}, kwargs.get('msg', None)]},

                3: {3: [{"msg": f"'{self.player.name}' created the room"}]},
                4: {3: [{"msg": f"info"}]},
                5: {3: [{"msg": f"'{self.player.name}' joined the room"}]},
                6: {3: [{"msg": f"'{self.player.name}' joined the Lobby!"}]},

        }
        return msg[x]

    def update_lobby(self):
        self.lobby.send_message_all(self.get_msg(0))