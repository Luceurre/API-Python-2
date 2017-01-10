import enum

from api.EventHandler import EventHandler

from api.Logger import Logger

class HANDLE_EVENT_PRIORITY(enum.Enum):
    VERY_LOW = enum.auto()
    LOW = enum.auto()
    NORMAL = enum.auto()
    HIGH = enum.auto()
    VERY_HIGH = enum.auto()

    def __lt__(self, other):
        return self.value < other.value

class Actor(EventHandler, Logger):
    def __init__(self):
        self.handle_event = False
        self.handle_event_priority = HANDLE_EVENT_PRIORITY.NORMAL
        self.should_draw = False
        self.z = 0
        self.should_update = False
        self.timers = []

    def draw(self):
        # L'Actor doit être dessiné ici, si c'est un Actor avec une image, utilise ActorSprite
        pass

    def update(self):
        # L'Actor doit être mis à jour ici -> Mouvement, Collision, etc...
        pass

    def add_timer(self, timer):
        self.timers.append(timer)

    def update_timers(self):
        for index, timer in enumerate(self.timers):
            if timer.update():
                self.timers.pop(index)

    # Quelques methodes pour aider :

    def set_centered(self, width, height):
        self.rect.x = (width - self.rect.width) / 2
        self.rect.y = (height - self.rect.height) / 2
