from sensor import Sensor


class EntrySensor(Sensor):
    """
    A sensor that detects vehicles entering the car park.
    
    This sensor monitors entry points and registers new vehicles
    by adding their license plates to the car park system.
    """
    
    def update_car_park(self, plate: str) -> None:
        self.car_park.add_car(plate)

