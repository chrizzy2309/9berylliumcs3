class Car: #create a class called Car
    def __init__(self): #create a constructor method to initialize the attributes of the Car class
        pass

    def move(self):#create a method to move the car
        print("The car drives on the road.")

    def start_trip(self):#create a method to start the trip of the car
        self.move()


class Boat: #create a class called Boat
    def __init__(self):#create a constructor method to initialize the attributes of the Boat class
        pass

    def move(self): #create a method to move the boat
        print("The boat sails on water.")

    def start_trip(self): #create a method to start the trip of the boat
        self.move()


class Drone:
    def __init__(self):#create a constructor method to initialize the attributes of the Drone class
        pass

    def move(self):#create a method to move the drone
        print("The drone flies in the sky.")

    def start_trip(self):#create a method to start the trip of the drone
        self.move()


drone1 = Drone()
drone1.start_trip()
boat1 = Boat()
boat1.start_trip()
car1 = Car()
car1.start_trip()
