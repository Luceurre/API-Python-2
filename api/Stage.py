from operator import attrgetter

import pygame
from api.EventHandler import EventHandler
from api.StageState import StageState
from api.Logger import Logger, LOG_LEVEL
from api.Timer import Timer


class Stage(EventHandler, Logger):
    def __init__(self, screen):
        self.state = StageState.INIT
        self.actors = []
        self.screen = screen
        self.timers = []

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

    """
    def auto_events_loop(self, *args, **kwargs):
        # Créée pour appeler 'events_loop' sans changer sa définition (Timer)

        self.events_loop()
    """

    def events_loop(self):
        actors_sorted = sorted(self.actors, key=attrgetter('handle_event', 'handle_event_priority'), reverse=True)

        for event in pygame.event.get():
            if not self.handle(event):
                for actor in actors_sorted:
                    if not actor.handle_event:
                        break
                    elif actor.handle(event):
                        break

    """
    def auto_draw_actors(self, *args, **kwargs):
        # Créée pour appeler 'draw_actors' sans changer sa définition (Timer)

        self.draw_actors()
    """

    def draw_actors(self):
        for actor in sorted(self.actors, key=attrgetter('should_draw', 'z'), reverse=True):
            if not actor.should_draw:
                break
            else:
                actor.draw(self.screen)

    """
    def auto_update_actors(self, *args, **kwargs):
        # Créée pour appeler 'update_actors' sans changer sa définition (Timer)

        self.update_actors()
    """

    def update_actors(self):
        for actor in sorted(self.actors, key=attrgetter('should_update'), reverse=True):
            if not actor.should_update:
                break
            else:
                actor.update()

    """
    def set_auto_call_events_loop(self, ms = 1000/500):
        self.add_timer(Timer(ms, self.auto_events_loop, repeat=True, infinite=True))

    def set_auto_call_draw_actors(self, ms = 1000/60):
        self.add_timer(Timer(ms, self.auto_draw_actors, repeat=True, infinite=True))

    def set_auto_call_update_actors(self, ms=1000/500):
        self.add_timer(Timer(ms, self.auto_update_actors, repeat=True, infinite=True))

    def set_auto_manage_scene(self, ms_au = 1000/120, ms_ad = 1000/60, ms_el=1000/60):
        self.set_auto_call_update_actors(ms_au)
        self.set_auto_call_draw_actors(ms_ad)
        self.set_auto_call_events_loop(ms_el)
        self.__auto = True
    """

    def add_timer(self, timer):
        self.timers.append(timer)

    def update_timers(self):
        for index, timer in enumerate(self.timers):
            if timer.update():
                self.timers.pop(index)

    def add_actor(self, actor):
        if actor not in self.actors:
            self.actors.append(actor)
        else:
            self.log("Tu as deux fois le même Actor! Check si tu as pas une erreur quelque part Renaud...", LOG_LEVEL.ERROR)