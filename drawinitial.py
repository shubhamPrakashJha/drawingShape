import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    tur = turtle.Turtle()
    tur.right(180)
    tur.forward(100)
    tur.right(-90)
    tur.forward(100)
    tur.right(-90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)


    tur.penup()
    tur.right(180)
    tur.forward(200)
    tur.pendown()
    tur.right(-90)
    tur.forward(200)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)

    window.exitonclick()

draw()