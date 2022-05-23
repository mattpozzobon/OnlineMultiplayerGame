from Client.scenarios import sc_1_menu
from Client.scenarios import sc_2_lobby
from Client.scenarios import sc_3_gameroom
from Client.scenarios import sc_4_battleroom

def switch(c, conn):
    FRAME = conn.FRAME

    if FRAME[0] == 1:
        sc_1_menu.start(c, FRAME)

    if FRAME[0] == 2:
        sc_2_lobby.start(c, conn)

    if FRAME[0] == 3:
        sc_3_gameroom.start(c, conn)

    if FRAME[0] == 4:
        sc_4_battleroom.start(c, FRAME)



