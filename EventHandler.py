import pygame


class EventHandler():
    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            return self.handle_keydown(event.unicode, event.key, event.mod)
        elif event.type == pygame.KEYUP:
            return self.handle_keyup(event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            return self.handle_mouse(event.pos, event.rel, event.buttons)
        else:
            return False

    def handle_keydown(self, unicode, key, mod):
        return False

    def handle_keyup(self, key, mod):
        return False

    def handle_mouse(self, pos, rel, buttons):
        False
