import turtle

writer = turtle.Turtle()



# red orange blue cyan
# outline color
# the first color is the outline color and the second one is the fill up color.
writer.color("green", "cyan")

# start filling up the shape
writer.begin_fill()
writer.forward(100)
writer.left(90)
writer.forward(100)
writer.left(90)
writer.forward(100)
writer.left(90)
writer.forward(100)
# end the filing
writer.end_fill()

writer.penup()
writer.forward(50)
writer.pendown()

writer.begin_fill()
writer.forward(100)
writer.left(90)
writer.forward(100)
writer.left(90)
writer.forward(100)
writer.left(90)
writer.forward(100)
writer.end_fill()


turtle.mainloop()

