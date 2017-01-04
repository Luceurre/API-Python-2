import Stage
from StageManager import StageManager
from StageState import StageState
from test.StageMenu import StageMenu


class StageInit(Stage.Stage):
    def init(self):
        print("Je me suis initilialisé !")
        StageManager().push(StageMenu())
        self.state = StageState.QUIT

    def quit(self):
        print("Adieu :'(")
