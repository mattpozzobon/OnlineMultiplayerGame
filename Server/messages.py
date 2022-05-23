import json


def on_login(player, lobby, gamerooms):
    msg = {0: [{"players": lobby.client_get()},
               {"rooms": gamerooms.get_rooms()},
               {"msg": f"{player.get_name()} has entered!"}]}
    lobby.send_message_all(msg)


def on_logout(player, lobby, gamerooms):
    msg = {0: [{"players": lobby.client_get()},
               {"rooms": gamerooms.get_rooms()},
               {"msg": f"{player.get_name()} has left!"}]}
    lobby.send_message_all(msg)

def MESSAGE_ALL(players, msg):
    try:
        for player in players:
            player.conn.sendall(json.dumps(msg).encode())
    except Exception as e:
        print(f"[CUSTOM_MSG][SEND_MESSAGE]{e}")

# WARNING # ERROR # ALERT
def custom_msg(players, msg_type, msg):

    m = {99: [{"type": msg_type}, {"msg": msg}]}

    if isinstance(players, list):
        try:
            for player in players:
                player.conn.sendall(json.dumps(m).encode())
        except Exception as e:
            pass
    else:
        try:
            players.conn.sendall(json.dumps(m).encode())
        except Exception as e:
            pass