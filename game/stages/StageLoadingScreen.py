import pygame
from api.Stage import Stage, StageState
from api.StageAutoManage import StageAutoManage
from game.actors.ActorLoadingScreen import ActorLoadingScreen


class StageLoadingScreen(StageAutoManage):
    def init(self):
        self.add_actor(ActorLoadingScreen())
