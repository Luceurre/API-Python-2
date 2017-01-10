import pygame
from api.Actor import Actor
from api.Logger import LOG_LEVEL
from api.StageManager import StageManager


class ActorSprite(Actor):
    def __init__(self, sprite=None):
        super().__init__()

        # Définition de nouveaux attributs
        self.rect = pygame.Rect(0, 0, 0, 0)
        if sprite is not None:
            self.sprite = sprite

        # Modification d'attribut venant de la classe Actor
        self.should_draw = True

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        if not isinstance(sprite, pygame.Surface):
            self.log("Le Sprite n'est pas valide!", LOG_LEVEL.ERROR)
            StageManager().exit()
        else:
            self.rect.width = sprite.get_width()
            self.rect.height = sprite.get_height()
            self.__sprite = sprite

    def draw(self, screen):
        if not isinstance(self.sprite, pygame.Surface):
            self.log("Le Sprite n'est pas valide!", LOG_LEVEL.ERROR)
            StageManager().exit()
        else:
            screen.blit(self.sprite, self.rect)