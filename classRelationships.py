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

print()

setattr(character79, "weapon", "Catalyst")

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

print()

class NATION:
    def __init__(self, nation):
        self.Nation = nation
        self.__CHARACTERS_LIST = []
       
       
    def display_nation(self):
        return self.Nation

    def ADD_CHARACTER(self, character: GENSHIN):
        """Adds a character to the nation's list."""
        self.__CHARACTERS_LIST.append(character)

    def display_characters(self):
        """Displays the names of all characters in the nation's list."""
        for character in self.__CHARACTERS_LIST:
            print(f"Character: {character.name}")




nation1 = NATION("Inazuma")

character1 = GENSHIN("Ayaka", nation1.display_nation(), "Cryo", "Sword")
character2 = GENSHIN("Ayato", nation1.display_nation(), "Hydro", "Sword")

print("Before Relationship")
print("Before adding characters to the nation, the characters do not have a nation assigned.")

print(nation1.display_nation())

print(f"Character 1: {character1.name}")
print(f"Character 2: {character2.name}")

print()
print()

print("After Relationship")
print("After adding characters to the nation, the characters now have a nation assigned.")
print()
nation1.ADD_CHARACTER(character1)
nation1.ADD_CHARACTER(character2)
print("Characters in the nation:")
nation1.display_characters()



