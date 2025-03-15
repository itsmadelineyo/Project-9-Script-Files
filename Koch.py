>>> import turtle
>>> def drawFractalLine(t, distance, angle, level):
...     if level == 0:
...         t.setheading(angle)
...         t.forward(distance)
...         return
...         distance /= 3.0
...         drawFractalLine(t, distance, angle, level - 1)
...         drawFractalLine(t, distance, angle + 60, level - 1)
...         drawFractalLine(t, distance, angle - 120, level - 1)
...         drawFractalLine(t, distance, angle, level - 1)
...
>>> def drawKochSnowflake(t, distance, level):
...     angles = [0, -120, 120]
...     for angle in angles:
...         drawFractalLine(t, distance, angle, level)
...
>>> def main():
...     screen = turtle.Screen()
...     screen.bgcolor("white")
...
>>> t = turtle.Turtle()
>>> t.pensize(2)
>>> t.pencolor("blue")
>>> t.penup()
>>> t.goto(-100, 50)
>>> t.pendown()
>>> drawKochSnowflake(t, 200, 2)
>>>
