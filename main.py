# Player Created =
class Player:

    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self, monster, damage):
        monster.health -= damage
        self.energy -= damage # self.energy = self.energy - damage
        if monster.is_attacked():
            self.health -= monster.damage
            print(f"\nPlayer {self.name} Diserang oleh Monster, Sisa darah = {self.health}")
        print(f"Player menyerang monster, Sisa darah Monster = {monster.health}, Energy sisa = {self.energy}")

    def show_info(self, player_number):
        print(f"Informasi Player {player_number}:")
        print(f"Nama player =\t {self.name}")
        print(f"Darah player =\t {self.health}")
        print(f"Energy player =\t {self.energy}")

def created_player (player_number):
    name= input("Masukan nama Player = ")
    health = int(input("Masukan darah Player = "))
    energy = int(input("Masukan Energy Player = "))
    return Player(name, health, energy)

player1 = created_player(1)
player1.show_info(1)

player2 = created_player(2)
player2.show_info(2)

class Monster:
    def __init__(self, health):
        self.health = health #Nilai akan berbubah jika ada serangan
        self.health_init = self.health #Nilai akan tetap 500
        self.damage = 70
        self.name = input("\nMasukan Nama Monster = ")

    def is_attacked(self):
        return self.health < self.health_init

    def show_info(self):
        print(f"Nama monster = {self.name}")
        print(f"Darah monster = {self.health}")

monster = Monster(health = 500)
monster.show_info()
player1.attack(monster, damage=50)
player2.attack(monster, damage=50)
