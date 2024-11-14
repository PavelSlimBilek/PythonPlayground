from Enemy import Enemy
from Player import Player

player = Player("Slim", 100, 15)
enemy = Enemy("Mára", 10, 1)

print(player.__str__())
print(enemy.__str__())

player.take_damage(enemy.damage)
print(player)
enemy.take_damage(player.damage)
print(enemy)

if enemy.health > 0:
    print(f"{enemy.name} is alive!")
else:
    print(f"{enemy.name} is dead! Yes!!'")

print(f"{player.name} has won! YES!!")