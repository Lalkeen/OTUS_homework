"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel,
                fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, plus_load):
        if self.cargo + plus_load <= self.max_cargo:
            self.cargo += plus_load
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo_old = self.cargo
        self.cargo = 0
        return cargo_old
