class GENSHIN:
    def __init__(self, name, nation, element, weapon):
        self.name = name
        self.nation = nation
        self.element = element
        self.weapon = weapon

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Nation: {self.nation}")
        print(f"Element: {self.element}")
        print(f"Weapon: {self.weapon}")





class Model_Type(GENSHIN):
    def __init__(self, name, nation, element, weapon, model_type):
        super().__init__(name, nation, element, weapon)
        self.model_type = model_type

    def display_model_type(self):
        print(f"Model Type: {self.model_type}")


#TESTING
character79 = Model_Type("Arlechinno", "Fontaine", "Pyro", "Polearm", "Tall Female")

character79.display_info()
character79.display_model_type()
