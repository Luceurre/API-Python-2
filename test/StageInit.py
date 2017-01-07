import Stage
from StageManager import StageManager
from StageState import StageState
from test.StageMenu import StageMenu
from Logger import LOG_LEVEL


class StageInit(Stage.Stage):
    def init(self):
        StageManager().push(StageMenu())
        self.state = StageState.QUIT

        self.warning("Ton programme ne fait actuellement rien...")
