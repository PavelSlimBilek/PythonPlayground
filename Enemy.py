from Entity import Entity


class Enemy(Entity):

    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)