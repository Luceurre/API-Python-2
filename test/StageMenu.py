import Stage
from StageManager import StageManager
from test.ActorTest import ActorTest


class StageMenu(Stage.Stage):
    def init(self):
        for i in range(10):
            self.actors.append(ActorTest())
        self.actors[4].handle_event = True
        self.actors[8].handle_event = True
        self.actors[2].handle_event = True

    def run(self):
        self.events_loop()

    def handle_keydown(self, unicode, key, mod):
        if (key == 27):
            StageManager().exit()
