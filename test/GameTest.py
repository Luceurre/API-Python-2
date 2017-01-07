import pygame

import Game
from test.StageInit import StageInit
from Logger import Logger, LOG_LEVEL


class GameTest(Game.Game, Logger):
    def __init__(self):
        super().__init__()

        pygame.init()
        # On définit le niveau de LOG de l'application
        self.set_log_level(LOG_LEVEL.DEBUG)

        self.stage_manager.push(StageInit())

        self.start()
