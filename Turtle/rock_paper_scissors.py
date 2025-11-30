import turtle
import random


screen = turtle.Screen()

screen.setup(600 , 300)

screen.title("rock paper scissors game")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 50)

choice = screen.textinput("rock paper scissors game",
                          "choose one of them :\nrock\npaper\nscissors")


comp = random.choice(["rock", "paper", "scissors"])


if choice == comp:
    result = "Draw!"
elif ((choice == "rock" and comp == "scissors") or (choice == "paper" and comp == "rock") or
      (choice == "scissors" and comp == "paper")):
    result = "You win!"
else:
    result = "Computer wins!"


writer.write(
    f"You: {choice}\n computer : {comp}\n\n{result}",
    align="center"
)


turtle.mainloop()

