from sensor import Sensor


class ExitSensor(Sensor):
    def update_car_park(self, plate: str) -> None:
        self.car_park.remove_car(plate)