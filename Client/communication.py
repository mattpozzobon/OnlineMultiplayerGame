
def communication(conn, net, app):
    if app is not None:
        if not app.HASWEBCAM.empty():
            msg = app.HASWEBCAM.get()
            conn.HASWEBCAM = msg

        if not app.RECEIVE.empty():
            msg = app.RECEIVE.get()
            conn.FROMHANDGESTURE(msg)

    if net is not None:
        if len(conn.TOSERVER) != 0:
            msg = conn.TOSERVER.pop()
            print("TOSERVER: " + str(msg))
            net.q_SEND.put(msg)

        if not net.q_RECEIVE.empty():
            msg = net.q_RECEIVE.get()
            print("FROMSERVER: " + str(msg))
            conn.FROMSERVER(msg)

        if not net.q_STATUS.empty():
            msg = net.q_STATUS.get()
            print("SERVER STATUS: " + str(msg))
            conn.FROMSERVER(msg)