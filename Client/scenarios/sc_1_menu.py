

def render_background(comps):
    comps.components.background.render()


def render_tab(comps):
    comps.components.tab_box_background.render()
    comps.components.tab_button_login.render()
    comps.components.tab_button_account.render()
    comps.components.tab_button_options.render()
    comps.components.tab_button_exit.render()


def render_login(comps):
    comps.components.header.render()
    comps.components.login_header.render()
    comps.components.login_box_main.render()
    comps.components.login_nick.render()
    comps.components.login_pass.render()
    comps.components.login_confirm.render()
    comps.components.login_check_box.render()


def render_account(comps):
    comps.components.header.render()
    comps.components.account_header_text.render()
    comps.components.account_box.render()
    comps.components.account_name.render()
    comps.components.account_nick.render()
    comps.components.account_pass1.render()
    comps.components.account_pass2.render()
    comps.components.account_confirm.render()


def render_options(comps):
    comps.components.header.render()
    comps.components.options_header_text.render()
    comps.components.options_box.render()
    comps.components.options_resolution.render()
    comps.components.options_input_ip.render()
    comps.components.options_comfirm_ip.render()
    comps.components.options_input_camera.render()
    comps.components.options_comfirm_camera.render()


def render_video(comps):
    comps.components.header.render()
    comps.components.video_header_text.render()
    comps.components.video_box.render()
    comps.components.video_fullscreen.render()
    comps.components.video_1920x1080.render()
    comps.components.video_1366x768.render()
    comps.components.video_1200x800.render()
    comps.components.video_1536x864.render()
    comps.components.video_800x600.render()


def render_client_version(comps):
    comps.components.box_client_version.render()
    comps.components.text_client_version.render()


def start(c, FRAME):
    render_background(c)
    render_tab(c)
    render_client_version(c)

    if FRAME[1] == 1:
        render_login(c)
    if FRAME[1] == 2:
        render_account(c)
    if FRAME[1] == 3:
        render_options(c)
    if FRAME[1] == 4:
        render_video(c)


















