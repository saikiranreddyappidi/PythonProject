import turtle

wn = turtle.Screen()
wn.bgcolor("#4ce6bf")
wn.title("ANIMAL RACES")
pen = turtle.Turtle()
pen.up()
pen.goto(300, 300)
pen.down()
# print(pen.position())
pen.right(90)
pen.width(4)
for i in range(15):
	pen.color("Black")
	pen.forward(20)
	pen.color("White")
	pen.forward(20)
# print(pen.position())
h1 = turtle.Turtle()
h1.up()
h1.goto(-300, 290)
h1.down()
h1.color("Blue")
h4 = turtle.Turtle()
h4.up()
h4.goto(-300, 145)
h4.down()
h4.color("#cc00cc")
h2 = turtle.Turtle()
h2.up()
h2.goto(-300, 0)
h2.down()
h2.color("Red")
h5 = turtle.Turtle()
h5.up()
h5.goto(-300, -145)
h5.down()
h5.color("#990099")
h3 = turtle.Turtle()
h3.up()
h3.goto(-300, -290)
h3.down()
h3.color("Green")
h1.width(3)
h2.width(3)
h3.width(3)
h4.width(3)
h5.width(3)
h1.forward(600)
h2.forward(600)
h3.forward(600)
h4.forward(600)
h5.forward(600)
turtle.done()
exit(3)