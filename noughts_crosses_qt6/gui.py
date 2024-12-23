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

    def __init__(self) -> None:
        '''
        Sets up the gui and handles the main program loop after exec is
        handed over.
        '''

        # initialises from QMainWindow
        super().__init__()

        # initialise object
        self.GameObj = Game('cpu')
        self.GameObj.InterfaceObj = self

        # creates a widget to hold our layout
        self.layout_widget = QWidget()
        self.setCentralWidget(self.layout_widget)

        # creates a layout to hold our widgets
        self.layout_current = QGridLayout()
        self.layout_widget.setLayout(self.layout_current)

        # draws our initial board to the screen
        self.draw_board()

        return

    def update_board(self, pos: tuple[int,int]) -> None:
        '''
            
        '''

        self.GameObj.board[pos[1]][pos[0]] = 1
        self.draw_board()

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
                psuedo_button = QLabel(str(self.GameObj.board[y][x]))
                psuedo_button.setFrameStyle(
                    QFrame.Shape.Panel | QFrame.Shadow.Raised
                )
                psuedo_button.setLineWidth(2)
                psuedo_button.mousePressEvent = lambda event, pos=(x,y): \
                    self.update_board(pos)

                # add the tile to the board layout
                self.board_layout.addWidget(psuedo_button,y,x)

                # remove the tile variable from memory
                # not necessarily needed as we reinitialise next anyway
                del psuedo_button

        # set the layout container the tiles onto the board widget
        self.board_widget.setLayout(self.board_layout)

        # style the board widget
        self.board_widget.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        self.board_widget.setLineWidth(2)

        # add the widget to window's layout
        self.layout_current.addWidget(self.board_widget, 1, 1)

        # set the layout
        self.layout_widget.setLayout(self.layout_current)

        return

def main() -> None:
    '''
    Controls the main program flow.
    '''

    # creates the window
    AppObj = QApplication([])
    WindowObj = GUI_Interface()
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
