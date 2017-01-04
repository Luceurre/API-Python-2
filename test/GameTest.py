import pygame

import Game
from test.StageInit import StageInit


class GameTest(Game.Game):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.stage_manager.push(StageInit())

        self.start()
