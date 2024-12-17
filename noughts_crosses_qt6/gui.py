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

# source: https://github.com/Cornelius-Figgle/noughts-crosses-qt6


import sys

from main import Game


def main() -> None:
    '''
    Controls the main program flow.
    '''

    # initialise object
    GameObj = Game('cpu')
   
    return


# only execute if called directly
if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print()
        sys.exit()
