from win32api import GetSystemMetrics
from Client.components.player import Player

def action(p, c, d, con, net):

    if len(con.TOCLIENT) == 0:
        return

    x = con.TOCLIENT.pop()
    popmessage = c.components.popmessage


    if x[0] == "hands":
        c.components.battleroom_hands.set(x[1], x[2])

    if x[0] == "character":
        con.SERVERMSG({3: x})

    if x[0] == "spell":
        con.SERVERMSG({3: x})

    # BATTLE
    if x[0] == "damage_received":
        con.SERVERMSG({5: x})

    if x[0] == "damage_dealt":
        con.SERVERMSG({5: x})

    if x[0] == "change_element":
        con.SERVERMSG({5: x})

    if x[0] == "attack_start":
        con.SERVERMSG({5: x})

    if x[0] == "attack_release":
        con.SERVERMSG({5: x})

    if x[0] == "Defense":
        con.SERVERMSG({5: x})

    if x[0] == "idle":
        con.SERVERMSG({5: x})

    if x[0] == "Charge":
        con.SERVERMSG({5: x})

    if x[0] == "special":
        con.SERVERMSG({5: x})

    if x[0] == "exit_tab_button": p.RUN = False

    if x[0] == "login_tab_button":      con.FRAME = [1, 1]
    if x[0] == "account_tab_button":    con.FRAME = [1, 2]
    if x[0] == "options_tab_button":    con.FRAME = [1, 3]
    if x[0] == "video_options":         con.FRAME = [1, 4]

    if x[0] == "fullscreen":
        d.resolution(GetSystemMetrics(0), GetSystemMetrics(1))
        popmessage.add("Need to restart Client", 5)
    if x[0] == "1920x1080":
        d.resolution(1920, 1080)
        popmessage.add("Need to restart Client", 5)
    if x[0] == "1366x768":
        d.resolution(1366, 768)
        popmessage.add("Need to restart Client", 5)
    if x[0] == "1200x800":
        d.resolution(1200, 800)
        popmessage.add("Need to restart Client", 5)
    if x[0] == "1536x864":
        d.resolution(1536, 864)
        popmessage.add("Need to restart Client", 5)
    if x[0] == "800x600":
        d.resolution(800, 600)
        popmessage.add("Need to restart Client", 5)

    if x[0] == "comfirm_ip":
        popmessage.add("Need to restart Client", 5)
        d.write("ip", c.components.options_input_ip.str)

    if x[0] == "comfirm_camera":
        popmessage.add("Need to restart Client", 5)
        d.write("camera", c.components.options_input_camera.str)


    if x[0] == "login_confirm":
        c = c.components
        con.SERVERMSG({-99: [c.login_nick.str, c.login_pass.str]})
        if con.STATUS == "Offline":
            popmessage.add("Server is Offline", 5)

    if x[0] == "account_confirm":
        c = c.components
        nick = c.account_nick.str
        name = c.account_name.str
        pass1 = c.account_pass1.str
        pass2 = c.account_pass2.str
        check = validate(c, {"name": name, "nickname": nick, "password 1": pass1, "password 2": pass2})
        if check:
            con.SERVERMSG({-99: [c.account_name.str, c.account_nick.str, c.account_pass1.str]})

    if x[0] == "lobby_logout":
        # net.disconnect()
        n = 1
        if n in con.FRAME_LOBBY:
            con.FRAME_LOBBY.remove(n)
        else:
            con.FRAME_LOBBY.append(n)

    if x[0] == "lobby_users":
        n = 2
        if n in con.FRAME_LOBBY:
            con.FRAME_LOBBY.remove(n)
        else:
            con.FRAME_LOBBY.append(n)

    if x[0] == "lobby_chat":
        n = 3
        if n in con.FRAME_LOBBY:
            con.FRAME_LOBBY.remove(n)
        else:
            con.FRAME_LOBBY.append(n)

    if x[0] == "lobby_rooms":
        n = 4
        if n in con.FRAME_LOBBY:
            con.FRAME_LOBBY.remove(n)
        else:
            con.FRAME_LOBBY.append(n)

    if x[0] == "comfirm_logout":
        if 1 in con.FRAME_LOBBY:
            c.components.button_slide_logout.click()
        if 2 in con.FRAME_LOBBY:
            c.components.button_slide_users.click()
        if 3 in con.FRAME_LOBBY:
            c.components.button_slide_chat.click()
        if 4 in con.FRAME_LOBBY:
            c.components.button_slide_rooms.click()

        con.FRAME = [1, 0]
        net.end()

    # cancel logout
    if x[0] == "cancel_logout":
        c.components.button_slide_logout.click()

    if x[0] == "comfirmroomcreation":
        input = c.components.lobby_rooms_display.getinput()
        con.SERVERMSG({3: ["create", input]})

    if x[0] == "joinroom":
        con.SERVERMSG({3: ["join", x[1]]})

    if x[0] == "gameroomexit":
        con.SERVERMSG({3: "remove"})

    if x[0] == "kickplayerout":
        con.SERVERMSG({3: "kick"})

    if x[0] == "readyformatch":
        con.SERVERMSG({3: "ready"})








