import random

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def attack(self):
        return random.randint(10, 15)
        
    def heal(self):
        return random.randint(10, 15)
    
    def is_alive(self):
        return self.hp > 0
