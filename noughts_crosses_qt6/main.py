#!/usr/bin/env python3 

'''
# Noughts & Crosses Project (PYQT6)

1. Draw a board/grid using a data structure of your choice
2. Create a two player game with turns
3. Create a winning function to test if after a turn there is a winner
4. Create a AI-ish predictive function that has predicted moves to win - in a "you versus the computer" game. Have the computer aim to play to win the game.
5. Integrate Pygame/Tkinker to create a window type GUI
'''

__version__ = '1.0.0'  
__author__ = 'Cornelius-Figgle'
__email__ = 'max@fullimage.net'
__maintainer__ = 'Cornelius-Figgle'
__copyright__ = 'Copyright (c) 2024 Max Harrison'
__license__ = 'MIT'
__status__ = 'Development'
__credits__ = ['Max Harrison']

# source: https://github.com/Cornelius-Figgle/noughts-crosses-qt6


from typing import Literal


class Game:
    '''
    Main progam logic.
    '''

    def __init__(
            self,
            gametype: Literal['cpu', '2pl'] = 'cpu'
        ) -> None:

        '''
        Initialises the object. 
        '''

        # create object for the interface
        # this is overwritten by `gui.py`, so we do not do anything here
        self.InterfaceObj = None

        # setup constant attributes
        self.GAMETYPES = {
            'cpu': ['player_turn', 'cpu_turn'],
            '2pl': ['player_turn', 'player_turn']
        }

        # define a blank board
        # a value of 0 represents a blank tile
        # a value of 1 represents player1's selections, or a nought
        # a value of -1 represents player2's selections, or a cross
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        # set current gametype
        self.cur_game = self.GAMETYPES[gametype]

        return

    def player_turn(self, id: int) -> None:
        '''
            
        '''
        
        print(f'player {id}')
        
        return
    
    def cpu_turn(self, id: int) -> None:
        '''
            
        '''

        print(f'cpu {id}')
        
        return

    def check_win(self, id: int) -> bool:
        '''
            
        '''

        return

    def gameloop(self) -> None:
        '''
            
        '''

        while True:
            for i in range(len(self.cur_game)):
                match self.cur_game[i]:
                    case 'player_turn':
                        self.player_turn(i)
                        self.InterfaceObj.draw_board()
                    case 'cpu_turn':
                        self.cpu_turn(i)
                        self.InterfaceObj.draw_board()
        
        return
