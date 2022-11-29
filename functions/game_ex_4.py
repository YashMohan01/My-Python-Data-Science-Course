import pgzrun

WIDTH = 1200
HEIGHT = 600

scr = 0

def gamescr(title,bgcolor="gray",info="Play the game"):
    screen.fill(bgcolor)
    screen.draw.text(title , center = (WIDTH/2 ,HEIGHT/2), fontsize= 100, color='white', align="center")
    screen.draw.text(info ,center =  (WIDTH/2, HEIGHT/2+100), fontsize= 50, color='white', align="center")

def draw():
    if scr==0:
        gamescr("Amazing Game","black","Press Space to Start")
    elif scr==1:
        gamescr(bgcolor="blue",title ="Game is Running")
    elif scr==2:
        gamescr("Game-Over",info ="go home")

        

def update():
    global scr 
    if keyboard.SPACE and scr==0:
        scr=1
    elif keyboard.ESCAPE and scr==1:
        scr=2
    elif keyboard.RETURN and scr==2:
        scr=0
    print(scr)

pgzrun.go()