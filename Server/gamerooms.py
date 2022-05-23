from gameroom import GameRoom
from messages import *

class GameRooms(object):
    def __init__(self, lobby):
        self.gamerooms = []
        self.lobby = lobby

    def create(self, player, label):
        game = GameRoom(self.lobby).create(player, label)
        if game not in self.gamerooms:
            self.gamerooms.append(game)
            self.send(player, {3: [{"flag": 1}, {"msg": "ROOM CREATED INFO SENT"}, {"players": [[player.name, player.score, player.picture]]}]})
            self.send(player, {500: [{"msg": f"Room created"}]})
            return True
        else:
            return False

    def close(self, player):
        game = player.get_game()
        if game in self.gamerooms:
            game.close(player)
            if game.owner == player.get_name():
                self.gamerooms.remove(game)

    def kick(self, player):
        game = player.get_game()
        if game in self.gamerooms:
            game.kick(game)

    def ready(self, player):
        game = player.get_game()
        game.ready(player)

    def set_character(self, player, character):
        player.character = character

    def set_element(self, player, element):
        if element in player.elements:
            player.elements.remove(element)
        elif len(player.elements) < 2:
            player.elements.append(element)
        elif len(player.elements) == 2:
            player.elements[0] = element
        self.send(player, {3: [{"flag": "61"}, {"msg": "ELEMENTS"}, {"elements": player.elements}]})

    def disconnected(self, player):
        game = player.get_game()
        if game in self.gamerooms:
            game.disconnected(player)
            if game.owner == player.get_name():
                self.gamerooms.remove(game)

    def join(self, player, ownerid):
        if len(self.gamerooms) >= 1:
            if player.get_game() == None:

                game = None
                for x in self.gamerooms:
                    if x.owner == ownerid:
                        game = x

                if game != None:
                    if len(game.players) < game.max:
                        if game in self.gamerooms:
                            game.add(player)
                            self.send(player, {3: [{"flag": "7"}, {"msg": "individual msg!"}]})
                            return True
                        else:
                            custom_msg(player, "ERROR", "Game Room not found.")
                    else:
                        custom_msg(player, "WARNING", "Game Room selected is now full.")
            else:
                custom_msg(player, "ERROR", "Already in a Game Room.")
        else:
            custom_msg(player, "ERROR", "No Game Rooms avaliable.")

    def fightaction(self, player, action):
        game = player.get_game()
        game.fightaction(player, action)

    def send_all(self, player, msg):
        game = player.get_game()
        game.sendchat(msg)

    def send(self, player, msg):
        player.conn.sendall(json.dumps(msg).encode())

    def get_rooms(self):
        l = []
        for g in self.gamerooms:
            l.append([g.owner, g.label, str(g.count())])
        return l

    def update(self, player):
        game = player.get_game()
        game.update()

    def count(self):
        return len(self.gamerooms)

    def print(self):
        return print(f"Number of rooms: {self.count()}")