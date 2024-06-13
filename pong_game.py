import turtle
import winsound
score_a=0
score_b=0
win=turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("pong game")
win.tracer(0) #rectangle not come in center
left_paddle=turtle.Turtle()
left_paddle.speed(0)  #no animaltion
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup() #line will noot display
left_paddle.goto(-380,0)

right_paddle=turtle.Turtle()
right_paddle.speed(0)  #no animaltion
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup() #line will noot display
right_paddle.goto(380,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=0.3
ball.dy=0.3
#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0",align="center",font=("Ariel",'24',"normal"))

def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)


win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')

while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    #bottom ball
    if ball.ycor() <- 290:
        ball.sety(-290)
        ball.dy *= -1
    #right wall
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b), align="center", font=("Ariel", '24', "normal"))

    #left wall
    if ball.xcor() < - 390:
        ball.setx(-390)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a, score_b), align="center", font=("Ariel", '24', "normal"))
        #collision with paddles
    if ball.xcor() > 370 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -370 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50:
        ball.setx(-360)
        ball.dx *= -1




