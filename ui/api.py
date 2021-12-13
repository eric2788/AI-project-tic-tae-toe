from abc import abstractmethod
from typing import Dict
import PySimpleGUI as sg



class UIView:

    @abstractmethod
    def render(self) -> list:
        return []
        
    @abstractmethod
    def listeners(self) -> dict:
        return {}

    def on_event(self, event, values) -> bool:
        return False
    
    def on_mount(self):
        pass

    def switch_page(self, page):
        pass

    