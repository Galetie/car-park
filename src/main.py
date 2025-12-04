from car_park import CarPark
from display import Display
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor

_car_park = CarPark(
    location="moondalup",
    capacity=100,
    log_file="moondalup.txt",
    config_file="moondalup_config.json"
)

_car_park.write_config()

# Demonstrate config persistence by reloading from file
re_car_park = CarPark.from_config("moondalup_config.json")

entry_sensor = EntrySensor(
    1,
    True,
    re_car_park
)

exit_sensor = ExitSensor(
    1,
    True,
    re_car_park
)

display = Display(
    1,
    "Welcome to Moondalup",
    True
)
re_car_park.register(display)

for _ in range(10):
    entry_sensor.detect_vehicle()

for _ in range(2):
    exit_sensor.detect_vehicle()
