## Overriding methods
## Since our ElectricCar is a more specialized type of Car, 
## we can give the ElectricCar its own drive_car() method 
## that has different functionality than the original Car class's.

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        return "This is a %s %s with %d MPG." % (self.color, self.model, self.mpg)
        
    def drive_car(self):
        self.condition = "used"
        return self.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        Car.__init__(self, model, color, mpg)
        self.battery_type = battery_type
        
    def drive_car(self):
        self.condition = "like new"
        return self.condition

my_car = ElectricCar("Prius", "blue", 88, "molten salt")
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
print my_car.battery_type
print my_car.drive_car()