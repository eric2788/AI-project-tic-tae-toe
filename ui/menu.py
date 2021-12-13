import PySimpleGUI as sg
from ui.api import UIView



class MainMenu(UIView):

    def render(self) -> list:
        return [
                [sg.Text('Do you want to play Tic Tae Toe with AI ?')],
                [sg.Button('Play', key='play_button')],
                [sg.Button('Played Histories', key='histories_button')]
        ]

    def listeners(self) -> dict:
        return {
            'play_button': self.on_click_play,
            'histories_button': self.on_click_history
        }

    def on_click_play(self, values):
        self.switch_page('play')

    def on_click_history(self, values):
        self.switch_page('histories')





