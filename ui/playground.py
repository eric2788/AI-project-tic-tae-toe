from typing import List
import PySimpleGUI as sg
import ai
from ui.api import UIView
import threading


MAX_ROWS = 3
MAX_COLUMNS = 3

class PlayGround(UIView):

    def __init__(self) -> None:
        super().__init__()
        self.player_round = True
        self.indicator = sg.Text('Round: Your Turn')
        self.grids = [[sg.Button(' ', size=(10, 5), key=(i*3+j+1, i, j), pad=(0, 0)) for j in range(MAX_ROWS)] for i in range(MAX_COLUMNS)]


        self.possible_wins_line = [
            # vertical
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            # horizontal
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2))
        ]

        self.possible_wins_incline = [
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0))
        ]

    def render(self) -> list:
        return [

            [ self.indicator ],

        ] + self.grids


    # key not stable so use on_event
    def on_event(self, event, values) -> bool:
        print(f'user clicked {event}')
        _, x, y = event

        if self.grids[x][y].GetText() != ' ':
            return

        is_end = self.handle_click(x, y, 'O' if self.player_round else 'X')

        if is_end:
            return is_end

        if self.player_round == False:
            self.AI_turn()
        
        return False

    def handle_click(self, x, y, mark) -> bool:
        self.grids[x][y].update(text=mark)

        winner = self.get_winner(x, y)

        if winner:
            sg.Popup(f"{'You' if winner == 'O' else 'AI'} won", title='Game Over')
            return True

        if self.is_over():
            sg.Popup('Game Draw', title='Game Over')
            return True

        self.player_round = not self.player_round
        self.indicator.update(value=f"Round: {'AI Turn' if not self.player_round else 'Your Turn'}")

        return False


    def AI_turn(self):
        self.indicator.update(value='Round: AI Turn (thinking...)')
        (x, y) = ai.min_max(self.grids)
        return self.grids[x][y].Click()
        

    def possible_moves(self) -> List[sg.Button]:
        selectable = []

        for row in self.grids:
            for btn in row:
                if btn.GetText() == ' ':
                    selectable.append(btn)
        return selectable


    def get_winner(self, x, y) -> str:
        possible_wins = []

        for winnable in self.possible_wins_line:
            if (x, y) in winnable:
                possible_wins.append(winnable)

        for winnable in self.possible_wins_incline:
            if (x, y) in winnable:
                possible_wins.append(winnable)

        if not possible_wins:
            return False
            
        #print(possible_wins)
        for (a, b, c) in possible_wins:
            (ax, ay) = a
            (bx, by) = b
            (cx, cy) = c

            if self.grids[ax][ay].GetText() == self.grids[bx][by].GetText() == self.grids[cx][cy].GetText():
                return self.grids[ax][ay].GetText()

        return None

    def is_over(self) -> bool:
        for row in self.grids:
            for box in row:
                if box.GetText() == ' ':
                    return False
        return True
