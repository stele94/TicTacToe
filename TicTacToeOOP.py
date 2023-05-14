# Welcome to TicTacToe
# You can play player vs player or player vs computer
###############################################


from random import choice
import os


class Human:
    def __init__(self, name):
        self.name = name
        self.symbol = None

    def playerPosition(self):
        while True:
            playerMove = input(f"{self.name},enter a position (1-9): ")

            if not playerMove.isdigit() or int(playerMove) not in range(1, 10):
                continue
            else:
                if self.checkPosition(playerMove):
                    return int(playerMove)

    def checkPosition(self, position):
        return Board.board[int(position)] == " "

    def playerChoice(self):
        playerSimbol = input(f"{self.name}, please choose X or Y: ").lower()

        while playerSimbol not in ('x', 'y'):
            playerSimbol = input(
                f"{self.name}, please choose X or Y: ").lower()

        self.symbol = playerSimbol


class Computer(Human):
    def __init__(self):
        pass

    def computerPosition(self):
        positions = []

        for position in range(1, 10):
            if Board.board[position] == " ":
                positions.append(position)

        pos = choice(positions)
        return pos


class Board:
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def showBoard(self):
        os.system("cls")

        print(Board.board[1]+"|"+Board.board[2]+"|"+Board.board[3])
        print("------")
        print(Board.board[4]+"|"+Board.board[5]+"|"+Board.board[6])
        print("------")
        print(Board.board[7]+"|"+Board.board[8]+"|"+Board.board[9])

    def checkWinnner(self, playerSimbol):

        # check rows
        if Board.board[1] == Board.board[2] == Board.board[3] == playerSimbol:
            return True
        elif Board.board[4] == Board.board[5] == Board.board[6] == playerSimbol:
            return True
        elif Board.board[7] == Board.board[8] == Board.board[9] == playerSimbol:
            return True

        # check columns
        if Board.board[1] == Board.board[4] == Board.board[7] == playerSimbol:
            return True
        elif Board.board[2] == Board.board[5] == Board.board[8] == playerSimbol:
            return True
        elif Board.board[3] == Board.board[6] == Board.board[9] == playerSimbol:
            return True

        # check diagonals

        if Board.board[1] == Board.board[5] == Board.board[9] == playerSimbol or Board.board[3] == Board.board[5] == Board.board[7] == playerSimbol:
            return True

    def checkTie(self):
        counter = 0

        for i in range(1, 10):
            if Board.board[i] != " ":
                counter += 1
        return counter == 9

    def resetBoard(self):
        Board.board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]


class GameOn:

    def __init__(self):
        while True:
            userInput = input(
                "Game Mode:\n1)Player vs Player\n2)Player vs Computer\n3)Exit\nAnswer:")

            # Player vs Player
            if userInput == '1':
                player1 = Human("Player 1")
                player2 = Human("Player 2")
                board = Board()

                # Reset the board
                board.resetBoard()
                player1.playerChoice()

                while True:

                    if player1.symbol == 'x':
                        player2.symbol = 'y'
                    else:
                        player1.symbol = 'y'
                        player2.symbol = 'x'

                    # Player1
                    Board.board[player1.playerPosition()] = player1.symbol
                    board.showBoard()
                    if board.checkWinnner(player1.symbol):
                        print(f"{player1.name} has won!!")
                        break

                    # Check for tie
                    if board.checkTie():
                        print("It is tie")
                        break

                    # Player2
                    Board.board[player2.playerPosition()] = player2.symbol
                    board.showBoard()
                    if board.checkWinnner(player2.symbol):
                        print(f"{player2.name} has won!!")
                        break

            # Player vs Computer
            elif userInput == '2':
                computer = Computer()
                player = Human("Player")
                board = Board()

                # Reset the board
                board.resetBoard()

                # GameOn
                while True:
                    if player.symbol == 'x':
                        computer.symbol = 'y'
                    else:
                        player.symbol = 'y'
                        computer.symbol = 'x'

                    # Player
                    Board.board[player.playerPosition()] = player.symbol
                    board.showBoard()
                    if board.checkWinnner(player.symbol):
                        print("Player has won!!")
                        break

                    # Check for tie
                    if board.checkTie():
                        print("It is tie")
                        break

                    # Computer
                    Board.board[computer.computerPosition()] = computer.symbol
                    board.showBoard()
                    if board.checkWinnner(computer.symbol):
                        print("Computer has won!!")
                        break

            # Exit the game
            elif userInput == '3':
                os.system("cls")
                print("Thank you for playing TicTacToe :) ")

                break
            else:
                os.system("cls")
                print("Wrong input,try again: ")
                continue


GameOn()
