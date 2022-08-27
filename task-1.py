import turtle
from time import sleep

def rectangle():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Alhazen Hackathon")
    skk = turtle.Turtle()
    sides = 4
    length = 200
    angle = 360 / sides
    for i in range(sides):
        if i % 2 != 0:
            skk.forward(length / 2)
            skk.right(angle)
        else:
            skk.forward(length)
            skk.right(angle)
    sleep(3)
    turtle.clearscreen()

def hexagon():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Alhazen Hackathon")
    skk = turtle.Turtle()
    sides = 6
    length = 65
    angle = 360 / sides
    for i in range(sides):
        skk.forward(length)
        skk.rt(angle)
    sleep(3)
    turtle.clearscreen()

def pentagon():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Alhazen Hackathon")
    skk = turtle.Turtle()
    sides = 5
    length = 65
    angle = 360 / sides 
    for i in range(sides):
        skk.forward(length)
        skk.rt(-angle)
    sleep(3)
    turtle.clearscreen()

def main():
    hexagon()
    pentagon()
    rectangle()

if __name__ == '__main__':
    main()
