import random
from typing import List
import PySimpleGUI as sg


def random_select(selectable) -> sg.Button:
    return random.choice(selectable)

def to_map(grids: List[List[sg.Button]]) -> dict:
    grid_map = {}
    for row in grids:
        for btn in row:
            _, x, y = btn.Key
            grid_map[(x, y)] = btn.GetText()
    return grid_map

# min max strategy

def min_max(grids):

    grid_map = to_map(grids)

    scores = {}

    for pos in possible_moves(grid_map):
        scores[pos] = min_max_algorithm(True)

    max_score, max_button = -4, None

    for button, score in scores.items():
        print(f'{button.Key}: {score}')
        if score > max_score:
            max_score, max_button = score, button

    return max_button

    



def min_max_algorithm(
        maxer: bool, 
        grid_map: dict
    ) -> int:
    
    _, x, y = button.Key
    if not seletable:
        if is_over():
            return 0
        return 1 if is_win(x, y) else -1
       

    scores = []

    for move in seletable:
        new_seletable = list(filter(lambda m: m != move, seletable))
        move.update(text='X' if maxer else 'O')
        scores.append(min_max_algorithm(not maxer, new_seletable, is_win, is_over, move))
        move.update(text=' ') # revert

    if maxer:
        return max(scores)
    else:
        return min(scores)
    
# alpha beta strategy (with pruning)

def alpha_beta(seletable) -> sg.Button:
    pass

# simulate

def possible_moves(grid_map):
    possible_move = []
    for pos, mark in grid_map.items():
        if mark == ' ':
            possible_move.append(pos)

    return possible_move

def is_winner(grid_map) -> bool:
    pass

def is_draw(grid_map) -> bool:
    pass

