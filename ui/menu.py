import PySimpleGUI as sg
from ui.api import UIView



class MainMenu(UIView):

    def render(self) -> list:
        return [
                [sg.Text('hwidahwidhawihdiaw')],
                [sg.Button('Play', key='play_button')],
                [sg.Button('Play Histories', key='histories_button')]
        ]

    def listeners(self) -> dict:
        return {
            'play_button': self.on_click_play,
            'histories_button': self.on_click_history
        }

    def on_click_play(self, values):
        print('user clicked play: ', values)
        self.switch_page('play')

    def on_click_history(self, values):
        print('user clicked histories', values)





