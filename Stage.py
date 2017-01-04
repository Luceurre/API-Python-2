import pygame

from EventHandler import EventHandler
from StageState import StageState


class Stage(EventHandler):
    def __init__(self):
        self.state = StageState.INIT

    def update(self):
        """Ici se passe toute la logique de la scène"""

    def draw(self):
        """Ici se passe tout ce qui est affiché à l'écran"""

    # Callbacks functions (StateManager)

    def resume(self):
        # Called when StageState changes from PAUSE to RUN
        pass

    def quit(self):
        # Called when StageState is QUIT (should be called once per instance)
        pass

    def init(self):
        # Called when StageState is INIT (should be called once per instance)
        pass

    def run(self):
        # Called each tick when StageState is RUN
        for event in pygame.event.get():
            self.handle(event)

    def pause(self):
        # Called each tick when StageState is PAUSE
        pass
