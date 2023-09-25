import turtle
import os
import keyboard as k
import math
import time as t

win = turtle.Screen()
win2 = 0
win.setup(width=645, height=529)
win.bgpic("images/bg.gif")
win.title("Space Point Plotter")
man = turtle.Turtle()
manpos = turtle.Turtle()
readoutdisplay = turtle.Turtle()
textManager = turtle.Turtle()
movingState = turtle.Turtle()
offscreenState = turtle.Turtle()
manpos.color('red')
manpos.shape("arrow")
win.bgcolor('black')
man.penup()
manpos.penup()
readoutdisplay.penup()
textManager.penup()
movingState.penup()
movingState.speed(0)
movingState.setx(-210)
movingState.sety(250)
offscreenState.penup()
offscreenState.speed(0)
offscreenState.setx(-190)
offscreenState.sety(250)
readoutdisplay.speed(0)
textManager.speed(0)
textManager.color("white")
textManager.hideturtle()
readoutdisplay.setx(-250)
readoutdisplay.sety(200)
textx = -300
texty = 240
textManager.setx(textx)
textManager.sety(texty)
running = True
manx = man.xcor()
many = man.ycor()

#fuck registering shapes
player = "images/ship.gif"
readout = "images/readout.gif"
indicatoroff = "images/lightidle.gif"
indicatoron = "images/lighton.gif"
switchoff = "images/button.gif"
switchon = "images/buttonpressed.gif"

turtle.register_shape(player)
turtle.register_shape(readout)
turtle.register_shape(indicatoroff)
turtle.register_shape(indicatoron)
turtle.register_shape(switchoff)
turtle.register_shape(switchon)
man.shape(player)
readoutdisplay.shape(readout)
movingState.shape(indicatoroff)
offscreenState.shape(indicatoroff)
#to the professionals reading this about to make a git commit--
#i understand this is bad practice, but it's 4am on a school night
#and frankly my patience is thinner than graphene right now

def backgroundLoop():
    var2 = tim2
    for i in range(tim2):
        win2.bgpic("images/sprite_0.gif")
        win2.update()
        t.sleep(0.5)
        win2.bgpic("images/sprite_1.gif")
        win2.update()
        t.sleep(0.5)
        win2.bgpic("images/sprite_2.gif")
        win2.update()
        t.sleep(0.5)
        win2.bgpic("images/sprite_3.gif")
        win2.update()
        t.sleep(0.5)
        os.system('cls')
        print("Ship is plotted at X" + str(manx) + " && Y" + str(many) + ".")
        print("It will take " + str(tim) + " minutes to get here.")
        print("Time Passed: " + str(i) + " minutes")

def travelSequence():
    win.bye()
    global win2
    win2 = turtle.Screen()
    backgroundLoop()
    t.sleep(1)
    print("ekfugusgf")
    

def handlePlotting(x, y):
    global manx
    global many
    manx = man.xcor()
    many = man.ycor()
    print("Ship is plotted at X" + str(manx) + " && Y" + str(many) + ".")
    divider = manx * many + 12
    if many == 0:
        many += 13
    if manx == 0:
        manx += 13
    global tim
    tim = abs(divider/4) * 0.4
    print("It will take " + str(tim) + " minutes to get here.")
    global tim2
    tim2 = int(tim) * 8
    running = False
    travelSequence()
    
def movementHandling():
    shipx = manpos.xcor()
    shipy = manpos.ycor()
    textManager.clear()
    textManager.write("X: " + str(round(man.xcor())))
    textManager.sety(195)
    textManager.write("Y: " + str(round(man.ycor())))
    textManager.sety(240)
    man.forward(7)
    manpos.forward(7)
    if shipx > 315:
        offscreenState.shape(indicatoron)
        textManager.setx(-170)
        textManager.write("Unknown Territory Warning!")
        textManager.setx(-300)
    else:
        offscreenState.shape(indicatoroff)
        
    if shipy > 250:
        offscreenState.shape(indicatoron)
        textManager.setx(-170)
        textManager.write("Unknown Territory Warning!")
        textManager.setx(-300)
    else:
        offscreenState.shape(indicatoroff)

while running == True:
    
    if k.is_pressed("d"):
        man.left(7)
        manpos.left(7)
    if k.is_pressed("a"):
        man.right(7)
        manpos.right(7)
        
    if k.is_pressed("w"):
        movingState.shape(indicatoron)
        movementHandling()
    else:
        movingState.shape(indicatoroff)
    manpos.onclick(handlePlotting)