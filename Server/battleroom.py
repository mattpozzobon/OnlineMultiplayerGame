import sys

from fighters import Fighters
from threading import Thread
from messages import *
import time

class BattleRoom(object):
    def __init__(self):
        self.players = []
        self.fighters = Fighters(self.players)
        self.owner = None
        self.round_number = 1
        self.round_max = 3
        self.round_timer_between = 2
        self.round_timer = 120
        self.cancel = False
        self.close = False
        self.disconnected = False

    def start(self, players, owner):
        self.players = players
        self.owner = owner
        self.fighters = Fighters(self.players)
        self.fighters.create_fighters()
        self.fighters.send_info()
        self.fighters.reset()
        self.repeat()

    def repeat(self):
        if not self.close:
            self.fighters.reset()
            if not self.cancel:
                self.counter()
            if self.cancel:
                self.round_start()


    def fightaction(self, player, action):
        index = self.players.index(player)
        self.fighters.action(index, action)
        self.fighters.response(index, action)


    def round_start(self):
        Thread(target=self.round_counter, args=()).start()
        self.fighters.start()

        while self.cancel:
            if self.round_timer <= 0 or self.fighters.dead():
                self.cancel = False

        self.round_end()

    def round_end(self):
        self.fighters.stop()
        self.round_number += 1

        self.fighters.whowon(self.disconnected)

        time.sleep(2)
        if self.fighters.isitfinished() or self.disconnected:
            self.game_finished()
            self.close = True
        else:
            self.repeat()
            self.cancel = False


    def game_finished(self):
        self.fighters.addvictorytoplayer(self.disconnected)

        for p in self.players:
            time.sleep(0.1)
            if p.name == self.owner:
                self.send(p, {5: [{"flag": 10}, {"msg": "OWNER"}]})
            else:
                self.send(p, {5: [{"flag": 11}, {"msg": "GUEST"}]})

        self.close_game()

    def stop(self):
        self.disconnected = True
        self.cancel = False
        self.fighters.stop()
        self.close = True


    def close_game(self):
        self.players = []
        self.fighters = []
        self.cancel = False
        self.close = False


    def round_counter(self):
        self.send(self.players, {5: [{"flag": 18}, {"msg": f"{self.round_timer}"}, {"round": self.round_number}]})
        timer = self.round_timer
        try:
            while self.cancel:
                if self.disconnected:
                    break
                if timer >= 0:
                    time.sleep(1)
                    timer -= 1
                else:
                    self.cancel = False
                    break

        except Exception as e:
            print(e)

    def counter(self):
        time.sleep(0.1)
        timer = self.round_timer_between
        self.send(self.players, {5: [{"flag": 17}, {"msg": timer}, {"round": self.round_number}]})

        try:
            while True:
                if self.disconnected:
                    break
                if timer >= 0:
                    time.sleep(1)
                    timer -= 1
                else:
                    break
            self.cancel = True

        except Exception as e:
            print(e)


    def send(self, p, msg):
        try:
            if self.disconnected is False:
                if isinstance(p, list):
                    for player in p:
                        player.conn.sendall(json.dumps(msg).encode())
                else:
                    p.conn.sendall(json.dumps(msg).encode())
        except Exception as e:
            print(e)