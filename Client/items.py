

def items(p, c, con):

    c.components.popmessage.render()

    if con.FRAME[0] == 2:
        c.components.tabplayersonline.render("Players Online: " + str(con.PLAYERS_ONLINE))

    if con.FRAME == [4, 0]:
        c.components.timer.render()
        c.components.timer2.render()
        c.components.battleroom_counter.render(c.components.timer.get())
        c.components.battleroom_counter2.render(c.components.timer2.get())
    else:
        #c.components.creativemode.render()

        c.components.tabcamera.render(con.HASWEBCAM)
        c.components.tabserver.render(con.STATUS)
        c.components.tabfps.render(p.clock.get_fps())


    p.clock.tick(p.FPS)
    p.p.display.update()

