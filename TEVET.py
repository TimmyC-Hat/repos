class Description:
    def __init__(self, description):
        self.description = description

class Level(Description):
    def __init__(self, description, level, sanity):
        super().__init__(description)
        self.level = level
        self.start_sanity = sanity
          
class Puzzle(Description):
    def __init__(self, description):
        super().__init__(description)

class Item(Description):
    def __init__(self, hydration, sanity, hunger):
        self.hydration = hydration
        self.sanity = sanity
        self.hunger = hunger

class Player:
    def __init__(self, hydration, sanity, hunger):
        self.hydration = hydration
        self.sanity = sanity
        self.hunger = hunger
        self.is_alive = True

if __name__ == "__main__":
    