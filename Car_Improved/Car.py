from Engine import *
from Wheels import *
from Persons import *
from Lights import *
from Seats import *

class Car:
    def __init__():
        self.engine = Engine("Diesel", 100, "V8")
        self.front_lights = Lights(85, "front", "white")
        self.back_lights = Lights(85, "back", "red")
        self.front_seat = Seats("Leather")
        self.back_seat = Seats("Leather")
        self.driver = Persons("Andy", "no")
        self.passenger = Persons("Mandy", "yes") 
