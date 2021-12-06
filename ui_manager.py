from tkinter.constants import CENTER
import PySimpleGUI as sg
from threading import Thread
from ui.api import UIView


TITLE = 'Play Tic Tae Toe With AI'

gui_map = {}

def add_gui(key: str, ui: UIView):

    if type(ui) == type:
        ui = ui()

    ui.switch_page = switch_page

    gui_map[key] = {
        'layout': ui.render(),
        'listeners': ui.listeners(),
        'event_handle': ui.on_event
    }


window = None


current_page = 'main'

def run(thread=True):
    global window

    if window:
        raise Exception('Window already started.')

    if 'main' not in gui_map:
        raise Exception('no main ui')

    if thread:
        Thread(target=run_until_close).start()
    else:
        run_until_close()
    
def run_until_close():

    global window

    layout = []
    for key, ui in gui_map.items():

        column = sg.Column(
            layout=ui['layout'], 
            key=key, 
            visible=key == 'main', 
            element_justification=CENTER, 
            justification=CENTER,
            pad=(5, 5))
        layout.append([column])

    window = sg.Window(TITLE, layout, finalize=True, size=(500, 500))

    while True:

        event, values = window.read()

        if event in [sg.WIN_CLOSED, sg.TITLEBAR_CLOSE_KEY]:
            break

        gui = gui_map[current_page]

        result = False

        if event in gui['listeners']:
            result = gui['listeners'][event](values)
        else:
            result = gui['event_handle'](event, values)

        if result:
            break

    window.close()
    window = None


def switch_page(key: str):

    global window, current_page

    print(f'switching page from {current_page} to {key}')

    if not window:
        raise Exception('Window not started')

    if key not in gui_map:
        raise Exception(f'ui {key} not found')

    if current_page:
        window[current_page].hide_row()
        window[current_page].update(visible=False)

    window[key].unhide_row()
    window[key].update(visible=True)
    current_page = key


