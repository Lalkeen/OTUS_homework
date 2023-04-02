from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __int__(self, weight=0, fuel=40, fuel_consumption=10, *args, **kwargs):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, travel: int):
        if self.fuel/self.fuel_consumption > travel:
            return True
        else:
            return NotEnoughFuel
