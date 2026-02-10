from player import Player
from enemy import Enemy
import animation as A
import random
import frame as F


class Battle:

    def __init__(self):
        self.player = Player("Player", 50, random.randint(10, 15))
        self.enemy = Enemy("Enemy", 50, random.randint(10, 15))

    def battling(self):
        
        F.intro()

        while self.player.is_alive() and self.enemy.is_alive():

            A.clear()
            A.animate("\n1. Attack")
            choice = A.input_animation("\nChoose: ")

            if choice == "1":

                # Player attacks enemy
                F.sword_player()
                self.enemy.hp -= self.player.atk. 
                A.animate(f"Player deals {self.player.atk} damage!")

                if not self.enemy.is_alive():
                    A.clear()
                    A.animate("\nEnemy is Dead!")
                    break

                # Enemy attacks player
                F.sword_enemy()
                self.player.hp -= self.enemy.atk
                A.animate(f"Enemy deals {self.enemy.atk} damage!")

                if not self.player.is_alive():
                    A.clear()
                    A.animate("Player is Dead!")
                    break

            A.clear()
            A.animate(f"Player HP: {self.player.hp}")
            A.clear()
            A.animate(f"Enemy HP: {self.enemy.hp}")
