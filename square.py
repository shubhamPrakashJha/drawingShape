import turtle

def square():
    window = turtle.Screen()
    window.bgcolor("#f9f59f")

    tutu = turtle.Turtle()
    tutu.speed(30)
    tutu.shape("turtle")
    tutu.width(2)
    tutu.turtlesize(5)
    tutu.color("green")
    for j in range(100):
        for i in range(4):
            tutu.forward(100)
            tutu.right(90)
        tutu.right(10)


    window.exitonclick()

square()