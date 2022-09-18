#space invaders
#CODING BY SURYA
#set up the screen
import turtle
import os
import math
import random
import winsound
import pyglet

#animation = pyglet.image.load_animation('tenor.gif')
#animSprite = pyglet.sprite.Sprite(animation)
#w = animSprite.width
#h = animSprite.height

#window = pyglet.window.Window(width=w, height=h)

#@window.event
#def on_draw():
#   window.clear()
#   animSprite.draw()

#pyglet.app.run()
    







#set up the screen
ms=turtle.Screen()
ms.bgcolor("black")
ms.title("SPACE INVASION")
ms.bgpic("original.gif")

#register the shapes
turtle.register_shape("invader3.gif")
turtle.register_shape("player.gif")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#title
titl_pen = turtle.Turtle()
titl_pen.speed(0)
titl_pen.color("violet")
titl_pen.penup()
titl_pen.setposition(0, 300)
titlstring = "ALIEN INVASION"
titl_pen.write(titlstring, False, align = "center", font=("Courier New", 28, "normal"))
titl_pen.hideturtle()


#set the score to zero
score = 0

#show the score on the screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 300)
scorestring = "score: %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


#create the player turtle
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 18

#no of enemies
if score < 90:
    number_of_enemies = 10
elif score > 90:
    number_of_enemies = 13

#create a empty list of enemies
enemies = []

#add enemies to list
for i in range(number_of_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color("green")
    enemy.shape("invader3.gif")
    enemy.penup()
    enemy.speed(50)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


enemyspeed = 2


#Create the playe's bullet
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed=30

#define bullet state
#ready -ready to fire
#fire - bullet is fired
bulletstate = "ready"



#move the player left and right and up and down
#move player up
def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 280:
        y = 280
    player.sety(y)
#move player down
def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    player.sety(y)



#move player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
#move player right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bullet state as aglobal if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet above the player (just above the player)
        winsound.PlaySound("wiz.wav", winsound.SND_ASYNC)
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

    
#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")

#main gameloop
while True:
    if score < 90:
        number_of_enemies = 10
    elif score > 90:
        number_of_enemies = 13
    #winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move enemy back and down
        if enemy.xcor() > 280:
            #moves all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction    
            enemyspeed *= -1
        

        if enemy.xcor() < -280:
            #moves all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction      
            enemyspeed *= -1

        #check for collision btw bullet and enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("exp.wav", winsound.SND_ASYNC)
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #add score
            score += 10
            scorestring = "score: %s" %score
            score_pen.clear()
            if score < 90:
                score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
            elif score > 90:
                enemyspeed = 6
                score_pen.color("yellow")
                score_pen.write(scorestring, False, align="left", font=("Arial", 18, "normal"))
            elif score > 190:
                enemyspeed = 4
                score_pen.color("green")
                score_pen.write(scorestring, False, align="left", font=("Arial", 20, "normal"))
            
            



        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"   
        
        
