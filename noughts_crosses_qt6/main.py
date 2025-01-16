#!/usr/bin/env python3 

'''
# Noughts & Crosses Project (PyQt6)
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
    Main program logic.
    '''

    def __init__(self, _InterfaceObj: type['InterfaceObj']) -> None:
        '''
        Initialises the object. 
        '''

        # create object for the interface
        self.InterfaceObj = _InterfaceObj

        # setup gametype definitions
        self.GAMETYPES = {
            'cpu': [
                {
                    'name': 'Player1',
                    'type': 'player_turn',
                    'id': 1,
                    'score': 0
                },
                {
                    'name': 'CPU1',
                    'type': 'cpu_turn',
                    'id': 2,
                    'score': 0
                }
            ],
            '2pl': [
                {
                    'name': 'Player1',
                    'type': 'player_turn',
                    'id': 1,
                    'score': 0
                },
                {
                    'name': 'Player2',
                    'type': 'player_turn',
                    'id': 2,
                    'score': 0
                }
            ]
        }

        return

    def setup_game(self, gametype: Literal['cpu', '2pl'] = None) -> None:
        '''
        Sets the default variables for the game.
        '''
        
        # define a blank board (this must be 3x3)
        # a value of 0 represents a blank tile
        # a non-zero value represents the player indexed by `GAMETYPES`
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        # reset the cpu move tracker
        self.cpu_moves = list()

        # reset current game settings
        if gametype:
            self.current_game = self.GAMETYPES[gametype]
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
            match self.current_game[self.current_player - 1]['type']:
                case 'player_turn':
                    # check if selected tile is empty
                    if self.board[pos[1]][pos[0]] == 0:
                        # update board
                        self.board[pos[1]][pos[0]] = self.current_player
                        # redraw board
                        self.InterfaceObj.draw_board()
                    else:
                        # inform user of invalid move and exit
                        # so that they can select another tile
                        self.InterfaceObj.inform_invalid('move')
                        break
                case 'cpu_turn':
                    # take turn as cpu
                    self.cpu_turn()
                    # redraw board after delay
                    self.InterfaceObj._delay(
                        1000,
                        self.InterfaceObj.draw_board
                    )

            # check if the player or cpu has made a winning move
            win_state = self.check_win()
            if win_state != 'none':
                # increase scores
                if win_state == 'win':
                    self.current_game[self.current_player - 1]['score'] += 3
                elif win_state == 'draw':
                    for player in self.current_game:
                        player['score'] += 1

                # let the user know and prompt for what next
                if self.InterfaceObj.inform_win(win_state):
                    # if they wish to replay, resetup the game variables
                    self.setup_game()
                    # and redraw the new board
                    self.InterfaceObj.draw_board()
                else:
                    # if they wish to exit
                    self.InterfaceObj._quit()  # future: landing screen
            else:
                # next player
                self.current_player += 1

                # reset player count if all players have had their turn
                if self.current_player > len(self.current_game):
                    self.current_player = 1

            # if next player is the cpu then loop
            # if next player is the user then exit and wait for input
            match self.current_game[self.current_player - 1]['type']:
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
        
        Algorithm logic adapted from the summary of Paul Curzon and
        Peter W McOwan's logic on p137 of their book 'The Power of
        Computational Thinking' provided on www dot advanced-ict dot
        info. Links to the source can be found in the project README.
        '''

        def check_almost_win(id: int) -> tuple[int, int] | None:
            '''
            Checks if the player one move away from winning.

            Nested function because we have to check this for the second
            and third/fourth moves. 
            '''

            # check for horizontal lines
            for row in self.board:
                if row == [0, id, id]:
                    return (0, self.board.index(row))
                elif row == [id, 0, id]:
                    return (1, self.board.index(row))
                elif row == [id, id, 0]:
                    return (2, self.board.index(row))
            else:
                # check for vertical lines
                for x in range(3):
                    if (self.board[0][x] == 0
                            and self.board[1][x] == id
                            and self.board[2][x] == id):

                        return (x, 0)
                    elif (self.board[0][x] == id
                            and self.board[1][x] == 0
                            and self.board[2][x] == id):

                        return (x, 1)
                    elif (self.board[0][x] == id
                            and self.board[1][x] == id
                            and self.board[2][x] == 0):

                        return (x, 2)
                else:
                    # check for diagonal lines
                    if (self.board[0][0] == 0
                            and self.board[1][1] == id
                            and self.board[2][2] == id):
                            
                        return (0, 0)
                    elif (self.board[0][2] == 0
                            and self.board[1][1] == id
                            and self.board[2][0] == id):
                            
                        return (2, 0)
                    elif ((self.board[0][0] == id
                            and self.board[1][1] == 0
                            and self.board[2][2] == id)
                            # TR:BL
                            or (self.board[0][2] == id
                            and self.board[1][1] == 0
                            and self.board[2][0] == id)):

                        return (1, 1)
                    elif (self.board[0][0] == id
                            and self.board[1][1] == id
                            and self.board[2][2] == 0):
                            
                        return (2, 2)
                    elif (self.board[0][2] == id
                            and self.board[1][1] == id
                            and self.board[2][0] == 0):
                            
                        return (0, 2)
                    else: 
                        return None

        match len(self.cpu_moves):
            # for the first move, go in a corner
            case 0:
                # check TL, else go TR
                if self.board[0][0] == 0:
                    selected_tile = (0, 0)
                else:
                    selected_tile = (2, 0)
            # for the second move, try to block the opponent's line,
            # else go in the opposite corner
            case 1:
                # try to fill in the opponent's line
                selected_tile = check_almost_win(
                    int(not self.current_player - 1) + 1
                )
                # if there was no move that needed to be blocked
                if selected_tile is None:
                    match self.cpu_moves[0]:
                        case (0,0):
                            # check TR, then BL, else go BR
                            if self.board[0][2] == 0:
                                selected_tile = (2, 0)
                            elif self.board[2][0] == 0:
                                selected_tile = (0, 2)
                            else:
                                selected_tile = (2, 2)
                        case (2,0):
                            # check BR else BL
                            # since TL would have already been checked
                            if self.board[2][2] == 0:
                                selected_tile = (2, 2)
                            else:
                                selected_tile = (0, 2)
            # for third and fourth move, try to fill our line, else try
            # to block the opponent's line, else go in another corner
            case 2 | 3:
                # try to fill the line we have 2 tiles in
                selected_tile = check_almost_win(
                    self.current_player
                )
                if selected_tile is None:
                    # try to fill in the opponent's line
                    selected_tile = check_almost_win(
                        int(not self.current_player - 1) + 1
                    )
                    # if there was no move that needed to be blocked
                    if selected_tile is None:
                        # go in another corner
                        # check BL, else BR, else any blank
                        if self.board[2][0] == 0:
                            selected_tile = (0, 2)
                        elif self.board[2][2] == 0:
                            selected_tile = (2, 2)
                        else:
                            for x in range(3):
                                for y in range(3):
                                    if self.board[y][x] == 0:
                                        selected_tile = (x,y)
                                        break
                                else:
                                    continue
                                break
                            
            # for the fifth move, go in the free space
            # this is only applicable if the cpu is going first
            case 4:
                for x in range(3):
                    for y in range(3):
                        if self.board[y][x] == 0:
                            selected_tile = (x,y)
                            break
                    else:
                        continue
                    break
        
        self.cpu_moves.append(selected_tile)

         # set our selected tile
        self.board[selected_tile[1]][selected_tile[0]] = self.current_player
        
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
        for x in range(3):
            for row in self.board:
                if row[x] != self.current_player:
                    break
            else:
                return 'win'

        # check for TL-BR diagonal wins
        for y in range(3):
            for x in range(3):
                if x == y:
                    if self.board[y][x] != self.current_player:
                        break
            else:
                continue
            break  # break break
        else:
            return 'win'

        # check for TR-BL diagonal wins
        for y in range(3):
            for x in range(3):
                if x == 3 - y - 1:
                    if self.board[y][x] != self.current_player:
                        break
            else:
                continue
            break  # break break
        else:
            return 'win'

        # check if all tiles are filled without a win (draw)
        for x in range(3):
            for y in range(3):
                if self.board[y][x] == 0:
                    break
            else:
                continue
            break  # break break
        else:
            return 'draw'

        return 'none'
