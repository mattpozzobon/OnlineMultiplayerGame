import socket
import threading
from datetime import datetime
from lobby import Lobby
from keys import *
from messages import *
from database import Database

PORT = 5555
SERVER = "localhost"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DISCONNECT_MSG = "!DISCONNECT"


class Server:
    def __init__(self):
        self.lobby = Lobby()
        self.gamerooms = GameRooms(self.lobby)
        self.keypass = KeyPass()
        self.database = Database()
        self.database.create()

    def time(self):
        return datetime.now().strftime("[%d/%m - %H:%M:%S]")

    def player_thread(self, conn, addr):
        player = None
        run = True
        while run:
            try:
                data = self.data_get(conn, 1024)
                print(data)
                if player != None:
                    self.keypass.start(self, data, conn, player)
                else:
                    v = self.database.account(data, conn, addr)
                    if v[0]:
                        player = Player(v[3][0], v[3][1], v[3][3], v[3][4], v[3][5], conn, addr)

                    self.data_send(conn, {-99: [{"flag": v[1]}, {"msg": v[2]}]})
                    self.on_login(player)

            except Exception as e:
                print(e)
                run = False


        self.on_logout(player)
        player = None
        conn.close()

    def connection_thread(self):
        try:
            try:
                server.bind((SERVER, PORT))
            except socket.error as e:
                print(e)

            print(f"{self.time()} [SERVER ON]")

            while True:
                try:
                    server.listen()
                    conn, addr = server.accept()
                    print(f"{self.time()} [CONNECT] IP CONNECTED = {addr}")
                    tt = threading.Thread(target=self.player_thread, args=(conn, addr))
                    tt.start()
                except Exception as e:
                    print(f"{self.time()} [Z1] {e}")
        except Exception as e:
            print(f"{self.time()} [Z2] ", e)

    """
     CUSTOM METHODS
    """

    def data_get(self, conn, bytes):
        data = conn.recv(bytes)
        data = json.loads(data.decode())
        return data

    def data_send(self, conn, msg):
        conn.sendall(json.dumps(msg).encode())

    def on_login(self, player):
        if player:
            self.lobby.add(player)
            on_login(player, self.lobby, self.gamerooms)
            print(f"{self.time()} [CONNECTED][{player.name}]{player.addr} ")

    def on_logout(self, player):
        if player:
            self.gamerooms.disconnected(player)
            self.lobby.disconnected(player)
            on_logout(player, self.lobby, self.gamerooms)
            print(f"{self.time()} [DISCONNECTED][{player.name}]{player.addr} ")

if __name__ == "__main__":
    s = Server()
    t1 = threading.Thread(target=s.connection_thread)
    t1.start()