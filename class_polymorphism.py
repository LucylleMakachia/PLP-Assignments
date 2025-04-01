# Base class
class Vehicle:
    def move(self):
        pass

# Derived classes
class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🚤.")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for vehicle in vehicles:
    vehicle.move()
