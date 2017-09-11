import turtle

def square():
    window = turtle.Screen()
    window.bgcolor("red")

    tutu = turtle.Turtle()
    tutu.speed(30)
    tutu.shape("turtle")
    tutu.width(1)
    tutu.color("white")
    for j in range(100):
        for i in range(4):
            tutu.forward(100)
            tutu.right(90)
        tutu.right(10)


    window.exitonclick()

square()