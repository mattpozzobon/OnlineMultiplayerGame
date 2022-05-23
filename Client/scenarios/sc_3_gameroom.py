def background(c):
    c.components.backgroundlobby.render()
    c.components.lobby_chat_box.render()
    c.components.gameroom_chat_display.render()
    c.components.gameroom_timer.render()
    c.components.battleroom_counter.render(c.components.gameroom_timer.get())

def tab_kick(c):
    c.components.gameroom_buton_kick.render()

def start(c, conn):
    FRAME = conn.FRAME
    background(c)

    if conn.display_buttons:
        c.components.gameroom_right_panel.render()
        c.components.gameroom_buton_exit.render()

        if FRAME[1] >= 1:
            c.components.gameroom_buton_ready.render()

        if FRAME[1] == 2:
            tab_kick(c)


    if FRAME[1] == 3:
        c.components.gameroom_select_fighter.render()

    if FRAME[1] == 4:
        c.components.gameroom_select_element.render()