import turtle

s= turtle.Screen()
t= turtle.Turtle()

s.bgcolor('pink')

#8
t.pensize(15)
t.pencolor('red')
t.penup()
t.goto(0,200)
t.pendown()
t.left(90)
t.circle(30,360)

t.penup()
t.goto(-30,170)
t.pendown()
t.left(90)
t.circle(30,360)
t.penup()

#8
t.left(90)
t.goto(-60,30)
t.pendown()
t.circle(30,360)

t.penup()
t.goto(-30,-60)
t.pendown()
t.left(90)
t.circle(30,360)
t.penup()

#3
t.right(90)
t.goto(-40,-165)
t.pendown()
t.right(-90)
t.circle(30,180)
t.penup()
t.goto(-40,-227)
t.pendown()
t.right(180)
t.circle(30,180)
t.penup()

#c
t.goto(-150,55)
t.pendown()
t.circle(58,180)

#f
t.penup()
t.goto(100,55)
t.right(90)
t.pendown()
t.forward(116)
t.goto(100,55)
t.left(90)
t.forward(60)
t.penup()
t.goto(100,10)
t.pendown()
t.forward(60)
