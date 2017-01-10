from api.Game import Game
from api.StageManager import StageManager
from game.stages.StageLoadingScreen import StageLoadingScreen


class GameNightmareEscape(Game):
    def __init__(self):
        super().__init__(1280, 1024)
        StageManager().push(StageLoadingScreen(self.screen))