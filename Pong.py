import turtle
wn= turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
scor_a,scor_b=0,0
p_A=turtle.Turtle()
p_A.speed(0)
p_A.shape("square")
p_A.color("white")
p_A.shapesize(stretch_wid=5, stretch_len=1)
p_A.penup()
p_A.goto(-350,0)
p_B=turtle.Turtle()
p_B.speed(0)
p_B.shape("square")
p_B.color("white")
p_B.shapesize(stretch_wid=5, stretch_len=1)
p_B.penup()
p_B.goto(350,0)
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2
s_scor=turtle.Turtle()
s_scor.speed(0)
s_scor.color('white')
s_scor.penup()
s_scor.hideturtle()
s_scor.goto(0,260)
s_scor.write("Player A:0  Player B:0",align="center", font=("Courier",24,"normal"))
def left_up():
    y=p_A.ycor()
    y+=20
    p_A.sety(y)
def left_down():
    y=p_A.ycor()
    y-=20
    p_A.sety(y)
def right_up():
    y=p_B.ycor()
    y+=20
    p_B.sety(y)
def right_down():
    y=p_B.ycor()
    y-=20
    p_B.sety(y)
wn.listen()
wn.onkeypress(left_up,"w")
wn.onkeypress(left_down,"s")
wn.onkeypress(right_up,"Up")
wn.onkeypress(right_down,"Down")
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.dy *=-1
    if ball.ycor()<-290:
        ball.dy *=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        scor_a+=1
        s_scor.clear()
        s_scor.write("Player A:{}  Player B:{}".format(scor_a,scor_b),align="center", font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        scor_b+=1
        s_scor.clear()
        s_scor.write("Player A:{}  Player B:{}".format(scor_a,scor_b),align="center", font=("Courier",24,"normal"))
    if (ball.xcor()>340 and ball.xcor()<350)and (ball.ycor()<p_B.ycor()+50 and ball.ycor()>p_B.ycor()-50):
        ball.setx(340)
        ball.dx *=-1
    if (ball.xcor()<-340 and ball.xcor()>-350)and (ball.ycor()<p_A.ycor()+50 and ball.ycor()>p_A.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1