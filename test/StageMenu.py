import Stage
from StageManager import StageManager


class StageMenu(Stage.Stage):
    def init(self):
        print("Je suis le MENU")

    def handle_keydown(self, unicode, key, mod):
        if (key == 27):
            StageManager().exit()
