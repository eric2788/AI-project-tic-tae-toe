import PySimpleGUI as sg
import ui_manager
import ui

sg.theme('Dark Gray 6')


if __name__ == '__main__':

    ui_manager.add_gui('main', ui.MainMenu)
    ui_manager.add_gui('play', ui.PlayGround)

    ui_manager.run()