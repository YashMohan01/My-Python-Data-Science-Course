import pgzrun
HEIGHT = 300
WIDTH = 800
p = Actor('ironman', (100,100))
c = Actor('cookie')

def draw():
    screen.fill("white")
    p.draw()
    c.draw()

def update():
    p.x +=1
    p.angle = -10
    if p.x > WIDTH:
        p.x = 0
    print(p.x,p.y)

pgzrun.go()