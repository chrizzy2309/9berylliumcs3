class GENSHIN:
    def __init__(self, name, nation, element, weapon):
        self.name = name
        self.nation = nation
        self.element = element
        self.weapon = weapon


    def display_name(self):
        print(f"{self.name})")

    def display_nation(self):
        print(f"{self.nation}")

    def display_element(self):
        print(f"{self.element}")

    def display_weapon(self):
        print(f"{self.weapon}")

character79 = GENSHIN("Arlechinno", "Fontaine", "Pyro", "Polearm")
character110 = GENSHIN("Zibai", "Liyue", "Geo", "Sword") 

print("Initial Character Information")

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

print("For character110")

print()

print("Character Name: ")

character110.display_name()

print()

print("Character Nation: ")

character110.display_nation()

print()

print("Character Element: ")

character110.display_element()

print()

print("Character Weapon: ")
character110.display_weapon()

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

print("For character110")

print()

print("Character Name: ")
character110.display_name()

print()

print("Character Nation: ")
character110.display_nation()

print()

print("Character Element: ")
character110.display_element()

print()

print("Character Weapon: ")
character110.display_weapon()
