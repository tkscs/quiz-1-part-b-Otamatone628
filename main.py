import turtle

# YOUR CODE HERE
turtle.forward(50)
a = turtle.position()
turtle.forward(50)
turtle.right(90)

turtle.forward(50)
b= turtle.position()
turtle.forward(50)
turtle.right(90)

turtle.forward(50)
c = turtle.position()
turtle.forward(50)
turtle.right(90)

turtle.forward(50)
d = turtle.position()
turtle.forward(50)
turtle.right(90)

turtle.penup()
turtle.goto(a)
turtle.pendown()

turtle.goto(b)
turtle.goto(c)
turtle.goto(d)
turtle.goto(a)

turtle.exitonclick()