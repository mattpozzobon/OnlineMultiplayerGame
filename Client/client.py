print("+ = "+__name__)
from multiprocessing import freeze_support
import sys
import threading
from hand import app as hand
from network import load_network
from config import load_config
from config import load_pygame, obj_groups, obj_connect
from events import events
from switch import switch
from items import items
from action import action, receive
from communication import communication


def main():
    p = load_pygame.Load(data)
    conn = obj_connect.Load()
    objs = obj_groups.Load(data, p, conn)

    while True:
        communication(conn, net, app)
        switch(objs, conn)
        events(p, objs, conn.FRAME)

        action(p, objs, data, conn, net)
        receive(p, objs, data, conn)

        items(p, objs, conn)

        if not p.RUN:
            app.end()
            net.end()
            break

    sys.exit()


print("- = "+__name__)

if __name__ == '__main__':
    freeze_support()

    data = load_config.Load()
    app = hand.Load(data.getcamera())
    net = load_network.Load(data.getip())

    x = threading.Thread(target=app.start, args=())
    y = threading.Thread(target=net.start, args=())
    z = threading.Thread(target=main, args=())

    z.start()
    x.start()
    y.start()



