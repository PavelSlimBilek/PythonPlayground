from Entity import Entity


class Player(Entity):

    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.level = 1
        self.xp = 0
