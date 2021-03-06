from api.StageState import StageState
from api.Stage import Stage


class StageManager():
    """Singleton object - Permet la gestion des Stages"""

    singleton = None

    class __StageManager():
        def __init__(self):
            self.stack = []

        def update(self):
            for object in self.stack:
                object.update()
                object.draw()

            return self.is_empty

        def push(self, object):
            if (object not in self.stack and isinstance(object, Stage)):
                self.stack.append(object)

        def pop(self, index):
            return self.stack.pop(index)

        def exit(self):
            for stage in self.stack:
                stage.state = StageState.QUIT

        def __iter__(self):
            return iter(self.stack)

        @property
        def is_empty(self):
            return len(self.stack) == 0

    def __new__(cls):
        if (cls.singleton == None):
            cls.singleton = cls.__StageManager()

        return cls.singleton
