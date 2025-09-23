import turtle

# Tegner en firkant med Turtle Graphics
def tegn_firkant(sidelengde, x_start=0, y_start=0):
    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()
    turtle.forward(sidelengde)
    turtle.right(90)
    turtle.forward(sidelengde)
    turtle.right(90)
    turtle.forward(sidelengde)
    turtle.right(90)
    turtle.forward(sidelengde)
    turtle.right(90)


if __name__ == "__main__":
    tegn_firkant(100)
    tegn_firkant(50, -100, 100)
    turtle.done()
