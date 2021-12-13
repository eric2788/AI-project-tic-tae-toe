from ui.api import UIView
from history_manager import list_records
import PySimpleGUI as sg


class HistoriesList(UIView):

    def __init__(self) -> None:
        super().__init__()
        self.records = [ [sg.Text('', auto_size_text=True)] for i in range(10)]  # mostly 10 lines

    def render(self) -> list:
        return [
            [
                sg.Text("Played Histories", size=(12, 2),
                        font='bold', auto_size_text=True)
            ],
        ] + self.records + [
            [sg.Button(button_text='Back To Main Menu', key='back-menu')]
        ]

    def on_mount(self):
        print('played histories on mount')
        records = list_records()
        lines = [line for line in records] if records else [
            '(No Played Histories.)']
        for i in range(len(lines)):
            if i == 10:
                break
            self.records[i][0].update(value=lines[i])

    def listeners(self) -> dict:
        return {
            'back-menu': self.on_back_menu
        }

    def on_back_menu(self, values):
        self.switch_page('main')
