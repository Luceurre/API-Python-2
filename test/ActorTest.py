from Actor import Actor


class ActorTest(Actor):
    def handle_keydown(self, unicode, key, mod):
        if unicode == "z":
            print("ACTOR WORKS!")
            return True
        else:
            return False