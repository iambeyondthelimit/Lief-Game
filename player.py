class Player:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk.random.randint(10, 15)

    def is_alive(self):
        return self.hp > 0
