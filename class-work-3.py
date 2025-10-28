class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving on the road")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on water")

vehicles = [Car(), Boat()]
for v in vehicles:
    v.move()
