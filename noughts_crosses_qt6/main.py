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


from random import choice
from time import sleep
from typing import Literal


class Game:
    '''
    Main progam logic.
    '''

    def __init__(self, _InterfaceObj: type['InterfaceObj']) -> None:
        '''
        Initialises the object. 
        '''

        # create object for the interface
        # this is overwritten by `gui.InterfaceObj`
        # so we do not do anything here
        self.InterfaceObj = _InterfaceObj

        # setup constant attributes
        self.GAMETYPES = {
            'cpu': ['player_turn', 'cpu_turn'],
            '2pl': ['player_turn', 'player_turn']
        }

        return

    def setup_game(self, _gametype: Literal['cpu', '2pl'] = 'cpu') -> None:
        '''
        Sets the default variables for the game.
        '''
        
        # define a blank board
        # a value of 0 represents a blank tile
        # a non-zero value represents the player indexed by `GAMETYPES`
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        # set current game settings
        self.gametype = _gametype
        self.current_player = 1

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
            match self.GAMETYPES[self.gametype][self.current_player - 1]:
                case 'player_turn':
                    # check if selected tile is empty
                    if self.board[pos[1]][pos[0]] == 0:
                        # update board
                        self.board[pos[1]][pos[0]] = self.current_player
                    else:
                        # inform user of invalid move and exit
                        # so that they can select another tile
                        self.InterfaceObj.inform_invalid('move')
                        break
                case 'cpu_turn':
                    self.cpu_turn()

            # redraw board
            self.InterfaceObj.draw_board()

            # check if the player or cpu has made a winning move
            win_state = self.check_win()
            if win_state != 'none':
                # let the user know and prompt for what next
                if self.InterfaceObj.inform_win(win_state):
                    # if they wish to replay, resetup the game variables
                    self.setup_game(self.gametype)
                    # and redraw the new board
                    self.InterfaceObj.draw_board()
                else:
                    # if they wish to exit
                    self.InterfaceObj._quit()  # future: landing screen
            else:
                # next player
                self.current_player += 1

                # reset player count if all players have had their turn
                if self.current_player > len(self.GAMETYPES[self.gametype]):
                    self.current_player = 1

            # if next player is the cpu then loop
            # if next player is the user then exit and wait for input
            match self.GAMETYPES[self.gametype][self.current_player - 1]:
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

        possible_options = list()

        for x in range(len(self.board[0])):
            for y in range(len(self.board)):
                if self.board[y][x] == 0:
                    possible_options.append((x,y))

        chosen_tile = choice(possible_options)
        
        self.board[chosen_tile[1]][chosen_tile[0]] = self.current_player
        
        return
    
    def check_win(self) -> Literal['none', 'win', 'draw']:
        '''
        Checks if a player has made a winning move.
        '''

        # check for horizontal wins
        for row in self.board:
            for tile in row:
                if tile != self.current_player:
                    break
            else:
                return 'win'

        # check for vetical wins
        for x in range(len(self.board[0])):
            for row in self.board:
                if row[x] != self.current_player:
                    break
            else:
                return 'win'

        # check for TL-BR diagonal wins
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if x == y:
                    if self.board[y][x] != self.current_player:
                        break
            else:
                continue
            break  # break break
        else:
            return 'win'

        # check for TR-BL diagonal wins
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if x == len(self.board[0])-y-1:
                    if self.board[y][x] != self.current_player:
                        break
            else:
                continue
            break  # break break
        else:
            return 'win'

        # check if all tiles are filled without a win (draw)
        for x in range(len(self.board[0])):
            for y in range(len(self.board)):
                if self.board[y][x] == 0:
                    break
            else:
                continue
            break  # break break
        else:
            return 'draw'

        return 'none'
