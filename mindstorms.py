import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    anige = turtle.Turtle()
    anige.shape("arrow")
    anige.color("yellow")
    anige.circle(100)
    anige.forward(90)
    
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("yellow")
    brad.speed(2)
    
    #@brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    for i in range(1,5):
        brad.forward(100)
        brad.right(90)
    for i in range(1,60):
        brad.forward(110)
        brad.right(100)
    for i in range(1,2):
        brad.forward(90)
        brad.left(50)
        brad.forward(100)
    


    anige = turtle.Turtle()
    anige.shape("arrow")
    anige.color("yellow")
    anige.circle(100)


    window.exitonclick()

draw_art()
