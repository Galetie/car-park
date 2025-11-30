from abc import abstractmethod
import random


class Sensor:
    def __init__(
            self,
            id: int = None,
            is_active: bool = False,
            car_park = None
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
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)