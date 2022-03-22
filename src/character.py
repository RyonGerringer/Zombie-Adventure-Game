

class Character:
    def __init__(self, name, money, health, damage, accuracy, stamina, knownLocations, items):
        self.name = name
        self.money = money
        self.health = health
        self.damage = damage
        self.accuracy = accuracy
        self.stamina = stamina
        self.knownLocations = []
        self.items = {}
        self.weapon = None
        self.stats = self.Stats()

    class Stats:
        def __init__(self):
            self.fights = 0
            self.trappedFights = 0