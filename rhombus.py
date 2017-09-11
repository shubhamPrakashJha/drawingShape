import turtle

def rhombus():
    window = turtle.Screen()
    window.bgcolor("red")

    tur = turtle.Turtle()
    tur.speed(20)
    for j in range(60):
        for i in range(2):
            tur.right(-150)
            tur.forward(100)
            tur.right(-30)
            tur.forward(100)

        tur.right(6)
    window.exitonclick()

rhombus()