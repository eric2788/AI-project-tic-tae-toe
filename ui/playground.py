import PySimpleGUI as sg
from ui.api import UIView


MAX_ROWS = 3
MAX_COLUMNS = 3

class PlayGround(UIView):

    def __init__(self) -> None:
        super().__init__()
        self.player_round = True
        self.indicator = sg.Text('Round: Your Turn')
        self.grids = [[sg.Button(' ', size=(10, 5), key=(i*3+j+1, i, j), pad=(0, 0)) for j in range(MAX_ROWS)] for i in range(MAX_COLUMNS)]


        self.possible_wins_line = [
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2))
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
        self.player_round = not self.player_round
        self.indicator.update(value=f"Round: {'AI Turn' if not self.player_round else 'Your Turn'}")
        self.grids[x][y].update(text='X' if not self.player_round else 'O')
        
        possible_wins = []

        for winnable in self.possible_wins_line:
            if (x, y) in winnable:
                possible_wins.append(winnable)

        for winnable in self.possible_wins_incline:
            if (x, y) in winnable:
                possible_wins.append(winnable)


        win = self.is_win(possible_wins)

        if win:
            sg.Popup(f'{"You" if self.player_round else "AI"} Win', title='Game Over')
            return True

        if self.is_over():
            sg.Popup('Game Draw', title='Game Over')
            return True

        
        return False


    def is_win(self, possible_wins) -> bool:
        #print(possible_wins)
        for (a, b, c) in possible_wins:
            (ax, ay) = a
            (bx, by) = b
            (cx, cy) = c
            if self.grids[ax][ay].GetText() == self.grids[bx][by].GetText() == self.grids[cx][cy].GetText():
                return True
        return False

    def is_over(self) -> bool:
        for row in self.grids:
            for box in row:
                if box.GetText() == ' ':
                    return False
        return True
