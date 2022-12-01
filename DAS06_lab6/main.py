import turtle

t = turtle.Pen()
turtle.Screen().bgcolor("black")

t.fillcolor("#E0E7E0")
t.begin_fill()
t.circle(100)
t.end_fill()

t.up()
t.goto(-50, 20)

t.fillcolor("black")
t.begin_fill()
t.down()
t.circle(80)
t.end_fill()

t.fillcolor("#E0E7E0")
t.up()
t.goto(35, 105)
t.down()

t.pencolor('#E0E7E0')
t.begin_fill()
t.goto(10, 80)
t.goto(35, 92)
t.goto(30, 105)
t.end_fill()

t.up()
t.pencolor("black")
t.goto(10, 60)
t.down()
t.goto(40,60)
t.circle(20, 90)
t.up()

t.goto(40, 130)
t.down()
t.goto(40, 115)
t.goto(50, 105)
t.goto(55, 105)
t.goto(65, 115)
t.goto(65, 130)
t.goto(55, 140)
t.goto(50, 140)
t.goto(40, 130)

t.up()
t.goto(40, 125)
t.down()
t.goto(65, 125)

t.up()
t.goto(-100, 100)


turtle.done()