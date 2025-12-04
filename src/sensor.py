from abc import abstractmethod, ABC
import random


class Sensor(ABC):
    """
    Abstract base class for vehicle detection sensors.
    
    This class provides the interface for sensors that detect vehicles
    entering or exiting a car park. Subclasses must implement the
    update_car_park method to define specific behavior.
    
    Attributes:
        id (int): Unique identifier for the sensor.
        is_active (bool): Whether the sensor is currently active.
        car_park (CarPark): Reference to the car park this sensor monitors.
    """
    
    def __init__(
            self,
            id: int = None,
            is_active: bool = False,
            car_park = None
    ):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    @abstractmethod
    def update_car_park(self, plate: str):
        pass

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)