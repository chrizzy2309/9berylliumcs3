character79 = GENSHIN("Arlechinno", "Fontaine", "Pyro", "Polearm")

print("Initial Character Information")

print()

print("For character79")

print()

print("Character Name: ")
add 
character79.display_name()

print()

print("Character Nation: ")
character79.display_nation()

print()

print("Character Element: ")
character79.display_element()

print()

print("Character Weapon: ")
character79.display_weapon()

print()
print()

setattr(character79, "weapon", "Catalyst")

print()
print()

print("Updated Character Information: ")

print()

print("For character79")

print()

print("Character Name: ")
character79.display_name()

print()

print("Character Nation: ")
character79.display_nation()

print()

print("Character Element: ")
character79.display_element()

print()

print("Character Weapon: ")
character79.display_weapon()

print()
print()


class NATION:
    def __init__(self, name,  weapon, element, region):
        
        self.name = name
        self.weapon = weapon
        self.element = element
        self.region = region
       

    def display_name(self):
        print(f"{self.name}")
    
    def display_weapon(self):
        print(f"{self.weapon}")
        
    def display_element(self):
        print(f"{self.element}")
        
    def display_region(self):
        print(f"{self.region}")
        
NATION.
        


