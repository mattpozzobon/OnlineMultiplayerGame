
def background(c):
    c.components.backgroundbattle.render()
    c.components.battleroom_status.render()
    c.components.battleroom_fighter1.render(c.components.battleroom_fighter2.rect)
    c.components.battleroom_fighter2.render(c.components.battleroom_fighter1.rect)
    c.components.battleroom_power.render(c.components.battleroom_fighter1.rect, c.components.battleroom_fighter2.rect)
    c.components.battleroom_hands.render()

def start(c, FRAME):
    background(c)



