from display import Display


class CarPark:
    def __init__(self, location: str, capacity: int, plates: list[str], displays: Display):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.displays = displays
