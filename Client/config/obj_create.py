print("+ = "+__name__)

from Client.components.background import Background
from Client.components.inputstr import InputStr
from Client.components.popup_message import PopUpMessage
from Client.components.text import Text
from Client.components.checkbox import CheckBox
from Client.components.box import Box
from Client.components.box2 import Box2
from Client.components.button import Button
from Client.components.creativemode import CreativeMode
from Client.components.tab_fps import TabFPS
from Client.components.tab_online import TabOnline
from Client.components.button_slide import ButtonSlide
from Client.components.background_lobby import BackgroundLobby
from Client.components.display_rooms import DisplayRooms
from Client.components.display_players import DisplayPlayers
from Client.components.tab_playrsonline import TabPlayersOnline
from Client.components.chat import Chat
from Client.components.counter import Counter
from Client.components.fighter import Fighter
from Client.components.timer import Timer
from Client.components.battleinput import BattleRoomInput
from Client.components.power import Power
from Client.components.fighter_status import Status
from Client.components.fighter_hands import DisplayHands
from Client.components.select_fighter import SelectFighter
from Client.components.select_element import SelectElement
from Client.components.tab_camera import TabCamera

class Load():
    def __init__(self, info):
        #([pyga, self.positions, self.images, data])
        pos = info[1]
        self.data = info[3]
        self.W = info[0].W
        self.H = info[0].H

        # [1,0]
        self.box_client_version =    Box(info, pos.box_client_version_pos, 255, border_round=0)
        self.text_client_version =   Text(info, "v1.0", pos.box_client_version_pos, 12)

        # [1,0] TAB BUTTONS
        self.tab_box_background =    Box(info, pos.tab_box_background_pos, 200)
        self.tab_button_login =      Button(info, pos.tab_button_login_pos, "Login", "login_tab_button")
        self.tab_button_account =    Button(info, pos.tab_button_account_pos, "Account", "account_tab_button")
        self.tab_button_options =    Button(info, pos.tab_button_options_pos, "Options", "options_tab_button")
        self.tab_button_exit    =    Button(info, pos.tab_button_exit_pos, "Exit", "exit_tab_button")

        # [1,1] RENDER LOGIN
        self.header = Box(info, pos.header, 200) # Shared
        self.login_header = Text(info, "Login", pos.header, 24)
        self.login_box_main = Box(info, pos.login_box_main_pos, 200)
        self.login_nick = InputStr(info, pos.login_input_nickname_pos, "Nickname", "login_nick")
        self.login_pass = InputStr(info, pos.login_input_password_pos, "Password", "login_pass", protect=True)
        self.login_confirm = Button(info, pos.login_button_confirm_login_pos, "Confirm", "login_confirm")
        self.login_check_box = CheckBox(info, pos.login_check_box_pos)

        # [1,2] CREATE ACCOUNT
        self.account_header_text = Text(info, "Create Account", pos.header, 24)
        self.account_box = Box(info, pos.account_box_pos, 200)
        self.account_box_info = Box(info, pos.box_info_pos, 200)
        self.account_name = InputStr(info, pos.account_name_pos, "Name", "account_name")
        self.account_nick = InputStr(info, pos.account_nick_pos, "Nickname", "account_nick")
        self.account_pass1 = InputStr(info, pos.account_pass1_pos, "Password", "account_pass1", protect=True)
        self.account_pass2 = InputStr(info, pos.account_pass2_pos, "Confirm Password", "account_pass2", protect=True)
        self.account_confirm = Button(info, pos.account_confirm_pos, "Confirm", "account_confirm")

        # [1,3] OPTIONS
        self.options_header_text = Text(info, "Options", pos.header, 24)
        self.options_box = Box(info, pos.options_box, 200)
        self.options_resolution = Button(info, pos.options_resolution, "Video", "video_options")

        self.options_input_ip =             InputStr(info, pos.input_ip, self.data.getip(), "input_ip")
        self.options_comfirm_ip =           Button(info, pos.comfirm_ip, "ok", "comfirm_ip")
        self.options_input_camera =         InputStr(info, pos.input_camera, str(self.data.getcamera()), "input_camera")
        self.options_comfirm_camera =       Button(info, pos.comfirm_camera, "ok", "comfirm_camera")



        # [1, 4] VIDEO OPTIONS
        self.video_header_text = Text(info, "Video Options", pos.header, 24)
        self.video_box = Box(info, pos.video_box_pos, 200)
        self.video_fullscreen = Button(info, pos.video_fullscreen_pos, "fullscreen", "fullscreen")
        self.video_1920x1080 = Button(info, pos.video_1920x1080_pos, "1920x1080", "1920x1080")
        self.video_1536x864 = Button(info, pos.video_1536x864_pos, "1536x864", "1536x864")
        self.video_1366x768 = Button(info, pos.video_1366x768_pos, "1366x768", "1366x768")
        self.video_1200x800 = Button(info, pos.video_1200x800_pos, "1200x800", "1200x800")
        self.video_800x600 = Button(info, pos.video_800x600_pos, "800x600", "800x600")

        # [2, 0] LOBBY
        self.button_slide_logout =      ButtonSlide(info, pos.lobby_logout, "Logout", "lobby_logout", info[2].img_lobby_logout)
        self.button_slide_users =       ButtonSlide(info, pos.lobby_players, "Players", "lobby_users", info[2].img_lobby_users)
        self.button_slide_chat =        ButtonSlide(info, pos.lobby_chat, "Chat", "lobby_chat", info[2].img_lobby_chat)
        self.button_slide_rooms =       ButtonSlide(info, pos.lobby_rooms, "Rooms", "lobby_rooms", info[2].img_lobby_rooms)

        # [2, 1] LOBBY LOGOUT
        self.lobby_logout_box =         Box(info, pos.lobby_logout_box_pos, 150, border_round=0)
        self.lobby_logout_comfirm =     Button(info, pos.lobby_logout_comfirm_pos, "Comfirm", "comfirm_logout")
        self.lobby_logout_cancel =      Button(info, pos.lobby_logout_cancel_pos, "Cancel", "cancel_logout")

        # [2, 2] LOBBY PLAYERS
        self.lobby_players_box =        Box(info, pos.lobby_players_box_pos, 150, border_round=0)
        self.lobby_players_display =    DisplayPlayers(info, pos.lobby_players_box_pos)

        # [2, 3] LOBBY CHAT
        self.lobby_chat_box =           Box(info, pos.lobby_chat_box_pos, 150, border_round=0)
        self.lobby_chat_display =       Chat(info, pos.lobby_chat_box_pos, "lobbychat", 2)

        # [2, 4] LOBBY ROOMS
        self.lobby_rooms_box =          Box(info, pos.lobby_rooms_box_pos, 150, border_round=0)
        self.lobby_rooms_display =      DisplayRooms(info, pos.lobby_rooms_box_pos)

        # [3, 0]
        self.gameroom_buton_exit =      Button(info, pos.gameroom_buton_exit, "Exit", "gameroomexit")
        self.gameroom_buton_ready =     Button(info, pos.gameroom_buton_ready, "Ready", "readyformatch")
        self.gameroom_buton_kick =      Button(info, pos.gameroom_buton_kick, "Kick", "kickplayerout")
        self.gameroom_chat_display =    Chat(info, pos.lobby_chat_box_pos, "roomchat", 1)

        self.gameroom_right_panel =     Box2(info, pos.gameroom_right_panel)
        self.gameroom_select_fighter =  SelectFighter(info)
        self.gameroom_select_element =  SelectElement(info)
        self.gameroom_timer =           Timer(info)

        # [4, 0]
        self.timer = Timer(info)
        self.timer2 = Timer(info)
        self.battleroom_counter = Counter(info)
        self.battleroom_counter2 = Counter(info)

        self.battleroom_power = Power(info)
        self.battleroom_status = Status(info)
        self.battleroom_fighter1 = Fighter(info, self.battleroom_power, pos.fighter1_pos, "left")
        self.battleroom_fighter2 = Fighter(info, self.battleroom_power, pos.fighter2_pos, "right")
        self.battleroom_input = BattleRoomInput(info, self.timer2)
        self.battleroom_hands = DisplayHands(info)

        import random
        # BACKGROUNDS
        self.background =               BackgroundLobby(info, 2)
        self.backgroundlobby =          BackgroundLobby(info, 1)
        self.backgroundbattle =         BackgroundLobby(info, int(random.uniform(5, 8)))

        # MISC
        self.popmessage = PopUpMessage(info)
        self.creativemode = CreativeMode(info)
        self.sound = info[5]


        self.tabplayersonline = TabPlayersOnline(info)

        self.tabserver = TabOnline(info, pos.server)
        self.tabcamera = TabCamera(info, pos.camera)
        self.tabfps = TabFPS(info, pos.fps)


print("+ - "+__name__)