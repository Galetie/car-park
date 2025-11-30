from display import Display


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
