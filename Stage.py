import pygame

from EventHandler import EventHandler
from StageState import StageState
from Logger import Logger


class Stage(EventHandler, Logger):
    def __init__(self):
        self.state = StageState.INIT
        self.actors = []

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
       pass

    def pause(self):
        # Called each tick when StageState is PAUSE
        pass

    def events_loop(self):
        events = pygame.event.get()

        for index, event in enumerate(events):
            if not self.handle(event):
                for actor in sorted(self.actors, key= lambda actor: actor.handle_event, reverse=True):
                    if not actor.handle_event:
                        break
                    if actor.handle(event):
                        break

