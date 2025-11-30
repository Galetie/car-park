from sensor import Sensor


class ExitSensor(Sensor):
    def update_car_park(self, plate: str) -> None:
        self.car_park.add_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")  # CarPark should be responsible for this