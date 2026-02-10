from player import Player
from enemy import Enemy
import animation as A
import random
import frame as F
import time


class Battle:

    def __init__(self):
        self.player = Player("Player", 50)
        self.enemy = Enemy("Enemy", 50)
        
    def picking(self):
        A.animate("Lief Game",speed=0.03)
        A.animate("\n1. Introduction",speed=0.03)
        A.animate("\n2. Skip Introduction",speed=0.03)
        pick = A.input_animation("\nChoose: ")
        while True:
            if pick == "1":
                self.battling()
            elif pick == "2":
                self.skip_intro()
            else:
                A.animate("Invalid Answer")

            

    def battling(self):
        
        F.intro()

        while self.player.is_alive() and self.enemy.is_alive():

            A.clear()
            A.animate("\n======================================",speed=0.01)
            A.animate("\nReminders:")
            A.animate("\nBoth participant has standard of 50 HP")
            A.animate("\nYou cannot use heal skill if HP is full")
            A.animate("\n--------------------------------------",speed=0.01)
            A.animate("\n1. Attack")
            A.animate("\n2. Heal")
            #A.animate("\n3. Ultimate skill")
            choice = A.input_animation("\nChoose: ")

            if choice == "1":

                # Player attacks enemy
                F.sword_player()
                dmg = self.player.attack()
                self.enemy.hp -= dmg
                A.animate(f"Player deals {dmg} damage!")

                if not self.enemy.is_alive():
                    A.clear()
                    A.animate("\nEnemy is Dead!")
                    break

                # Enemy attacks player
                F.sword_enemy()
                damage = self.enemy.attack()
                self.player.hp -= damage
                A.animate(f"Enemy deals {damage} damage!")

                if not self.player.is_alive():
                    A.animate("Player is Dead!")
                    break
            
            elif choice == "2":
                
                #heal player
                if self.player.hp == 50:
                        A.animate("Player HP is full")
                        time.sleep (1)
                        pass
                else:
                    if self.player.hp < 50:
                        F.heal_animation()
                        hp_heal = self.player.heal()
                        self.player.hp += hp_heal
                        A.animate(f"Healing: + {hp_heal}")
                
                        #enemy attack
                        F.sword_enemy()
                        damage = self.enemy.attack()
                        self.player.hp -= damage
                        A.animate(f"Enemy deals {damage} damage!")

                        if not self.player.is_alive():
                            A.animate("Player is Dead!")
                            break
            
            A.clear()
            A.animate(f"Player HP: {self.player.hp}")
            A.animate(f"\nEnemy HP: {self.enemy.hp}")
            A.clear()
            
            
    def skip_intro(self):
        
        while self.player.is_alive() and self.enemy.is_alive():

            A.clear()
            A.animate("\n======================================",speed=0.01)
            A.animate("\nReminders:")
            A.animate("\nBoth participant has standard of 50 HP")
            A.animate("\nYou cannot use heal skill if HP is full")
            A.animate("\n--------------------------------------",speed=0.01)
            A.animate("\n1. Attack")
            A.animate("\n2. Heal")
            #A.animate("\n3. Ultimate skill")
            choice = A.input_animation("\nChoose: ")

            if choice == "1":

                # Player attacks enemy
                F.sword_player()
                dmg = self.player.attack()
                self.enemy.hp -= dmg
                A.animate(f"Player deals {dmg} damage!")

                if not self.enemy.is_alive():
                    A.clear()
                    A.animate("\nEnemy is Dead!")
                    A.backstep()
                    break

                # Enemy attacks player
                F.sword_enemy()
                damage = self.enemy.attack()
                self.player.hp -= damage
                A.animate(f"Enemy deals {damage} damage!")

                if not self.player.is_alive():
                    A.animate("Player is Dead!")
                    A.backstep()
                    break
            
            elif choice == "2":
                
                #heal player
                if self.player.hp == 50:
                        A.animate("Player HP is full")
                        time.sleep (1)
                        pass
                else:
                    if self.player.hp < 50:
                        F.heal_animation()
                        hp_heal = self.player.heal()
                        self.player.hp += hp_heal
                        A.animate(f"Healing: + {hp_heal}")
                
                        #enemy attack
                        F.sword_enemy()
                        damage = self.enemy.attack()
                        self.player.hp -= damage
                        A.animate(f"Enemy deals {damage} damage!")

                        if not self.player.is_alive():
                            A.animate("Player is Dead!")
                            A.backstep()
                            break
            
            A.clear()
            A.animate(f"Player HP: {self.player.hp}")
            A.animate(f"\nEnemy HP: {self.enemy.hp}")
            A.clear()
