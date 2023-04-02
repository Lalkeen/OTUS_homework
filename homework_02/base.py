from abc import ABC

import homework_02.exceptions
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=100, fuel=40, fuel_consumption=10):

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

    def move(self, travel):
        req_fuel = self.fuel_consumption * travel
        if req_fuel <= self.fuel:
            self.fuel -= req_fuel
        else:
            raise NotEnoughFuel
