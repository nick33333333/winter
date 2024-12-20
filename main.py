import turtle

screen=turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("lightsteelblue")
t=turtle.Turtle()

t_ground=turtle.Turtle()
t_ground.penup()
t_ground.pencolor("snow1")
t_ground.fillcolor("snow1")
t_ground.speed(0)
t_ground.begin_fill()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()
t.penup()

t.fillcolor('sienna')
t.speed(0)

t.goto(-100,-100)
t.pendown()
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(30)
t.left(90)
t.forward(300)
t.left(90)
t.forward(30)
t.end_fill()

t.fillcolor('chocolate')


t.penup()
t.goto(-100,-39)
t.pendown()
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(300)
t.left(90)
t.forward(30)
t.left(90)
t.forward(300)
t.end_fill()

t.fillcolor('sienna')


t.penup()
t.goto(200,-10)
t.pendown()
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(30)
t.left(90)
t.forward(300)
t.left(90)
t.forward(30)
t.end_fill()

t.fillcolor('chocolate')


t.penup()
t.goto(200,-10)
t.pendown()
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(300)
t.left(90)
t.forward(30)
t.left(90)
t.forward(300)
t.end_fill()

t.fillcolor('sienna')

t.penup()
t.goto(-100,20)
t.pendown()
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(30)
t.left(90)
t.forward(300)
t.left(90)
t.forward(30)
t.end_fill()

t.fillcolor('chocolate')

t.penup()
t.goto(-100,80)
t.pendown()
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(300)
t.left(90)
t.forward(30)
t.left(90)
t.forward(300)
t.end_fill()

t.fillcolor('sienna')

t.goto(-100,80)

t.pendown()
t.begin_fill()
t.goto(200,80)
t.goto(50,140)
t.goto(-100,80)
t.end_fill()
t.penup()
t.goto(-200,-200)
t.pendown()


t.fillcolor('snow1')
t.begin_fill()
t.circle(50)
t.penup()
t.end_fill()

t.goto(-200,-140)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
#head
t.goto(-200,-100)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

t.pensize(5)
t.penup()
t.goto(-185,-120)
t.dot()
t.penup()
t.goto(-215,-120)
t.dot()

t.pensize(1)

t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.goto(-200,-130)
t.goto(-200,-130)
t.goto(-150,-140)
t.end_fill()
t.penup()
t.goto(-230,-140)
t.end_fill()
t.pendown()
t.end_fill()

t.hideturtle()

t.fillcolor("snow1")
t.begin_fill()
t.penup()
t.goto(-200,350)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.goto(-170,350)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.goto(-140,350)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(-150,300)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(-180,300)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(-110,350)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(-240,350)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(-210,400)
t.pendown()
t.circle(50)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(-180,380)
t.pendown()
t.circle(50)
t.end_fill()



t.fillcolor("gold")
t.begin_fill()
t.penup()
t.goto(500,450)
t.pendown()
t.circle(100)
t.end_fill()


t.penup()
t.hideturtle()
t.speed(0)
t.pensize(20)
t.pencolor('brown')
t.setheading(90)
t.penup()
t.goto(-200,-95)
t.pendown()
t.forward(50)
t.pensize(15)
t.penup()
t.goto(-200,100)
t.setheading(0)
t.pendown()
t.pencolor('darkolivegreen')
t.fillcolor("darkolivegreen")
t.begin_fill()
t.goto(-250,-50)
t.goto(-150,-50)
t.goto(-200,100)
t.end_fill()

t.write("Happy Holidays", font=("arial", 30, "bold"), align="center")

#this is the last line of code
turtle.done()























