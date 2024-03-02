from Project4_AI import *
import random
class GameInitalize:

    def __init__(self): # Initalizes the GameInitialize class
        self._turncounter = 0

    def chooseFirstMove(self, Player, Player2): # Randomly chooses and assigns which players moves first
        if random.randrange(0, 2) == 0:
            print(Player._name, 'goes first')
            Player._turnNumber = 1
        else:
            print('Computer Player Goes first')
            Player2._turnNumber = 1
    
    def chooseMark(self, Player, Player2): # Randomly chooses  and assigns which players get X or O
        if random.randrange(0, 1) == 0:
            Player._playerMark = 'X'
            Player2._playerMark = 'O'
            print(Player._name, 'is O, Computer Player is X')
        else:
            Player2._playerMark = 'O'
            Player._playerMark = 'X'
            print(Player._name, 'is X, Computer Player is O')