import turtle

#turning on turtle mode! 
t = turtle.Turtle()
t.color("blue") 
t.pensize(6)     

#D-Drawing start
t.penup()
t.goto(-50, 0)  
t.pendown()
t.setheading(90)  
t.forward(100)

#D-Drawing part 2
t.right(90)
t.circle(-50, 180)

#turtle moving 
t.penup()
t.goto(30, 0)
t.pendown()

#A-Drawing
t.setheading(75)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(50)
t.right(105)
t.forward(30)

turtle.done()
