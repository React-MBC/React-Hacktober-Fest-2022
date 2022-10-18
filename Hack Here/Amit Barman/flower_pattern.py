import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("grey")
t.speed(0)
a = 0
b = 0
while True:
    for i in range(4):
        t.forward(80)
        t.right(90)
        t.right(15)
        a+=1
        if a>=390/30:
            t.forward(50)
            a = 0
            b +=1
            if b >=12:
                break
        t.hideturtle()
turtle.done()