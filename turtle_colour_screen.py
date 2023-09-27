import turtle
import time

t=turtle.Turtle()
s=turtle.Screen()

l=['Yellow','Gray','Blue','Green','Pink']

while True:
    for i in l:
        s.bgcolor(i)
        time.sleep(1)
