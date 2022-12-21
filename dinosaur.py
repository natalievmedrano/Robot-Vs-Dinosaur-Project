from weapons import Weapons
from robot import Robot
class Dinosaurs:

    def __init__(self, name, attack_power):
        self.weapon = Weapons("Razor Claws",20)
        self.name = name
        self.health= 100
        attack_power = attack_power
        self.is_winner = True


    def attack(self,robot ):
         robot.health -= self.weapon.attack_power
         print(f'{self.name} hits DINO with {self.weapon}')
         print(f'ROB has {robot.health} HP REMANING!!!!')
    
       