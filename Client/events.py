

def events(p, c, FRAME):

    for event in p.p.event.get():

        c.components.creativemode.event(event)

        if FRAME[0] == 1:
            c.components.tab_button_login.event(event)
            c.components.tab_button_account.event(event)
            c.components.tab_button_options.event(event)
            c.components.tab_button_exit.event(event)

            if FRAME[1] == 1:
                c.components.login_confirm.event(event)
                c.components.login_nick.event(event)
                c.components.login_pass.event(event)
                c.components.login_check_box.event(event)

            if FRAME[1] == 2:
                c.components.account_confirm.event(event)
                c.components.account_name.event(event)
                c.components.account_nick.event(event)
                c.components.account_pass1.event(event)
                c.components.account_pass2.event(event)

            if FRAME[1] == 3:
                c.components.options_resolution.event(event)

                c.components.options_input_ip.event(event)
                c.components.options_comfirm_ip.event(event)
                c.components.options_input_camera.event(event)
                c.components.options_comfirm_camera.event(event)

            if FRAME[1] == 4:
                c.components.video_fullscreen.event(event)
                c.components.video_1920x1080.event(event)
                c.components.video_1366x768.event(event)
                c.components.video_1200x800.event(event)
                c.components.video_1536x864.event(event)
                c.components.video_800x600.event(event)

        if FRAME[0] == 2:
            c.components.button_slide_logout.event(event)
            c.components.button_slide_users.event(event)
            c.components.button_slide_chat.event(event)
            c.components.button_slide_rooms.event(event)

            # logout
            c.components.lobby_logout_comfirm.event(event)
            c.components.lobby_logout_cancel.event(event)

            c.components.lobby_rooms_display.event(event)
            c.components.lobby_players_display.event(event)
            c.components.lobby_chat_display.event(event)

        if FRAME[0] == 3:
            c.components.gameroom_buton_exit.event(event)
            c.components.gameroom_chat_display.event(event)


            if FRAME[1] == 1:
                c.components.gameroom_buton_ready.event(event)

            if FRAME[1] == 2:
                c.components.gameroom_buton_kick.event(event)
                c.components.gameroom_buton_ready.event(event)

            if FRAME[1] == 3:
                c.components.gameroom_select_fighter.event(event)

            if FRAME[1] == 4:
                c.components.gameroom_select_element.event(event)

        if FRAME[0] == 4:
            c.components.battleroom_input.event(event)



        if event.type == p.p.MOUSEBUTTONDOWN:
            pass

        if event.type == p.p.MOUSEBUTTONUP:
            pass

        if event.type == p.p.KEYUP:
            pass

        if event.type == p.p.KEYDOWN:
            pass

        if event.type == p.p.QUIT:

            p.RUN = False

