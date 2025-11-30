from abc import ABC, abstractmethod
import random

from car_park import CarPark


class Sensor:
    def __init__(
            self,
            id: str = None,
            is_active: bool = False,
            car_park: CarPark = None
    ):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    @abstractmethod
    def update_car_park(self, plate: str):
        pass

    @abstractmethod
    def detect_car(self):
        pass