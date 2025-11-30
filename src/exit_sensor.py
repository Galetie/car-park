import random

from sensor import Sensor


class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate: str) -> None:
        self.car_park.remove_car(plate)