import turtle

pen = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)
bgcl = ['black', 'white']

colors = ['red', 'green', 'yellow', 'blue']

for x in range(400):
    pen.pencolor(colors[x%4])
    pen.penup()
    pen.forward(4*x)
    pen.pendown()
    pen.write('Zolikaaaa', font = ('Consolas', int((x+4) / 4), 'bold'))
    pen.left(92)
    # turtle.bgcolor(bgcl[x%2])

turtle.done()