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
from collections.abc import Callable
from typing import Any

import qtawesome as qta
from PyQt6.QtCore import QSize, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QHBoxLayout,
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
        self.GameObj.setup_game(gametype='cpu')

        # stores the QApplication object for later use in `_quit()`
        self.AppObj = _AppObj

        # sets title
        self.setWindowTitle('Noughts & Crosses Qt6')

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

    def _delay(self, length: int, func: Callable[[], Any]) -> None:
        '''
        Waits a fixed amount of time before running the function.
        '''

        # creates a timer that runs once when the time expires
        self.delay_timer = QTimer()
        self.delay_timer.setSingleShot(True)
        self.delay_timer.timeout.connect(func)

        # starts the timer
        self.delay_timer.start(length)

        return

    def _event(self, func: Callable[[...], Any], args: list[...]) -> None:
        '''
        Handles user input events.
        '''

        # test if a timer exists
        try:
            # test is the timer is active
            if not self.delay_timer.isActive():
                func(*args)        
        except AttributeError:
            func(*args)        
        
        return

    def draw_info(self) -> None:
        '''
        Draws the info tiles to the window.
        '''

        # remove existing info to redraw (if it exists)
        try:
            self.layout_current.removeWidget(self.info_widget)
        except AttributeError:
            pass

        # create a widget to hold the info's layout
        self.info_widget = QFrame()
        
        # create a layout to hold the tiles of the info
        self.info_layout = QHBoxLayout()

        # create widget for first player's score
        score_widget_1 = QLabel(
            str(self.GameObj.current_game[0]['score']).zfill(3)
        )
        score_widget_1.setFrameStyle(
            QFrame.Shape.Panel | QFrame.Shadow.Raised 
        )
        score_widget_1.setLineWidth(4)
        self.info_layout.addWidget(score_widget_1)

        # create widget for title
        title_widget = QLabel('<h1>Noughts & Crosses Qt6</h1>')
        self.info_layout.addWidget(title_widget)

        # create widget for second player's score
        score_widget_2 = QLabel(
            str(self.GameObj.current_game[1]['score']).zfill(3)
        )
        score_widget_2.setFrameStyle(
            QFrame.Shape.Panel | QFrame.Shadow.Raised 
        )
        score_widget_2.setLineWidth(4)
        self.info_layout.addWidget(score_widget_2)

        # set the layout containing the tiles onto the info widget
        self.info_widget.setLayout(self.info_layout)

        # set options for the frame        
        self.info_widget.setFrameStyle(
            QFrame.Shape.Panel | QFrame.Shadow.Sunken 
        )
        self.info_widget.setLineWidth(4)

        # add the widget to window's layout
        self.layout_current.addWidget(self.info_widget, 0, 0)

        # set the layout
        self.layout_widget.setLayout(self.layout_current)

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

                # sets options for our 'button'
                psuedo_button.setFrameStyle(
                    QFrame.Shape.Panel | QFrame.Shadow.Raised
                )
                psuedo_button.setLineWidth(4)
                psuedo_button.setScaledContents(True)
                psuedo_button.mousePressEvent = lambda event, pos=(x,y): \
                    self._event(self.GameObj.take_turn, [pos])

                # add the tile to the board layout
                self.board_layout.addWidget(psuedo_button,y,x)

        # set the layout containing the tiles onto the board widget
        self.board_widget.setLayout(self.board_layout)

        # style the board widget
        self.board_widget.setFrameStyle(
            QFrame.Shape.Panel | QFrame.Shadow.Sunken
        )
        self.board_widget.setLineWidth(4)

        # add the widget to window's layout
        self.layout_current.addWidget(self.board_widget, 1, 0)

        # set the layout
        self.layout_widget.setLayout(self.layout_current)

        # draw info panels to match the updated board
        self.draw_info()

        return

    def inform_win(self, win_state: str) -> True | False:
        '''
        Creates a dialog window to inform the user of who has won or if
        there was a draw and to ask what to do next.
        '''

        # get the winning player's name
        win_player_name = self.GameObj.current_game[
            self.GameObj.current_player - 1
        ][
            'name'
        ]

        # pop-up window
        match win_state:
            case 'win':
                choice = QMessageBox.question(
                    self,
                    f'{win_player_name} has won!',
                    f'{win_player_name} has won!\n'
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
