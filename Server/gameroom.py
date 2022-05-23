from datetime import datetime
from battleroom import *
import time as t

class GameRoom(object):
    def __init__(self, lobby):
        self.var_disconnected = False
        self.owner = None
        self.label = None
        self.stage = 1
        self.players = []
        self.status = []
        self.lobby = lobby
        self.max = 2
        self.time = 20
        self.time_characters = 10
        self.time_elements = 10
        self.battleroom = BattleRoom()

    def reset(self):
        self.var_disconnected = False
        self.status = []
        self.time = 30
        self.time_characters = 10
        self.time_elements = 10
        self.stage = 1

    def get_owner(self):
        return self.owner

    def create(self, player, string):
        self.owner = player.name
        self.label = string
        self.add(player)
        return self

    def count(self):
        return len(self.players)

    def ready(self, player):
        if player in self.status:
            self.status.remove(player)
            self.send([player], {3: [{"flag": 31}, {"msg": "UNREADY"}]})
        elif player not in self.status:
            self.status.append(player)
            self.send([player], {3: [{"flag": 32}, {"msg": "READY"}]})

        self.send(self.players, {3: [{"flag": 50}, {"msg": "READY FOR ALL"}, {"players": self.players_info()}]})

        if len(self.status) == self.max:
            self.reset()
            tt = Thread(target=self.choose_character, args=())
            tt.start()


    def choose_character(self):
        self.stage = 2
        str = {"msg": f"Choose your character, in {self.time_characters} seconds."}
        self.send(self.players, {3: [{"flag": 21}, str, {"timer": self.time_characters}]})
        while self.time_characters >= 0:
            if self.var_disconnected:
                break
            t.sleep(1)
            self.time_characters -= 1

        if self.stage == 2:
            tt = Thread(target=self.choose_elements, args=())
            tt.start()

    def choose_elements(self):
        self.stage = 3

        str = {"msg": f"Choose 2 elements, in {self.time_elements} seconds."}
        self.send(self.players, {3: [{"flag": 20}, str, {"timer": self.time_elements}]})

        while self.time_elements >= 0:
            if self.var_disconnected:
                break
            t.sleep(1)
            self.time_elements -= 1

        for player in self.players:
            if len(player.elements) < 2:
                player.elements = ["Fire", "Water"]

        if self.stage == 3:
            tt = Thread(target=self.start, args=())
            tt.start()

    def update_player_characters(self):

        img =       {"image": [self.players[0].character, self.players[1].character]}
        elements =  {"elements": [self.players[0].elements, self.players[1].elements]}
        msg = {3: [{"flag": 60}, {"msg": "UPDATE IMAGE AND ELEMENTS"}, img, elements]}
        self.players[0].conn.sendall(json.dumps(msg).encode())

        img = {"image": [self.players[1].character, self.players[0].character]}
        elements = {"elements": [self.players[1].elements, self.players[0].elements]}
        msg = {3: [{"flag": 60}, {"msg": "UPDATE IMAGE AND ELEMENTS"}, img, elements]}
        self.players[1].conn.sendall(json.dumps(msg).encode())


    def start(self):
        self.update_player_characters()

        # OLD TIMER BEFORE MOVING TO SCENARIO 4
        #self.send(self.players, {3: [{"flag": 22}, {"msg": f"Game will start in {self.time} seconds"}]})

        if self.var_disconnected is False:
            # resetting
            time.sleep(0.1)
            self.send(self.players, {3: [{"flag": 23}, {"msg": "START"}]})
            time.sleep(0.1)
            self.send(self.players, {3: [{"flag": 23}, {"msg": "START"}]})
            self.stage = 4
            self.battleroom = BattleRoom()
            self.battleroom.start(self.players, self.owner)
        self.send(self.players, {3: [{"flag": 25}, {"msg": "BACK TO LOBBY"}, {"players": self.players_info()}]})

    def add(self, player):
        if self.count() < self.max:
            try:
                if player not in self.players:
                    player.set_game(self)
                    self.players.append(player)
                    self.lobby.remove(player)
            except Exception as e:
                print(e)

    def disconnected(self, player):
        self.var_disconnected = True
        self.players.remove(player)
        # 1 - Still in gameroom, getting ready
        if self.stage == 1:
            self.close(player)
            for player in self.players:
                self.send([player], {3: [{"flag": 31}, {"msg": "UNREADY"}]})

        if self.stage == 2 or self.stage == 3:
            self.stage = 1
            self.close(player)

        if self.stage == 4:

            self.battleroom.stop()
            self.close(player)
            for player in self.players:
                self.send([player], {3: [{"flag": 31}, {"msg": "UNREADY"}]})
        self.reset()
        self.battleroom = BattleRoom()

    def players_info(self):
        l = []
        for g in self.players:
            a = None
            if g in self.status:
                a = "True"
            else:
                a = "False"
            l.append([g.name, g.score, g.picture, a])
        return l


    def close(self, player):
        self.status = []

        if player.name == self.owner:
            for p in self.players:
                msg = {3: [{"flag": 4}, {"msg": "BACK TO LOBBY"}]}
                p.conn.sendall(json.dumps(msg).encode())
                p.set_game(None)
                self.lobby.add(p)
                self.players = []
        else:
            for p in self.players:
                if player.name == p.name:
                    msg = {3: [{"flag": 4}, {"msg": "BACK TO LOBBY"}]}
                    p.conn.sendall(json.dumps(msg).encode())
                    p.set_game(None)
                    self.lobby.add(p)
                    self.players.remove(p)

            self.update()


    def update(self):
        for player in self.players:
            if player.name == self.owner:
                msg = {3: [{"flag": 11}, {"msg": "UPDATE FOR OWNER"}, {"players": self.players_info()}]}
            else:
                msg = {3: [{"flag": 10}, {"msg": "UPDATE FOR GUEST"}, {"players": self.players_info()}]}
            player.conn.sendall(json.dumps(msg).encode())

    def fightaction(self, player, action):
        self.battleroom.fightaction(player, action)

    def kick(self, game):
        for player in game.players:
            if player.name != game.owner:
                self.close(player)

    def send(self, p, msg):
        try:
            for player in p:
                player.conn.sendall(json.dumps(msg).encode())
        except Exception as e:
            time = datetime.now().strftime("[%d/%m - %H:%M:%S]")
            print(f"{time}[GAME][SEND_MESSAGE]{e}")


    def sendchat(self, msg):
        try:
            for player in self.players:
                player.conn.sendall(json.dumps(msg).encode())
        except Exception as e:
            time = datetime.now().strftime("[%d/%m - %H:%M:%S]")
            print(f"{time}[GAME][SEND_MESSAGE]{e}")

    def __set_name__(self, owner, name):
        self.name = self.owner

    def __eq__(self, other):
        if not isinstance(other, GameRoom):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.owner == other.owner