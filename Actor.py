from EventHandler import EventHandler
from Logger import Logger


class Actor(EventHandler, Logger):
    def __init__(self):
        self.handle_event = False
        self.age = 3