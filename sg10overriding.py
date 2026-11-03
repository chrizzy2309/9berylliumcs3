class Animal:   # create a class called Animal
    def __init__(self, name): # creates a constructor method that initializes the name attribute of the Animal class
        self.name = name
    
    def feed(self): # creates a method that prints a message indicating that the animal is eating
        print(f" the {self.name} eats.") # prints a message indicating that the animal is eating

    def make_sound(self):# creates a method that prints a message indicating that the animal is making a sound
        print(f" the {self.name} makes a sound.")# creates a method that prints a message indicating that the animal is making a sound

class Lion(Animal): # creates a class called Lion that inherits from Animal

    def __init__(self, name): # creates a constructor method that initializes the name attribute of the Lion class
        super().__init__(name) # inherits the constructor of the parent class (Animal) to initialize the name attribute

    def make_sound(self): # creates a method that prints a message indicating that the lion is roaring
        print(f" the {self.name} roars!") # prints a message indicating that the lion is roaring

    def feed(self): # creates a method that prints a message indicating that the lion is eating
        print(f" the {self.name} eats fresh meat.") # prints a message indicating that the lion is eating fresh meat

class Elephant(Animal): # creates a class called Elephant that inherits from Animal
    def __init__(self, name): # creates a constructor method that initializes the name attribute of the Elephant class
        super().__init__(name)  # inherits the constructor of the parent class (Animal) to initialize the name attribute


    def make_sound(self): # creates a method that prints a message indicating that the elephant is trumpeting
        print(f" the {self.name} trumpets!") # prints a message indicating that the elephant is trumpeting

    def feed(self): # creates a method that prints a message indicating that the elephant is eating
        print(f" the {self.name} eats grass and fruits.") # prints a message indicating that the elephant is eating grass and fruits

class Monkey(Animal): # creates a class called Monkey that inherits from Animal
    def __init__(self, name):# creates a constructor method that initializes the name attribute of the Monkey class
        super().__init__(name) # inherits the constructor of the parent class (Animal) to initialize the name attribute


    def make_sound(self): # creates a method that prints a message indicating that the monkey is chattering
        print(f" the {self.name} chatters!") # prints a message indicating that the monkey is chattering

    def feed(self): # creates a method that prints a message indicating that the monkey is eating
        print(f" the {self.name} eats bananas.") # prints a message indicating that the monkey is eating bananas

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.feed()
print("-----")

elephant.make_sound()
elephant.feed()
print("-----")

monkey.make_sound()
monkey.feed()
print("-----")
