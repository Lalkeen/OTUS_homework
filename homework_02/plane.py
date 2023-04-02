"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __int__(self, weight: int, fuel: int,
                fuel_consumption: int, max_cargo: int):
        super().__init__()
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, plus_load: int):
        if self.cargo + plus_load < self.max_cargo:
            self.cargo += plus_load
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo_old = self.cargo
        self.cargo = 0
        return cargo_old
