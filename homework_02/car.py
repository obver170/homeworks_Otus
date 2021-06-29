from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        super().__init__(weight, started, fuel, fuel_consumption)

        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
