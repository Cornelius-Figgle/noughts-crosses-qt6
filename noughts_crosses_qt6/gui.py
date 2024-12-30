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


import sys

import qtawesome as qta
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
    QLabel,
    QPushButton,
    QMessageBox,
    QFrame
)

from main import Game


class GUI_Interface(QMainWindow):
    '''
    Collection of methods for displaying information to, and receiving
    information from, the user in a consistant and modular way. 
    '''

    def __init__(self, _AppObj: type[QApplication]) -> None:
        '''
        Sets up the gui and handles the main program loop after exec is
        handed over.
        '''

        # initialises from QMainWindow
        super().__init__()

        # initialise object
        self.GameObj = Game(self)
        self.GameObj.setup_game('2pl')

        # stores the QApplication object for later use in `_quit()`
        self.AppObj = _AppObj

        # creates a widget to hold our layout
        self.layout_widget = QWidget()
        self.setCentralWidget(self.layout_widget)

        # creates a layout to hold our widgets
        self.layout_current = QGridLayout()
        self.layout_widget.setLayout(self.layout_current)

        # draws our initial board to the screen
        self.draw_board()

        return

    def _quit(self) -> None:
        '''
        Gracefully exits the application.
        '''

        self.AppObj.quit()

        return

    def draw_board(self) -> None:
        '''
        Draws the board and its tiles to the window.
        '''

        # remove existing board to redraw (if it exists)
        try:
            self.layout_current.removeWidget(self.board_widget)
        except AttributeError:
            pass

        # create a widget to hold the board's layout
        self.board_widget = QFrame()
        
        # create a layout to hold the tiles of the board
        self.board_layout = QGridLayout()

        # add tiles to the board, using `Game.board`
        for x in range(len(self.GameObj.board[0])):
            for y in range(len(self.GameObj.board)):
                # use a clickable `QLabel` for each tile
                # since we can set `QFrame` styling options on `QLabel`s
                # which you can't do on a `QPushButton`
                psuedo_button = QLabel()
                match self.GameObj.board[y][x]:
                    case 0:
                        psuedo_button.setPixmap(
                            qta.icon('msc.blank').pixmap(QSize(128,128))
                        )
                    case 1:
                        psuedo_button.setPixmap(
                            qta.icon('msc.circle-large').pixmap(QSize(128,128))
                        )
                    case 2:
                        psuedo_button.setPixmap(
                            qta.icon('msc.chrome-close').pixmap(QSize(128,128))
                        )

                psuedo_button.setFrameStyle(
                    QFrame.Shape.Panel | QFrame.Shadow.Raised
                )
                psuedo_button.setLineWidth(2)
                psuedo_button.setScaledContents(True)
                psuedo_button.mousePressEvent = lambda event, pos=(x,y): \
                    self.GameObj.take_turn(pos)

                # add the tile to the board layout
                self.board_layout.addWidget(psuedo_button,y,x)

                # remove the tile variable from memory
                # not necessarily needed as we reinitialise next anyway
                del psuedo_button

        # set the layout container the tiles onto the board widget
        self.board_widget.setLayout(self.board_layout)

        # style the board widget
        self.board_widget.setFrameStyle(
            QFrame.Shape.Panel | QFrame.Shadow.Sunken
        )
        self.board_widget.setLineWidth(2)

        # add the widget to window's layout
        self.layout_current.addWidget(self.board_widget, 1, 1)

        # set the layout
        self.layout_widget.setLayout(self.layout_current)

        return

    def inform_win(self, win_state: str) -> True | False:
        '''
        Creates a dialog window to inform the user of who has won or if
        there was a draw and to ask what to do next.
        '''

        # pop-up window
        match win_state:
            case 'win':
                choice = QMessageBox.question(
                    self,
                    f'Player {self.GameObj.current_player} has won!',
                    f'Player {self.GameObj.current_player} has won!\n'
                        +'Would you like to play again?'
                )
            case 'draw':
                choice = QMessageBox.question(
                    self,
                    'There is a draw!',
                    'There is a draw!\n'
                        +'Would you like to play again?'
                )

        # convert values to a normal `bool`
        match choice:
            case QMessageBox.StandardButton.Yes:
                return True
            case QMessageBox.StandardButton.No:
                return False

    def inform_invalid(self, op: str) -> None:
        '''
        Informs the user of an invalid operation, `op`.
        '''

        # pop-up window
        # future: add a message across the bottom of the window instead
        QMessageBox.information(
            self,
            'Invalid Operation',
            f'Invalid {op}.'            
        )

        return


def main() -> None:
    '''
    Controls the main program flow.
    '''

    # creates the window
    AppObj = QApplication([])
    WindowObj = GUI_Interface(AppObj)
    WindowObj.show()

    # hands control of the program flow over to PyQt
    AppObj.exec()
   
    return


# only execute if called directly
if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print()
        sys.exit()
