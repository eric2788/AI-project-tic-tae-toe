import math
import random
from typing import List
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import main_get_debug_data


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

    max_score, max_pos = -math.inf, None

    for pos in possible_moves(grid_map):
        grid_map[pos] = 'X'
        score = min_max_algorithm(False, grid_map)
        grid_map[pos] = ' '
        if score > max_score:
            max_score, max_pos = score, pos

    return max_pos


def min_max_algorithm(
    maxer: bool,
    grid_map: dict
) -> int:

    winner = get_winner(grid_map)
    moves = possible_moves(grid_map)
    if winner:
        return 1 if winner == 'X' else -1
    elif not moves:
        return 0

    scores = []

    for move in moves:
        grid_map[move] = 'X' if maxer else 'O'
        scores.append(min_max_algorithm(not maxer, grid_map))
        grid_map[move] = ' '

    if maxer:
        return max(scores)
    else:
        return min(scores)

# alpha beta strategy (with pruning)

def alpha_beta(grids):
    grid_map = to_map(grids)

    max_score, max_pos = -math.inf, None

    for pos in possible_moves(grid_map):
        grid_map[pos] = 'X'
        score = alpha_beta_min_max_alogithm(0, False, grid_map)
        grid_map[pos] = ' '
        if score > max_score:
            max_score, max_pos = score, pos

    return max_pos


def alpha_beta_min_max_alogithm(
        depth: int,
        maximizer: bool,
        grid_map: dict,
        alpha: int = -math.inf,
        beta: int = math.inf,
        MIN=-math.inf,
        MAX=math.inf
) -> int:

    winner = get_winner(grid_map)
    moves = possible_moves(grid_map)

    if winner:
        return 1 if winner == 'X' else -1
    elif not moves:
        return 0

    if maximizer:
        best = MIN

        for move in moves:

            grid_map[move] = 'X'
            value = alpha_beta_min_max_alogithm(depth + 1, False, grid_map, alpha, beta)
            grid_map[move] = ' '

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for move in moves:

            grid_map[move] = 'O'
            value = alpha_beta_min_max_alogithm(depth + 1, True, grid_map, alpha, beta)
            grid_map[move] = ' '

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

# simulate


def possible_moves(grid_map):
    possible_move = []
    for pos, mark in grid_map.items():
        if mark == ' ':
            possible_move.append(pos)

    return possible_move


def get_winner(grid_map) -> str:
    possible_wins = [
        # vertical
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        # horizontal
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        # incline
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    ]
    for (a, b, c) in possible_wins:
            (ax, ay) = a
            (bx, by) = b
            (cx, cy) = c

            if grid_map[(ax, ay)] == grid_map[(bx, by)] == grid_map[(cx,cy)] == 'X':
                return 'X'

            if grid_map[(ax, ay)] == grid_map[(bx, by)] == grid_map[(cx,cy)] == 'O':
                return 'O'

    return None


def is_draw(grid_map) -> bool:
    for v in grid_map.values():
        if v == ' ':
            return False
    return True
