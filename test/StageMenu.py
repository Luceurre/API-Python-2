from api.Actor import HANDLE_EVENT_PRIORITY
from api.StageManager import StageManager

from api import Stage
from test.ActorButtonTest import ActorButtonTest
from test.ActorTest import ActorTest


class StageMenu(Stage.Stage):
    def init(self):
        for i in range(1):
            self.add_actor(ActorButtonTest())

        self.actors[0].set_centered(640, 480)


    def run(self):
        self.events_loop()
        self.draw_actors()

    def handle_keydown(self, unicode, key, mod):
        if (key == 27):
            StageManager().exit()
