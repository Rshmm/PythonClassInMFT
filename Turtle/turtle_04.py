import turtle

writer = turtle.Turtle()

writer.color("green", "blue")

writer.begin_fill()
for _ in range(50):
    writer.forward(100)
    writer.right(170)
    writer.forward(100)
writer.end_fill()

turtle.mainloop()