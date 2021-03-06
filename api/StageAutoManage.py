from api.Stage import Stage


class StageAutoManage(Stage):
    def __init__(self, screen):
        super().__init__(screen)

        self.auto_manage = True

    def run(self):
        super().run()

        if self.auto_manage:
            self.events_loop()

            self.update()
            self.draw()

    def update(self):
        super().update()

        if self.auto_manage:
            self.update_timers()
            self.events_loop()
            self.update_actors()

    def draw(self):
        super().draw()

        if self.auto_manage:
            self.draw_actors()