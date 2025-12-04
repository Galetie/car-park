import random

from sensor import Sensor


class ExitSensor(Sensor):
    def _scan_plate(self):
        # Check if the car park has plates to pull from, as this is a hack
        if len(self.car_park.plates) == 0:
            return None

        return random.choice(self.car_park.plates)

    def update_car_park(self, plate: str) -> None:
        self.car_park.remove_car(plate)