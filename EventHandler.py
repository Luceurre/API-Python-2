import pygame


class EventHandler():
    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            self.handle_keydown(event.unicode, event.key, event.mod)
        elif event.type == pygame.KEYUP:
            self.handle_keyup(event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            self.handle_mouse(event.pos, event.rel, event.buttons)

    def handle_keydown(self, unicode, key, mod):
        pass

    def handle_keyup(self, key, mod):
        pass

    def handle_mouse(self, pos, rel, buttons):
        pass
