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

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"