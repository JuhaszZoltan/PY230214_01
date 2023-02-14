import turtle



#           0       1        2        3        4          5
colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow']

t = turtle.Pen()
turtle.bgcolor('white')
t.speed(10)

for x in range(360):
    t.pencolor(1 - (x / 360), 0, 0)
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(85)

turtle.done()