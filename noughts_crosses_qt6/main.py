#!/usr/bin/env python3 

'''
# Noughts & Crosses Project (PYQT6)
'''

__version__ = '1.0.0'  
__author__ = 'Cornelius-Figgle'
__email__ = 'max@fullimage.net'
__maintainer__ = 'Cornelius-Figgle'
__copyright__ = 'Copyright (c) 2024 Max Harrison'
__license__ = 'MIT'
__status__ = 'Development'
__credits__ = ['Max Harrison']

# source code: https://github.com/Cornelius-Figgle/noughts-crosses-qt6


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
        # a non-zero value represents the player indexed by `GAMETYPES`
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        # set current game settings
        self.cur_game = self.GAMETYPES[gametype]
        self.cur_player = 1

        return

    def take_turn(self, pos: tuple[int,int] = None) -> None:
        '''
        Either updates the board based on the tile coordinate passed in,
        or takes a turn as the cpu 'player'. 

        Then pass control to the next player. 
        '''

        while True:
            # either update the board to reflect the user's input
            # or let the cpu 'player' take its turn
            match self.cur_game[self.cur_player - 1]:
                case 'player_turn':
                    # check if selected tile is empty
                    if self.board[pos[1]][pos[0]] == 0:
                        # update board
                        self.board[pos[1]][pos[0]] = self.cur_player
                    else:
                        # inform user of invalid move and exit
                        # so that they can select another tile

                        ...  # TODO: `QMessageBox`
                        
                        break
                case 'cpu_turn':
                    self.cpu_turn()
                
            # redraw board
            self.InterfaceObj.draw_board()

            # next player
            self.cur_player += 1

            # reset player count if all players have had their turn
            if self.cur_player > len(self.cur_game):
                self.cur_player = 1

            # if next player is the cpu then loop
            # if next player is the user then exit and wait for input
            match self.cur_game[self.cur_player - 1]:
                case 'player_turn':
                    # break and wait for user input
                    break
                case 'cpu_turn':
                    # loop and take turn
                    continue
                    
        return

    def cpu_turn(self) -> None:
        '''
        Takes a go as the cpu 'player'.  
        '''

        ...

        return
    
    def check_win(self) -> None:
        '''
            
        '''

        ...  # TODO: `QMessageBox`

        return
