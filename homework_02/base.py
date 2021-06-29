from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    # def start(self):
    #     if not self.started:
    #         if self.fuel > 0:
    #             self.started = True
    #         else:
    #             raise LowFuelError

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance):
        max_distance = self.fuel * self.fuel_consumption
        if distance > max_distance:
            raise NotEnoughFuel
        else:
            self.fuel = self.fuel - distance/self.fuel_consumption

    pass
