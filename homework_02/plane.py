from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, max_cargo, weight=0, started=False, fuel=0, fuel_consumption=0):
        super().__init__(weight, started, fuel, fuel_consumption)

        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        common_weight = weight + self.cargo

        if common_weight <= self.max_cargo:
            self.cargo = common_weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res
