from sensor import Sensor


class EntrySensor(Sensor):
    def update_car_park(self, plate: str) -> None:
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")  # CarPark should be responsible for this