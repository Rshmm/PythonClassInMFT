import turtle

screen = turtle.Screen()

screen.setup(500,250)

screen.title("turtle draw square")

writer = turtle.Turtle()
writer.goto(0, 50)
writer.goto(50, 50)
writer.goto(50, 0)
writer.goto(0, 0)


screen.mainloop()
