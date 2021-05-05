import turtle
import random

t = turtle.Pen()

t.shape("turtle")
t.shapesize(3, 3)
t.up()


x = random.randint(-300, 300)
y = random.randint(-300, 300)

t.goto(x, y)

x = random.randint(-300, 300)

y = random.randint(-300, 300)
t.goto(x, y)
