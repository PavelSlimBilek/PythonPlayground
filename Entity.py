

class Entity:

    def __init__(self, name: str, health: int, damage: int):
        self.name: str = name
        self.health: int = health
        self.damage: int = damage

    def __repr__(self) -> str:
        return f"Entity('{self.__class__.__name__}','{self.name}','{self.health}')"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} - {self.name} has {self.health} health"

    def take_damage(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0
