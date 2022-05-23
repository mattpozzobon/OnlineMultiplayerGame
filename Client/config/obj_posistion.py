print("+ = "+__name__)


class Load():
    def __init__(self, pyga):
        W = pyga.SIZE[0]
        H = pyga.SIZE[1]


        # [1,0] BACKGROUND2
        self.background_menu =                  (W*0.27917,  H*0.91875, W*0.44167,  H*0.12500)

        # [1,0] PING AND FPS AND VERSION
        self.players_online_pos =               (W * 0.8216,  H*0.07575, W*0.13500,  H * 0.025)

        self.online_words_pos =                 (W * 0.93, H * 0.013)
        self.status_words_pos =                 (W * 0.857, H * 0.013)

        self.fps =      (W * 0.92, H * 0.013, W * 0.045, H * 0.045)
        self.server =   (W * 0.87, H * 0.013, W * 0.045, H * 0.045)
        self.camera =   (W * 0.82, H * 0.013, W * 0.045, H * 0.045)


        self.box_client_version_pos =           (W*0.96083,  H*0.96375, W*0.03833,  H*0.03500)

        # [1,3] OPTIONS
        self.options_box =                      (W*0.35000,  H*0.25000, W*0.30000,  H*0.55000)
        self.options_resolution = (W * 0.38833, H * 0.28625, W * 0.23333, H * 0.08000)

        self.input_ip = (W*0.38917,  H*0.40750, W*0.19500,  H*0.06000)
        self.comfirm_ip = (W*0.58417,  H*0.41500, W*0.04000,  H*0.05250)
        self.input_camera = (W*0.38917,  H*0.48750, W*0.19500,  H*0.06000)
        self.comfirm_camera = (W*0.58417,  H*0.49500, W*0.04000,  H*0.05250)



        # [1,0] TAB
        self.tab_box_background_pos  =          (W*0.27917,  H*0.91875, W*0.44167,  H*0.12500)
        self.tab_button_login_pos  =            (W*0.29500,  H*0.94000, W*0.10000,  H*0.05000)
        self.tab_button_account_pos  =          (W*0.39500,  H*0.94000, W*0.10000,  H*0.05000)
        self.tab_button_options_pos  =          (W*0.49500, H*0.94000, W*0.10000,  H*0.05000)
        self.tab_button_exit_pos =              (W*0.59500, H*0.94000, W*0.10000,  H*0.05000)

        # [1,1]
        self.header =                           (W*0.35000,  H*0.12000, W*0.30000,  H*0.10000)
        self.login_box_main_pos =               (W*0.35000,  H*0.25000, W*0.30000,  H*0.25000)
        self.login_input_nickname_pos =         (W*0.40000,  H*0.27500, W*0.20000,  H*0.05625)
        self.login_input_password_pos =         (W*0.40000,  H*0.33500, W*0.20000,  H*0.05625)
        self.login_button_confirm_login_pos =   (W*0.40000,  H*0.40500, W*0.17000,  H*0.05625)
        self.login_check_box_pos =              (W*0.57000,  H*0.41500, W*0.03000,  H*0.03000)
        self.box_info_pos =                     (W*0.85333,  H*0.12150, W*0.21250,  H*0.81875)

        # [1,2]
        self.account_menu =                     (W*0.35000,  H*0.25000, W*0.30000,  H*0.35000)
        self.account_box_pos =                  (W*0.35000,  H*0.25000, W*0.30000,  H*0.40000)
        self.account_name_pos =                 (W*0.40000,  H*0.27500, W*0.20000,  H*0.05625)
        self.account_nick_pos =                 (W*0.40000,  H*0.33500, W*0.20000,  H*0.05625)
        self.account_pass1_pos =                (W*0.40000,  H*0.39500, W*0.20000,  H*0.05625)
        self.account_pass2_pos =                (W*0.40000,  H*0.45500, W*0.20000,  H*0.05625)
        self.account_confirm_pos =              (W*0.40000,  H*0.52500, W*0.20000,  H*0.05625)

        # [1, 3]
        self.video_box_pos =                    (W*0.35000,  H*0.25000, W*0.30000,  H*0.41000)
        self.video_fullscreen_pos =             (W*0.37583,  H*0.26875, W*0.24917,  H*0.04500)
        self.video_1920x1080_pos =              (W*0.37583,  H*0.33250, W*0.24917,  H*0.04500)
        self.video_1536x864_pos =               (W*0.37583,  H*0.39625, W*0.24917,  H*0.04500)
        self.video_1366x768_pos =               (W*0.37583,  H*0.46000, W*0.24917,  H*0.04500)
        self.video_1200x800_pos =               (W*0.37583,  H*0.52375, W*0.24917,  H*0.04500)
        self.video_800x600_pos  =               (W*0.37583,  H*0.58750, W*0.24917,  H*0.04500)

        # [2, 0]
        self.lobby_logout =                     (W*0.00000,  H*0.10750, W*0.03500,  H*0.0750)
        self.lobby_players =                    (W*0.00000,  H*0.26750, W*0.03500,  H*0.0750)
        self.lobby_rooms =                      (W*0.00000,  H*0.18750, W*0.03500,  H*0.0750)
        self.lobby_chat =                       (W*0.00000,  H*0.34750, W*0.03500,  H*0.0750)

        # Logout
        self.lobby_logout_box_pos =             (W*0.14333,  H*0.10750, W*0.90500,  H*0.0750)
        self.lobby_logout_comfirm_pos =         (W*0.15500,  H*0.11500, W*0.15000,  H*0.0550)
        self.lobby_logout_cancel_pos =          (W*0.31500,  H*0.11500, W*0.15000,  H*0.0550)

        # Rooms
        self.lobby_rooms_box_pos =              (W*0.14333,  H*0.18750, W*0.68833,  H*0.49500)

        # Players
        self.lobby_players_box_pos =            (W*0.83250,  H*0.18750, W*0.17000,  H*0.81125)

        # Chat
        self.lobby_chat_box_pos =               (W*0.14333,  H*0.68750, W*0.48833,  H*0.32000)

        # [3, 0]
        self.gameroom_buton_exit =              (W*0.82583,  H*0.92375, W*0.15667,  H*0.06250)
        self.gameroom_buton_ready =             (W*0.82583,  H*0.81875, W*0.15667,  H*0.06250)
        self.gameroom_buton_kick =              (W*0.82583,  H*0.71375, W*0.15667,  H*0.06250)

        # [3, 0] PANELS
        self.gameroom_left_panel =  (W*0.00000,  H*0.18875, W*0.12583,  H*0.31000)
        self.gameroom_right_panel = (W*1.00000-(W*0.12583), H*0.18875, W*0.12583, H*0.31000)



        # [4, 0]
        self.fighter1_pos =                     (W*0.10000,  H*0.67125, W*0.08000,  H*0.25625)
        self.fighter2_pos =                     (W*0.82000,  H*0.67125, W*0.08000,  H*0.25625)

print("- = "+__name__)