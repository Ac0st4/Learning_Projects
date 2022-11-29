#Today we are creating the old game of pong :D


#Getting started with the set up first
#-----------------------------------------------------------------------------------------------------------------
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)
#-------------------------------------------------------------------------------------------------------------------
# Score
score_a = 0
score_b = 0
#-----------------------------------------------------------------------------------------------------------------
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
#-----------------------------------------------------------------------------------------------------------------
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#-------------------------------------------------------------------------------------------------------------------
#Ball
ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07
#---------------------------------------------------------------------------------------------------------------
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0     Player B: 0", align="center", font=("Courier", 24, "normal"))

#-----------------------------------------------------------------------------------------------------------------
#Function paddle a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

#Function paddle b

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)
#--------------------------------------------------------------------------------------------
#Keyboard binding paddle a
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
#--------------------------------------------------------------------------------------------
#Keyboard binding paddle b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#--------------------------------------------------------------------------------------------

# Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 

    #Border checking Y
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wax", winsound.SND_ASYNC)

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wax", winsound.SND_ASYNC)


    #Border checking X
    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}     Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
         ball.dx *= -1
         winsound.PlaySound("bounce.wax", winsound.SND_ASYNC)

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wax", winsound.SND_ASYNC)
