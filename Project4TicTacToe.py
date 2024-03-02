from random import randrange
from Project4_AI import *
from Project4_GameInitialize import *
class TicTacToe:

    def __init__(self): # Initialized the TicTacToe class; creates the board. _player is used when a player is marking the board with an X/O
        self._board = [[' '] * 3 for j in range(3)]
        self._player = ' '

    def mark(self, i, j): # Checks if a board position is taken and puts a mark down when it is not taken
        if not(0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid Board Position')
        if self._board[i][j] != ' ':
            raise ValueError('Board Position Occupied')
        if self.winner() is not None:
            raise ValueError('Game is already Complete')
        self._board[i][j] = self._player

    def _is_win(self, mark): # Checks for a winner by looking at the board
        board = self._board
        return ( mark == board[0][0] == board[0][1] == board[0][2] or
                 mark == board[1][0] == board[1][1] == board[1][2] or
                 mark == board[2][0] == board[2][1] == board[2][2] or
                 mark == board[0][0] == board[1][0] == board[2][0] or
                 mark == board[0][1] == board[1][1] == board[2][1] or
                 mark == board[0][2] == board[1][2] == board[2][2] or
                 mark == board[0][0] == board[1][1] == board[2][2] or
                 mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self): # Returns who won when _is_win finds a winner
        for Player._playerMark in 'XO':
            if self._is_win(Player._playerMark):
                return Player._playerMark
            return None

    def __str__(self): # Adds bars in between the spots of the ._board list to create the Tic Tac Toe board
        rows = ['|' .join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

game = TicTacToe() # Simplifies referral to the TicTacToe class for the program
gameInit = GameInitalize() # Simplifies referral to the GameInitialize class for the program

def endTurn(): # Checks to see if there is a winner after the board is updated
    winner = game.winner()
    if winner is not None:
        print(winner, 'wins')
        exit()
    if not any(' ' in x for x in game._board) and winner is None:
        print('Tie')
        exit()

def userMove(HumanPlayer, CompPlayer): # Used to get the User's input on their turn
            column = input(HumanPlayer._name + "'s Turn, Please choose which column to put an " + HumanPlayer._playerMark +" in: ")
            row = input('Please choose which column to put an ' + HumanPlayer._playerMark + ' in: ')
            game._player = HumanPlayer._playerMark
            game.mark(int(column), int(row))
            print(game)
            endTurn()
            computerPlayerMove(CompPlayer, HumanPlayer)

def computerPlayerMove(CompPlayer, HumanPlayer): # Determines how the Computer Player will play each turn
    if game._board[1][1] == ' ': # Computer Player places a mark in the middle
        print("Computer Player's Turn...")
        game._player = CompPlayer._playerMark
        game.mark(1, 1)
        print(game)
        winner = game.winner()
        if winner is not None:
            print(game)
            print(winner, 'wins')
        if not any(' ' in x for x in game._board) and winner is None:
            print(game)
            print('Tie')
        userMove(HumanPlayer, CompPlayer)
    elif game._board[0][0] and game._board[0][1] == HumanPlayer._playerMark and game._board[0][2] == ' ' or game._board[0][1] and game._board[0][2] == HumanPlayer._playerMark and game._board[0][0] == ' ' or game._board[0][2] and game._board[0][0] == HumanPlayer._playerMark and game._board[0][1] == ' ': # Blocks the user from getting three marks in the top row
        if game._board[0][0] and game._board[0][1] == HumanPlayer._playerMark and game._board[0][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0,2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif game._board[0][1] and game._board[0][2] == HumanPlayer._playerMark and game._board[0][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0,0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif game._board[0][2] and game._board[0][0] == HumanPlayer._playerMark and game._board[0][1] == ' ': 
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0,1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[1][0] and game._board[1][1] == HumanPlayer._playerMark and game._board[1][2] == ' ' or game._board[1][1] and game._board[1][2] == HumanPlayer._playerMark and game._board[1][0] == ' ' or game._board[1][2] and game._board[1][0] == HumanPlayer._playerMark and game._board[1][1] == ' ': # Blocks the User from getting three marks in the middle row
        if game._board[1][0] and game._board[1][1] == HumanPlayer._playerMark and game._board[1][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[1][1] and game._board[1][2] == HumanPlayer._playerMark and game._board[1][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[1][2] and game._board[1][0] == HumanPlayer._playerMark and game._board[1][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[2][0] and game._board[2][1] == HumanPlayer._playerMark and game._board[2][2] == ' ' or game._board[2][1] and game._board[2][2] == HumanPlayer._playerMark and game._board[2][0] == ' ' or game._board[2][2] and game._board[2][0] == HumanPlayer._playerMark and game._board[2][1] == ' ': # Blocks the User from getting three marks in the bottom row
        if game._board[2][0] and game._board[2][1] == HumanPlayer._playerMark and game._board[2][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[2][1] and game._board[2][2] == HumanPlayer._playerMark and game._board[2][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[2][2] and game._board[2][0] == HumanPlayer._playerMark and game._board[2][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[0][0] and game._board[1][0] == HumanPlayer._playerMark and game._board[2][0] == ' ' or game._board[1][0] and game._board[2][0] == HumanPlayer._playerMark and game._board[0][0] == ' ' or game._board[2][0] and game._board[0][0] == HumanPlayer._playerMark and game._board[1][0] == ' ': # Blocks the User from getting three marks in the left column
        if game._board[0][0] and game._board[1][0] == HumanPlayer._playerMark and game._board[2][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[1][0] and game._board[2][0] == HumanPlayer._playerMark and game._board[0][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[2][0] and game._board[0][0] == HumanPlayer._playerMark and game._board[1][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[0][1] and game._board[1][1] == HumanPlayer._playerMark and game._board[2][1] == ' ' or game._board[1][1] and game._board[2][1] == HumanPlayer._playerMark and game._board[0][1] == ' ' or game._board[0][1] and game._board[2][1] == HumanPlayer._playerMark and game._board[1][1] == ' ': # Blocks the User from getting three marks in the middle column
        if game._board[0][1] and game._board[1][1] == HumanPlayer._playerMark and game._board[2][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[1][1] and game._board[2][1] == HumanPlayer._playerMark and game._board[0][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[0][1] and game._board[2][1] == HumanPlayer._playerMark and game._board[1][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[0][2] and game._board[1][2] == HumanPlayer._playerMark and game._board[2][2] == ' ' or game._board[1][2] and game._board[2][2] == HumanPlayer._playerMark and game._board[0][2] == ' ' or game._board[2][2] and game._board[0][2] == HumanPlayer._playerMark and game._board[1][2] == ' ': # Blocks the User from getting three marks in the right column
        if game._board[0][2] and game._board[1][2] == HumanPlayer._playerMark and game._board[2][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[1][2] and game._board[2][2] == HumanPlayer._playerMark and game._board[0][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[2][2] and game._board[0][2] == HumanPlayer._playerMark and game._board[1][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 2)
            print(game)
            winner = game.winner()
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[0][0] and game._board[1][1] == HumanPlayer._playerMark and game._board[2][2] == ' ' or game._board[1][1] and game._board[2][2] == HumanPlayer._playerMark and game._board[0][0] == ' ' or game._board[2][2] and game._board[0][0] == HumanPlayer._playerMark and game._board[1][1] == ' ' or game._board[0][2] and game._board[1][1] == HumanPlayer._playerMark and game._board[2][0] == ' ' or game._board[2][0] and game._board[0][2] == HumanPlayer._playerMark and game._board[1][1] == ' ' or game._board[1][1] and game._board[2][0] == HumanPlayer._playerMark and game._board[0][2] == ' ': # Blocks the User from getting three marks in a diagonal
        if game._board[0][0] and game._board[1][1] == HumanPlayer._playerMark and game._board[2][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[1][1] and game._board[2][2] == HumanPlayer._playerMark and game._board[0][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[2][2] and game._board[0][0] == HumanPlayer._playerMark and game._board[1][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[0][2] and game._board[1][1] == HumanPlayer._playerMark and game._board[2][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[2][0] and game._board[0][2] == HumanPlayer._playerMark and game._board[1][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        if game._board[1][1] and game._board[2][0] == HumanPlayer._playerMark and game._board[0][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[1][1] == HumanPlayer._playerMark: # CP blocks the User if the User marked the center position
        if random.randrange(0, 4) == 0 and game._board[0][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif random.randrange(0, 4) == 1 and game._board[1][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif random.randrange(0, 4) == 2 and game._board[1][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(1, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif random.randrange(0, 4) == 3 and game._board[2][1] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 1)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
    elif game._board[1][1] != ' ': # CP places a mark in a corner if the center position is already marked
        if game._board[0][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif game._board[0][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(0, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif game._board[2][0] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 0)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)
        elif game._board[2][2] == ' ':
            print("Computer Player's Turn...")
            game._player = CompPlayer._playerMark
            game.mark(2, 2)
            print(game)
            endTurn()
            userMove(HumanPlayer, CompPlayer)


def Game(): # Function that runs the Tic Tac Toe Game
    HumanPlayer = Player(' ', ' ', 0) # Creation of HumanPlayer Object
    CompPlayer = Player('Computer Player', ' ', 0) # Creation of CompPlayer Object
    HumanPlayer.getPlayerName(HumanPlayer) # Gets a name from the User to use in the HumanPlayer object
    gameInit.chooseMark(HumanPlayer, CompPlayer) # Sets which players get X/O
    gameInit.chooseFirstMove(HumanPlayer, CompPlayer) # Sets which player moves first
    if HumanPlayer._turnNumber == 1: # The Game if the User goes first
        while 'X' or 'O' not in game._board and ' ' in game._board:
            userMove(HumanPlayer, CompPlayer)
            computerPlayerMove(CompPlayer, HumanPlayer)
    if CompPlayer._turnNumber == 1: # The game if the AI goes first
        while 'X' or 'O' not in game._board and ' ' in game._board:
            computerPlayerMove(CompPlayer, HumanPlayer)
            userMove(HumanPlayer, CompPlayer)
