def background(c):
    c.components.backgroundlobby.render()


def tab_logout(c):
    c.components.lobby_logout_box.render()
    c.components.lobby_logout_comfirm.render()
    c.components.lobby_logout_cancel.render()


def tab_players(c):
    c.components.lobby_players_display.render()


def tab_chat(c):
    c.components.lobby_chat_box.render()
    c.components.lobby_chat_display.render()


def tab_rooms(c):
    c.components.lobby_rooms_box.render()
    c.components.lobby_rooms_display.render()


def buttons(c):
    c.components.button_slide_logout.render()
    c.components.button_slide_users.render()
    c.components.button_slide_chat.render()
    c.components.button_slide_rooms.render()


def start(c, con):
    background(c)

    if 1 in con.FRAME_LOBBY:
        tab_logout(c)
    if 2 in con.FRAME_LOBBY:
        tab_players(c)
    if 3 in con.FRAME_LOBBY:
        tab_chat(c)
    if 4 in con.FRAME_LOBBY:
        tab_rooms(c)

    buttons(c)