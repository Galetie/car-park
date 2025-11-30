from abc import ABC, abstractmethod
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

    @abstractmethod
    def update_car_park(self, plate: str):
        pass

    @abstractmethod
    def detect_car(self):
        pass