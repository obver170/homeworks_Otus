from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)

        self.cargo = 0
        self.max_cargo = max_cargo

    # def load_cargo(self, baggage):
    #     common_weight = baggage + self.cargo + self.weight
    #
    #     if common_weight <= self.max_cargo:
    #         self.cargo = common_weight - self.weight
    #     else:
    #         raise CargoOverload

    def load_cargo(self, baggage):
        common_weight = baggage + self.cargo

        if common_weight <= self.max_cargo:
            self.cargo = common_weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res
