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