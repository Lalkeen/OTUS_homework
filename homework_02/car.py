"""
создайте класс `Car`, наследник `Vehicle`
"""
# from dataclasses import dataclass

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = Engine(volume=1.4, pistons=4)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_engine(self, engine: Engine):
        if isinstance(engine, Engine):
            self.engine = engine
