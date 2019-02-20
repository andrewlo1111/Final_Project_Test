class Unit():
    
    def __init__(self):
        self.attack = 1
        self.defense = 1
    
    def defend(self):
        print("Unit is in defense position")
    
    def attack_enemy(self,other_unit):
        print("Attacking " + other_unit)
        if(self.attack >other_unit.defense):
            print("Win battle")
        else:
            print("Lost battle")
        

class Villager(Unit):
    attack = .5
    defense = .5
    def __init__(self):
        pass
    
    def __str__(self):
        return "Villager"

    def move(self):
        print("Villager moved")

    def build(self):
        building = input("What building would you like to make?")
        possible_buildings = ['town center', 'farm', 'mine']
        for selected in possible_buildings:
            if (building == possible_buildings[selected]):
                print("Built" + possible_buildings[selected])


class Warrior(Unit):
    attack = 1
    defense = 1
    def __init__(self):
        pass

    def __str__(self):
        return "Warrior"

class Archer(Unit):
    attack = .75
    defense = 2
    def __init__(self):
        pass
    
    def__str__(self):
        return "Archer"
    
class Knight(Unit):
    attack = 2
    defense = .75
    def __init__(self):
        pass
    
    def __str__(self):
        return "Knight"


if __name__ == '__main__':
    useless = Villager()
    print(useless.attack)
    print(useless.defense)

    