def receive(p, c, d, con):

    if len(con.RECEIVE) == 0:
        return

    popmsg = c.components.popmessage
    x = con.RECEIVE.pop()

    if "5" in x:
        flag =  x["5"][0]["flag"]

        # INFO ABOUT WHO'S LEFT WHO'S RIGHT
        if flag == 1:
            l_name = x["5"][2]["left"][0]
            l_health = x["5"][2]["left"][1]
            l_mana = x["5"][2]["left"][2]
            l_stamina =  x["5"][2]["left"][3]

            r_name = x["5"][3]["right"][0]
            r_health = x["5"][3]["right"][1]
            r_mana = x["5"][3]["right"][2]
            r_stamina = x["5"][3]["right"][3]

            c.components.battleroom_status.set_info([l_health, l_mana, l_stamina, r_health, r_mana, r_stamina])

        # YOURSELF (LEFT)
        if flag == 5:
            actions = x["5"][1]["action"]
            c.components.battleroom_fighter1.update(actions)

            lista = x["5"][2]["info"]
            c.components.battleroom_status.set_info(lista)

            if actions[0][0] == "fail" and len(actions[0]) >= 3:
                c.components.battleroom_status.send(actions[0][2])

        # ENEMY (RIGHT)
        if flag == 6:
            actions = x["5"][1]["action"]
            c.components.battleroom_fighter2.update(actions)

            lista = x["5"][2]["info"]
            c.components.battleroom_status.set_info(lista)



        #RESET
        if flag == 21:
            c.components.battleroom_status.reset()
            c.components.battleroom_power.reset()
            c.components.battleroom_fighter1.reset()
            c.components.battleroom_fighter2.reset()

        # ROUND WIN
        if flag == 22:
            actions = x["5"][1]["action"]
            c.components.sound.play(actions)
            popmsg.add(actions, 5)
            c.components.battleroom_status.set_score(1)

        # LOST ROUND
        if flag == 23:
            actions = x["5"][1]["action"]
            c.components.sound.play(actions)
            popmsg.add(actions, 5)
            c.components.battleroom_status.set_score(2)

        # CLOSED ROOM, OWNER
        if flag == 10:
            con.display_buttons = True
            con.FRAME = [3, 2]
            c.components.battleroom_status.reset_score()

        # CLOSED ROOM, GUEST
        if flag == 11:
            con.display_buttons = True
            con.FRAME = [3, 1]
            c.components.battleroom_status.reset_score()

        # COUNTER START EACH ROUND
        if flag == 17:
            msg = x["5"][1]["msg"]
            round = x["5"][2]["round"]

            c.components.battleroom_status.reset()
            c.components.battleroom_power.reset()
            c.components.battleroom_fighter1.reset()
            c.components.battleroom_fighter2.reset()

            c.components.sound.play(int(round))
            #c.components.timer.add(int(msg))

        # ROUND COUNTER AND ROUND NUMBER
        if flag == 18:
            msg = x["5"][1]["msg"]
            round = x["5"][2]["round"]

            c.components.sound.play(4)
            c.components.battleroom_counter2.set_round(round)
            c.components.timer2.add(int(msg))


    if "3" in x:
        flag = int(x["3"][0]["flag"])
        msg = x["3"][1]["msg"]

        # Created
        if flag == 1:
            #con.room_list = []
            con.FRAME = [3, 0]
            con.room_list = x["3"][2]["players"]

        # guest Left
        if flag == 3:
            c.components.gameroom_buton_ready.unready()
            con.display_buttons = True
            con.FRAME = [3, 0]
            con.room_list = x["3"][2]["players"]

        # Owner Left
        if flag == 4:
            c.components.gameroom_buton_ready.unready()
            con.FRAME = [2, 0]

        # Guest entered room
        if flag == 7:
            con.FRAME = [3, 0]

        # UPDATE FOR GUEST
        if flag == 10:
            con.display_buttons = True
            con.FRAME = [3, 1]
            con.room_list = x["3"][2]["players"]

        # UPDATE FOR OWNER
        if flag == 11:
            con.display_buttons = True
            con.FRAME = [3, 2]
            con.room_list = x["3"][2]["players"]
            c.components.battleroom_status.reset_score()

            if len(con.room_list) == 1:
                con.FRAME = [3, 0]


        # MSG TO OWNER, GUEST LEFT
        if flag == 12:
            con.FRAME = [3, 0]
            con.room_list = x["3"][2]["players"]
            c.components.battleroom_status.reset_score()

        # IN-GAME CHAT MSG + TIMER
        if flag == 20:
            con.FRAME = [3, 4]
            t = x["3"][2]["timer"]
            c.components.gameroom_chat_display.update("Server", msg)
            #c.components.gameroom_timer.add(int(t))

        if flag == 21:
            con.display_buttons = False
            con.FRAME = [3, 3]
            t = x["3"][2]["timer"]
            c.components.gameroom_chat_display.update("Server", msg)
            #c.components.gameroom_timer.add(int(t))

        # IN-GAME CHAT MSG
        if flag == 22:
            c.components.gameroom_chat_display.update("Server", msg)

        # BATTLE STARTED, MOVE TO NEXT SCENARIO
        if flag == 23:
            con.FRAME = [4, 0]

        # resetting
        if flag == 25:
            c.components.gameroom_buton_ready.unready()
            con.room_list = x["3"][2]["players"]

            if len(x["3"][2]["players"]) == 1:
                con.display_buttons = True
                con.FRAME = [3, 0]


        # READY INDIVIDUAL BUTTON
        if flag == 31:
            c.components.gameroom_buton_ready.unready()

        # UN-READY INDIVIDUAL BUTTON
        if flag == 32:
            c.components.gameroom_buton_ready.ready()

        # READY FOR EVERYONE
        if flag == 50:
            con.room_list = x["3"][2]["players"]

        # SEND CHARACTER ON EACH SIDE
        if flag == 60:
            img = x["3"][2]["image"]
            elements = x["3"][3]["elements"]
            c.components.battleroom_fighter1.set_character(img[0], elements[0])
            c.components.battleroom_fighter2.set_character(img[1], elements[1])
            c.components.battleroom_status.set_avatar(img[0], img[1])



        # SENDING ELEMENTS LIST
        if flag == 61:
            c.components.gameroom_select_element.selected_elements(x["3"][2]["elements"])

    # MSG FROM ABOVE, 500 USED FOR THE SERVER
    if "500" in x:
        popmsg.add(x["500"][0]["msg"], 5)

    # FROM NETWORK, GIVING SERVER STATUS
    if "-1000" in x:
        con.STATUS = x.get("-1000")

    # ACOUNT CREATED
    if "-99" in x and x["-99"][0]["flag"] == 1:
        con.FRAME = [2, 0]
        popmsg.add(x["-99"][1]["msg"], 5)

    # LOGIN
    if "-99" in x and x["-99"][0]["flag"] == 2:
        if d.check:
            d.save_user_info("True", c.components.login_nick.str, c.components.login_pass.str)
            con.FRAME = [2, 0]
        else:
            d.save_user_info("False", "", "")
        popmsg.add(x["-99"][1]["msg"], 5)

    # CREATING ACCOUNT: Error
    if "-99" in x and x["-99"][0]["flag"] == 3:
        popmsg.add(x["-99"][1]["msg"], 5)

    # UPDATING LOBBY
    if "0" in x:
        playerlist = x["0"][0]["players"]
        roomlist = x["0"][1]["rooms"]
        con.PLAYERS_ONLINE = len(playerlist)
        c.components.lobby_rooms_display.update(roomlist)
        c.components.lobby_players_display.update(playerlist)

    # 2 IS FOR CHAT MESSAGES IN LOBBY
    if "2" in x:
        c.components.lobby_chat_display.update(x["2"][0]["player"], x["2"][1][1])

    # 1 IS FOR CHAT MESSAGES IN GAMEROOM
    if "1" in x:
        c.components.gameroom_chat_display.update(x["1"][0]["player"], x["1"][1][1])



def validate(c, lista):
    popmsg = c.popmessage
    pass1 = None
    pass2 = None
    for item, value in lista.items():
        if len(value) > 5:
            if item == "password 1":
                pass1 = value
            if item == "password 2":
                pass2 = value
        else:
            popmsg.remove()
            popmsg.add(str(item) + " is too short", 5)
            return False

    if pass1 != pass2:
        popmsg.remove()
        popmsg.add("Passwords don't match!", 5)
        return False
    else:
        return True