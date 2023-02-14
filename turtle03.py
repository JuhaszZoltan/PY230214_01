import turtle
from random import randint

t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)


for x in range(360):
    r:int = randint(0, 255)
    g:int = randint(0, 255)
    b:int = randint(0, 255)
    hexacode:str = f'#{r:02x}{g:02x}{b:02x}'.upper()
    t.width(x / 10 + 5)
    t.pencolor(hexacode)
    t.pendown()
    t.circle(x*3 + 60)
    t.penup()
    t.forward(x)
    t.left(28)
turtle.done()