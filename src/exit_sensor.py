import random

from sensor import Sensor


class ExitSensor(Sensor):
    """
    A sensor that detects vehicles exiting the car park.
    
    This sensor monitors exit points and removes vehicles from the
    car park system by selecting from currently registered plates.
    """
    
    def _scan_plate(self):
        # Exit sensors need existing plates to simulate realistic exits
        if len(self.car_park.plates) == 0:
            return None

        return random.choice(self.car_park.plates)

    def update_car_park(self, plate: str) -> None:
        self.car_park.remove_car(plate)