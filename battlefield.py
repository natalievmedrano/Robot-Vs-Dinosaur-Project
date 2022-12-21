from robot import Robot
from dinosaur import Dinosaurs

class Battlefield:
    def __init__(self) -> None:
        self.robot= Robot('Rob')
        self.dino= Dinosaurs('Henry',20)



    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("WELCOME TO ROBOTS VS DINOSAURS!")
        print()
        print("WHO WILL WIN? ARE YOU READY?")
        print()


    def battle_phase(self):
        while self.robot.health >= 0 and self.dino.health >= 0 :
         self.robot.attack(self.dino)
         self.dino.attack(self.robot)

    def display_winner(self):
        print()
        if self.robot.health < 0:
            print(f'{self.dino.name} is the winnner!')
        else:
            print(f'{self.robot.name} is the winner!!')
        print()
