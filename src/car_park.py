from datetime import datetime
from pathlib import Path
from display import Display
from sensor import Sensor
import json


class CarPark:
    """
    A car park management system that tracks vehicle entries and exits.
    
    This class manages parking bays, vehicle registration plates, display units,
    and activity logging for a car park facility.
    
    Attributes:
        location (str): The physical location of the car park.
        capacity (int): The total number of parking bays available.
        plates (list[str]): List of currently parked vehicle license plates.
        displays (list[Display]): Connected display units showing car park information.
        log_file (Path): Path to the activity log file.
        config_file (Path): Path to the configuration file.
    """
    
    def __init__(
            self,
            location: str = 'Unknown',
            capacity: int = 0,
            plates: list[str] | None = None,
            displays: list[Display] | None = None,
            log_file: Path | str | None = None,
            config_file: Path | str | None = None
    ):
        self.location = location
        self.capacity = capacity

        if plates is None:
            self.plates = []
        else:
            self.plates = plates

        if displays is None:
            self.displays = []
        else:
            self.displays = displays

        if isinstance(log_file, str):
            self.log_file = Path(log_file)
        elif isinstance(log_file, Path):
            self.log_file = log_file
        else:
            self.log_file = Path("log.txt")

        self._create_log_file()

        if isinstance(config_file, str):
            self.config_file = Path(config_file)
        elif isinstance(config_file, Path):
            self.config_file = config_file
        else:
            self.config_file = Path("config.json")

    def write_config(self):
        with self.config_file.open("w") as f:
            json.dump(
                {
                    "location": self.location,
                    "capacity": self.capacity,
                    "log_file": str(self.log_file),
                    "config_file": str(self.config_file)
                },
                f
            )

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(location=config["location"], capacity=config["capacity"], log_file=config["log_file"])

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def _create_log_file(self):
        if self.log_file is None:
            raise ValueError("Log file cannot be None")

        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"

    def register(self, hardware: Sensor | Display) -> None:
        if isinstance(hardware, Sensor):
            hardware.car_park = self
            return
        elif isinstance(hardware, Display):
            self.displays.append(hardware)
            return

        raise TypeError(f"Object must be a Sensor or Display, got: {type(hardware)}")

    def add_car(self, plate: str):
        if plate in self.plates:
            raise Exception(f"Plate {plate} is already in the car park!")

        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

    def remove_car(self, plate):
        if plate not in self.plates:
            raise ValueError(f"Plate {plate} does not exist in the car park!")

        self.plates.remove(plate)
        self.update_displays()
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def update_displays(self):
        display_data = {
            "available_bays": self.available_bays,
            "temperature": 25, # TODO: Sensor or weather API
            "time": datetime.now()
        }

        for display in self.displays:
            display.update(display_data)

    @property
    def available_bays(self):
        return max(self.capacity - len(self.plates), 0)