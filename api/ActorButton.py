import enum
from api.ActorSprite import ActorSprite

class BUTTON_STATE(enum.Enum):
    NORMAL = enum.auto()
    HOVERED = enum.auto()
    PRESSED = enum.auto()

class ActorButton(ActorSprite):
    def __init__(self, sprites=None):
        super().__init__()
        if sprites is not None:
            self.sprites = sprites
            self.sprite = self.sprites[BUTTON_STATE.NORMAL]

        self.button_state = BUTTON_STATE.NORMAL
        self.previous_button_state = BUTTON_STATE.NORMAL
        self.handle_event = True

    def handle_mouse(self, pos, rel, buttons):
        if self.rect.collidepoint(pos[0], pos[1]):
            self.previous_button_state = self.button_state
            self.button_state = BUTTON_STATE.HOVERED
        else:
            self.previous_button_state = self.button_state
            self.button_state = BUTTON_STATE.NORMAL

        self.sprite = self.sprites[self.button_state]


    @property
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, sprites):
        self.__sprites = sprites
        self.sprite = sprites[self.button_state]

    # Quelques méthodes utiles :

    def did_change(self):
        return self.button_state == self.previous_button_state