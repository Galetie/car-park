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

    def register(self, hardware: Sensor | Display):
        if isinstance(hardware, Sensor):
            pass # stub
        elif isinstance(hardware, Display):
            self.displays.append(hardware)