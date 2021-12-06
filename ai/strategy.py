import random
import PySimpleGUI as sg


def random_select(selectable) -> sg.Button:
    return random.choice(selectable)