import sqlite3
import json


class Database:
    def __int__(self):
        self.conn = None
        self.create()

    def create(self):
        self.conn = sqlite3.connect("players.db")
        c = self.conn.cursor()
        c.execute("""create table if not exists players (
            name text,
            nickname text,
            password text,
            access integer,
            victory integer,
            image integer,
            UNIQUE(nickname)
        )""")

        c.execute("SELECT * FROM players WHERE nickname='admin'")
        if c.fetchone() == None:
            print("Admin account created")
            c.execute("INSERT INTO players VALUES('adm', 'admin', '123', '3', '9999', '4')")
        else:
            print("Admin account already exists")

        self.conn.commit()
        self.conn.close()

    def account(self, data, conn, addr):
        self.conn = conn
        conn = sqlite3.connect("players.db")
        c = conn.cursor()
        v = None

        if int(list(data.keys())[0]) == -99:
            data = data['-99']
            if len(data) == 3:
                v = self.create_account(c, data[0], data[1], data[2])
            elif len(data) == 2:
                v = self.login(c, data[0], data[1])

            conn.commit()
            conn.close()
        return v

    def login(self, c, nickname, password):
        v = None
        c.execute("SELECT * FROM players WHERE nickname=?", (nickname,))
        d = c.fetchone()

        if d is not None:
            if d[2] == password:
                v = [True, 2, "Server: Logged in!", d]
            else:
                v = [False, 3, "Wrong password!"]
        else:
            v = [False, 3, "Account doesn't exist!"]
        return v


    def create_account(self, c,  name, nickname, password):
        v = None
        c.execute("SELECT * FROM players WHERE nickname=?", (nickname,))
        if c.fetchone() == None:
            c.execute("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)", (name, nickname, password, 0, 0, 0))
            c.execute("SELECT * FROM players WHERE nickname=?", (nickname,))
            d = c.fetchone()
            v = [True, 1, "Server: Account Created!", d]
        else:
            v = [False, 3, "Nickname already in use!"]
        return v




    def data_send(self, msg):
        self.conn.sendall(json.dumps(msg).encode())