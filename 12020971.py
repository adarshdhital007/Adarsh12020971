#created by Adarsh
#importing libraries
import turtle
import time
import random

#Score
score = 0
high_score = 0
delay=0.1

#screen
screen = turtle.Screen()
screen.title("SnakeGame-ad007")
screen.bgpic("hehe.gif")
screen.setup(width=600, height=600) #Pixels
screen.tracer(0) #turns off the animation on screen/turns off the screen object

#Creating a snake head and moving it
head = turtle.Turtle()
head.speed(0) #Animation speed of the turtle module and maximum speed is zero
head.shape("square")
head .color("yellow")
head.penup() #Turtle module is used to draw,We did this so that it does not draw anything
head.goto(0,0) #so that it starts at centre
head.direction = "stop" #so that when it starts it will sit there in the middle with head up

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food .color("red")
food.penup()
food.goto(0,100)

# increasing the snake body
segments = []

#Pen
score=0
high_score=0
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0  Highscore  : 0" , align="center",font=("Courier",24,"normal"))



#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "down":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y + 20) #So if head is up then it will move 20 coordinates up

    if head.direction == "down":
        y=head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x + 20)

#Keyboard Bindings

screen.listen()
screen.onkeypress(go_up , "Up")
screen.onkeypress(go_down , "Down")
screen.onkeypress(go_left , "Left")
screen.onkeypress(go_right , "Right")
#Main Game loop
while True:
    screen.update() #so everytime the screen gets updated

    #Check for a collision of head with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1) #Pause the game for a second
        head.goto(0, 0)
        head.direction = "stop"
        #Hide the segments due to collision
        for segment in segments:
            segment.goto(1000, 1000) #We are just sending the segments away from screen
        #Clear the segments
        segments = []

        #Reset the Score
        score = 0
        pen.clear()
        pen.write("Score= {}  Highscore= {}".format(score, high_score), align="center",font=("Courier",24,"normal"))

#Check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot on the screen
        x=random.randint(-290, 290)#Because sccreen is divided in 300 half of the x and y diretion i.i. 600/2
        y = random.randint(-290, 290)
        food.goto(x, y)
        #here we are adding a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

        #Increase the Score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score= {}  Highscore= {}".format(score, high_score), align="center",font=("Courier",24,"normal"))

    #for moving the segments first in reverse order
    for index in range(len(segments)-1,0,-1):#it is working only when there more then 1 segments
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move the segment zero to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    #here we check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #we hide the segments due to collision
            for segment in segments:
                segment.goto(1000, 1000) #we are just sending the segments away from screen
            #Clear the segments
            segments = []
    time.sleep(delay) #stops the program by 0.1 seconds
