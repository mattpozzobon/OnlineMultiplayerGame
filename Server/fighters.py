import sys

from playerfighter import PlayerFighter
from threading import Thread
import json
import time

class Fighters:
    def __init__(self, players):
        self.players = players
        self.fighters = []
        self.running = True

    def create_fighters(self):
        arr = []
        for player in self.players:
            fighter = PlayerFighter(player)
            arr.append(fighter)
        self.fighters = arr

    def reset(self):
        self.send(self.players, {5: [{"flag": 21}, {"action": "reset"}]})
        for fighter in self.fighters:
            fighter.reset()

    def dead(self):
        for fighter in self.fighters:
            if fighter.getHealth() <= 0:
                self.response(self.players.index(fighter.player), ["death"])
                return True

    def whowon(self, disconnected):
        if disconnected:
            for f in self.fighters:
                self.send(f.player, {5: [{"flag": 22}, {"action": "Disconnected"}]})
        else:
            t = []
            for f in self.fighters:
                t.append(f.getHealth())

            index = t.index(max(t))
            self.fighters[index].setWin(self.fighters[index].getWin() + 1)

            for f in self.fighters:
                if self.fighters[index].name == f.name:
                    self.send(f.player, {5: [{"flag": 22}, {"action": "won"}]})
                if self.fighters[index].name != f.name:
                    self.send(f.player, {5: [{"flag": 23}, {"action": "lost"}]})

    def isitfinished(self):
        for f in self.fighters:
            if f.getWin() == 2:
                return True
        return False

    def addvictorytoplayer(self, disconnected):
        if not disconnected:
            for f in self.fighters:
                if f.getWin() == 2:
                    f.player.set_score(f.player.get_score() + 1)


    def start(self):
        self.running = True
        Thread(target=self.render, args=()).start()

    def render(self):
        while self.running:
            time.sleep(1)
            for f in self.fighters:
                f.render()
                self.send_info()

                if f.test:
                    f.test = False
                    self.response(self.players.index(f.player), [["fail", "ShieldBroke", "Shield Broke"]])

    def stop(self):
        self.running = False

    def send_info(self):
        f1 = None
        f2 = None

        for player in self.players:
            for f in self.fighters:
                if f.player == player:
                    f1 = {"left": [f.name, f.getHealth(), f.getMana(), f.getStamina()]}
                else:
                    f2 = {"right": [f.name, f.getHealth(), f.getMana(), f.getStamina()]}

            self.send(player, {5: [{"flag": 1}, {"msg": ""}, f1, f2]})


    def action(self, index, action):
        self.fighters[index].action(action)

    def response(self, index, action):
        for player in self.players:
            if player == self.players[index]:
                self.send(player, {5: [{"flag": 5}, {"action": action}, self.info(player)]})
            else:
                self.send(player, {5: [{"flag": 6}, {"action": action}, self.info(player)]})

    def info(self, player):
        f1 = None
        f2 = None

        for f in self.fighters:
            if f.player == player:
                f1 = [f.getHealth(), f.getMana(), f.getStamina()]
            else:
                f2 = [f.getHealth(), f.getMana(), f.getStamina()]
        return {"info": f1+f2}


    def send(self, p, msg):
        try:
            if isinstance(p, list):
                for player in p:
                    player.conn.sendall(json.dumps(msg).encode())
            else:
                p.conn.sendall(json.dumps(msg).encode())
        except Exception as e:
            print(e)