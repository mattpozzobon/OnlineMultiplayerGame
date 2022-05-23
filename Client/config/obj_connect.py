import time

class Load:
    # p = python # c = components # d = data # f = frame
    def __init__(self):
        self.FRAME = [1, 0]
        self.FRAME_LOBBY = []

        # USED TO DISPLAY READY/KICK BUTTONS IN THE ROOM
        self.display_buttons = True
        # USED TO DISPLAY PLAYERS IN THE ROOM
        self.room_list = []

        self.STATUS = "Fetching"
        self.TIME = 0
        self.TIME2 = 0


        self.HASWEBCAM = None
        self.TOCLIENT = []
        self.TOSERVER = []
        self.RECEIVE = []

        self.FROMWEBCAM = {"Right": None, "Left": None}
        self.LAST_ACTION = None
        self.CURRENT_ACTION = None
        self.lastaction = time.time()
        self.cooldown = 0.2

        self.PLAYERS_ONLINE = 0


    def CLIENTMSG(self, msg):
        self.TOCLIENT.append(msg)

    def SERVERMSG(self, msg):
        self.TOSERVER.append(msg)

    def FROMSERVER(self, msg):
        self.RECEIVE.append(msg)

    def FROMHANDGESTURE(self, msg):
        if msg[0] == "Right":
            self.FROMWEBCAM["Right"] = msg[1]
            self.CLIENTMSG(["hands", "Right", self.FROMWEBCAM["Right"]])

        if msg[0] == "Left":
            self.FROMWEBCAM["Left"] = msg[1]
            self.CLIENTMSG(["hands", "Left", self.FROMWEBCAM["Left"]])

        if self.FROMWEBCAM["Left"] is not None and self.FROMWEBCAM["Right"] is not None:
            if (self.lastaction - time.time()) <= 0:
                self.lastaction = time.time()+self.cooldown
            else:
                return

            left = self.FROMWEBCAM["Left"]
            right = self.FROMWEBCAM["Right"]

            if left == "Open" and right == "Open":
                if self.LAST_ACTION == "attack_start":
                    self.CURRENT_ACTION = "attack_release"
                else:
                    self.CURRENT_ACTION = "idle"

            if left == "Open" and right == "Close":
                self.CURRENT_ACTION = "attack_start"

            if left == "Close" and right == "Close":
                self.CURRENT_ACTION = "Charge"

            if left == "Close" and right == "Open":
                self.CURRENT_ACTION = "Defense"

            if left == "Pointer" and right == "Pointer":
                self.CURRENT_ACTION = "special"

            if left == "Pointer" and right == "Close":
                self.CURRENT_ACTION = "change_element"

            if self.LAST_ACTION != self.CURRENT_ACTION:
                self.LAST_ACTION = self.CURRENT_ACTION

                if self.FRAME == [4, 0]:
                    self.CLIENTMSG([self.CURRENT_ACTION])


            self.FROMWEBCAM = {"Right": None, "Left": None}

