import turtle
import winsound

wn = turtle.Screen()
wn.title("Avihay&Idan Game")
wn.bgcolor("black")
wn.setup(width =800, height= 600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0





#paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)



#paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24, "normal"))



# Function (for movement of paddels)
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_a_right():
    x=paddle_a.xcor()
    x+=20
    paddle_a.setx(x)

def paddle_a_left():
    x=paddle_a.xcor()
    x-=20
    paddle_a.setx(x)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

def paddle_b_right():
    x=paddle_b.xcor()
    x+=20
    paddle_b.setx(x)

def paddle_b_left():
    x=paddle_b.xcor()
    x-=20
    paddle_b.setx(x)


#keyboard binding with listeners

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_right, "Right")
wn.onkeypress(paddle_b_left, "Left")




# main game loop
while True:
    wn.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
      # if you want it to bounce off everything: ball.setx(390)
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "normal"))
        winsound.PlaySound("wow.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
      #  ball.setx(-390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("wow.wav", winsound.SND_ASYNC)

    if (ball.xcor() > paddle_b.xcor() and ball.xcor() < (paddle_b.xcor()+20)) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor()> paddle_b.ycor() -40):
        ball.setx(paddle_b.xcor()-20)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < paddle_a.xcor() and ball.xcor() > (paddle_a.xcor() -20)) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor()> paddle_a.ycor() -40):
        ball.setx(paddle_a.xcor()+20)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # AI Player - in case you want it rather than multiplayer- can change the terms of AI
    # if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor()-ball.ycor()) > 10:
    #     paddle_b_up()
    #
    # elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor()-ball.ycor()) > 10:
    #     paddle_b_down()