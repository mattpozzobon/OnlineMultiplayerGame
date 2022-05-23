import json
from datetime import datetime

class Lobby(object):
    def __init__(self):
        self.players = []

    def client_get(self):
        emp = []
        for player in self.players:
            emp.append([player.nickname, player.score, player.picture])
        return emp

    def add(self, player):
        self.players.append(player)
        #print("test added player from lobby")

    def disconnected(self, player):
        if player in self.players:
            self.players.remove(player)
            #print("test removed player from lobby disconnected")

    def remove(self, player):
        if player in self.players:
            self.players.remove(player)
            #print("test removed player from lobby")

    def get_players(self):
        return self.players

    def count(self):
        return len(self.players)

    def send_message_all(self, msg):
        try:
            for player in self.players:
                player.conn.sendall(json.dumps(msg).encode())
        except Exception as e:
            time = datetime.now().strftime("[%d/%m - %H:%M:%S]")
            print(f"{time}[LOBBY][SEND_MESSAGE]{e}")