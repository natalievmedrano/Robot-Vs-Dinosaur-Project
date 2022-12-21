from weapons import Weapons

class Robot:

 def __init__(self, name):
    self.name= name
    self.health= 100
    self.weapons= Weapons('Flame Thrower',20)
    self.is_winner = True

 def attack(self, dinosaur):
        dinosaur.health -= self.weapons.attack_power
        print()
        print(f'{self.name} hits DINO with {self.weapons}')
        print(f'DINO has {dinosaur.health} HP REMANING!!!!')
        print()



          
        
          
        


