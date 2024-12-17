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


class Game:
    '''
    Main progam logic.
    '''

    def __init__(self, gametype: str = 'cpu') -> None:
        '''
            
        '''

        self.gametype_defs = {
            'cpu': ['player_turn', 'cpu_turn'],
            'splitscreen': ['player_turn','player_turn'],
            'alternate': ['player_turn', 'player_turn']
        }
        
        self.gametype = self.gametype_defs[gametype]
        print(self.gametype)

        self.board = (
            (int, int, int),
            (int, int, int),
            (int, int, int)
        )

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
            for i in range(len(self.gametype)):
                match self.gametype[i]:
                    case 'player_turn':
                        self.player_turn(i)
                    case 'cpu_turn':
                        self.cpu_turn(i)
        
        return
