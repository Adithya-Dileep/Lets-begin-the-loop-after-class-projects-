import turtle
pen = turtle.Turtle()
pen.speed(1)
side_length = 100
for _ in range(4):
    pen.forward(side_length)
    pen.right(90)
turtle.done()