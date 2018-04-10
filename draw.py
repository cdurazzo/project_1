import turtle

painter = turtle.Turtle()
painter.pensize(20)

for _ in range(100):
    painter.forward(150)
    painter.left(100)

turtle.done()