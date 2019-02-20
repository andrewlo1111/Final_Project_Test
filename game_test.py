class Unit():
    
    def __init__(self):
        self.attack = 1
        self.defense = 1
    

class Villager(Unit):
    
    def move(self):
        print("Villager moved")

    def build(self):
        building = input("What building would you like to make?")
        possible_buildings = ['town center', 'farm', 'mine']
        for selected in possible_buildings:
            if (building == possible_buildings[selected]):
                print("Built" + possible_buildings[selected])
                
    