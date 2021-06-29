"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    print(' * '*15, 'LowFuelError')


class NotEnoughFuel(Exception):
    print(' * '*15, 'NotEnoughFuel')


class CargoOverload(Exception):
    print(' * '*15, 'CargoOverload')
