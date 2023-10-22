from tkinter import *
import random

# Take user input


def userInput(row, column):
    global player

    if buttons[row][column]["text"] == "" and checkWinner() == False:
        if player == players[0]:

            buttons[row][column]["text"] = players[0]

            if checkWinner() == True:
                label.config(text=f"{player} win!")

            elif checkWinner() == "Tie":
                label.config(text="It is tie!")

            elif checkWinner() == False:
                player = players[1]
                label.config(text=f"{player}`s turn")

        else:
            buttons[row][column]["text"] = players[1]

            if checkWinner() == True:
                label.config(text=f"{player} win!")

            elif checkWinner() == "Tie":
                label.config(text="It is tie!")

            elif checkWinner() == False:
                player = players[0]
                label.config(text=f"{player}`s turn")

# New game


def restartGame():
    global label
    for row in range(3):
        for column in range(3):
            buttons[row][column]["text"] = ""
            buttons[row][column].config(bg="white")

    label.config(text=f"{player}`s turn")


# Check for winning conditions
def checkWinner():

    for row in range(3):
        for column in range(3):
            if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
                buttons[row][0].config(bg='green')
                buttons[row][1].config(bg='green')
                buttons[row][2].config(bg='green')
                return True

    for row in range(3):
        for column in range(3):
            if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
                buttons[0][column].config(bg='green')
                buttons[1][column].config(bg='green')
                buttons[2][column].config(bg='green')
                return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    if checkTie():
        return "Tie"

    return False


# Check for empty spaces
def checkTie():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return True

    return False


# Make a window with widgets and players
root = Tk()
root.title("Tic-Tac-Toe Game")
root.resizable(False, False)
players = ["X", "O"]
player = random.choice(players)
label = Label(root, text=f"{player}`s turn", font=("Times new Roman", 15))
label.pack()

newGame = Button(root, text="New game", bg="black",
                 fg="white", command=restartGame)
newGame.pack()

frame = Frame(root)
frame.pack()


buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame, width=15, font=("Arial", 10), height=15, text="", bg="white", command=lambda row=row, column=column: userInput(row, column))
        buttons[row][column].grid(row=row, column=column)


root.mainloop()
