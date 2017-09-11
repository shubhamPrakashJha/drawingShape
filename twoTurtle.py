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
    for j in range(50):
        for i in range(4):
            tutu.forward(100)
            tutu.right(90)
        tutu.right(10)

    mitthu = turtle.Turtle()
    mitthu.speed(20)
    mitthu.shape("turtle")
    for j in range(100):
        for i in range(4):
            mitthu.circle(100)
        mitthu.right(10)

    window.exitonclick()

square()