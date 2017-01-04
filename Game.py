from StageManager import StageManager
from StageState import StageState


class Game:
    """Don't know why I made this..."""

    def __init__(self):
        self.stage_manager = StageManager()

    def start(self):
        """Called when you want the game to start -> unless you're using multi-threading, you won't be able to do
        anything until your game ends """

        while not self.stage_manager.is_empty:
            for index, stage in enumerate(self.stage_manager):
                if stage.state == StageState.RUN:
                    stage.run()
                elif stage.state == StageState.PAUSE:
                    stage.pause()
                elif stage.state == StageState.RESUME:
                    stage.state = StageState.RUN
                    stage.resume()
                elif stage.state == StageState.INIT:
                    stage.state = StageState.RUN
                    stage.init()
                elif stage.state == StageState.QUIT:
                    self.stage_manager.pop(index)
                    stage.quit()
