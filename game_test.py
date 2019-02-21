class Unit():
    
    def __init__(self):
        self.unit_type = 'Unit'
        self.attack = 1
        self.defense = 1
        self.done = False
    
    def __str__(self):
        return self.unit_type

    def move(self):
        print("Villager moved")
        self.done = True

    def defend(self):
        print(self.unit_type + " is in defense position")
        self.defense *= 1.25
        self.done = True
    
    def attack_enemy(self,other_unit):
        print(self.unit_type + "attacking " + other_unit.unit_type)
        if(self.attack >other_unit.defense):
            print("Won battle")
            self.done
        else:
            print("Lost battle")
        

class Villager(Unit):
    unit_type = 'Villager'
    attack = .5
    defense = .5
    def __init__(self):
        pass

    def build(self):
        building = input("What building would you like to make?")
        possible_buildings = ['TownCenter', 'Farm', 'Mine']
        for selected in possible_buildings:
            if (building == possible_buildings[selected]):
                print("Built" + possible_buildings[selected])


class Warrior(Unit):
    unit_type = "Warrior"
    attack = 1
    defense = 1
    def __init__(self):
        pass

class Archer(Unit):
    unit_type = "Archer"
    attack = .75
    defense = 1.75

    def __init__(self):
        pass
       
class Knight(Unit):
    unit_type = "Knight"
    attack = 2
    defense = .75
    def __init__(self):
        pass
    

class Building():
    def __init__(self):
        self.durability = 2
        self.building_type = "Building"

class Farm(Building):
    building_type = "Farm"
    def __init__(self):
        pass

class Mine(Building):
    building_type = "Mine"
    def __init__(self):
        pass

class TownCenter(Building):
    durability = 3
    building_type = "TownCenter"
    def __init__(self):
        pass

class Player():

    def __init__(self):
        self.money = 100
        self.food = 100
        self.mine_count = 0
        self.farm_count = 0
    
    def create_unit(self):
        desired_unit = input("What unit do you want to make?")
        if(desired_unit == 'Villager'):
            print("Villager has been created")
            self.money -= 50
            self.money -= 50

        elif(desired_unit == 'Warrior'):
            self.money -= 75
            self.food -= 50
        
        elif(desired_unit == 'Archer'):
            self.money -= 100
            self.food -= 50
        
        elif(desired_unit == 'Knight'):
            self.money -= 75
            self.food -= 100
        
        else:
            print("Invalid Unit")
        
        
if __name__ == '__main__':
    useless = Villager()
    print(useless.attack)
    print(useless.defense)
    warrior1 = Warrior()
    print(warrior1)
    archer1 = Archer()
    archer1.defend()
    print(archer1.defense)

    