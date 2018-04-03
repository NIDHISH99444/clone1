import turtle
def drawSquare() :
    window =turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    turtle.color("blue", "red")
    turtle.shape("turtle")
    turtle.speed(10)
    i=0
    for j in range(36) :
        for i in range(4) :
            brad.forward(100)
            brad.right(90)
        brad.right(10)




    window.exitonclick()
drawSquare()