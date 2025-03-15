>>> import turtle
>>> import math
>>> def drawCircle(t, x, y, radius):
...     t.up()
...     t.goto(x, y - radius)
...     t.down()
...
>>> def drawCircle(t, x, y, radius):
...     t.up()
...     t.goto(x, y - radius)
...     t.down()
...     distance = 2.0 * math.pi * radius / 120.0
...     for _ in range(120):
...         t.forward(distance)
...         t.left(3)
...
>>> if __name__ == "__main__":
...     screen = turtle.Screen()
...     screen.bgcolor("white")
...
>>> t = turtle.Turtle()
>>> t.pensize(2)
>>> t.pencolor("blue")
>>> drawCircle(t, 0, 0, 100)
>>>
