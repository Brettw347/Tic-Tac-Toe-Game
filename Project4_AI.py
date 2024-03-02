from Project4TicTacToe import *
class Player:

    def __init__(self, name, mark, turnNum): # Creates the Player Class
        self._name = name
        self._playerMark = mark
        self._turnNumber = turnNum

    def getPlayerName(self, Player): # Recieves the User's name for the HumanPlayer object in the Tic Tac Toe File
        Player._name = input('Please enter your name: ')

