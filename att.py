class Vehicle():
    def __init__(self, weight):
        print('Vehicle class created')
        self.weight = weight
        self.number_wheels = 4

    def _mytype(self):
        print('Type Vehicle')

vehicle = Vehicle(1000)
vehicle._mytype()

class Car(Vehicle):
    def __init__(self,weight):
        Vehicle.__init__(self, weight)
        print('\nCar class created')
        self.number_doors = 4

    def car_name(self):
        print('Audio')

    def _mytype(self):
        print('Type Car')

car = Car(1500)
car.car_name()
car._mytype()
print(car.number_wheels, car.number_doors)

class Robot(Vehicle):
    def __init__(self,weight):
        Vehicle.__init__(self, weight)
        print('\nRobot class created')
        self.number_doors = 2

    def robot_name(self):
        print('R2D2')

    def _mytype(self):
        print('Type Robot')

robot = Robot(10000)
robot.robot_name()
robot._mytype()
print(robot.number_wheels, robot.number_doors)

class Motoc(Vehicle):
    def __init__(self,weight):
        Vehicle.__init__(self, weight)
        print('\nMotoc class created')
        self.number_doors = 0

    def motoc_name(self):
        print('dugatti')

    def _mytype(self):
        print('Type Motoc')

motoc = Motoc(100)
motoc.motoc_name()
motoc._mytype()
print(motoc.number_wheels, motoc.number_doors)