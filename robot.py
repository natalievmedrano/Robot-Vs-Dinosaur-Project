from weapon import Weapons

class Robot:

 def __init__(self, name):
    self.name= name
    self.health= 100
    self.attack_power= 100
    self.weapons= Weapons('Flame Thrower',20)

 def attack(self, dinosaur):
        pass