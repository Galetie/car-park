from display import Display
from sensor import Sensor


class CarPark:
    def __init__(
            self,
            location: str = 'Unknown',
            capacity: int = 0,
            plates: list[str] = None,
            displays: list[Display] = None
    ):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.displays = displays

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"

    def register(self, hardware: Sensor | Display) -> None:
        if isinstance(hardware, Sensor):
            hardware.car_park = self
            return
        elif isinstance(hardware, Display):
            self.displays.append(hardware)
            return

        raise TypeError(f"Object must be a Sensor or Display, got: {type(hardware)}")

    def add_car(self, plate: str):
        if plate in self.plates:
            raise Exception(f"Plate {plate} is already in the car park!")

        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        if plate not in self.plates:
            raise Exception(f"Plate {plate} does not exist in the car park!")

        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        pass # stub

    @property
    def available_bays(self):
        return max(self.capacity - len(self.plates), 0)