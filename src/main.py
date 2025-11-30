from car_park import CarPark
from display import Display
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor

# create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
_car_park = CarPark(
    location="moondalup",
    capacity=100,
    log_file="moondalup.txt",
    config_file="moondalup_config.json"
)

# Write the car park configuration to a file called "moondalup_config.json"
_car_park.write_config()

# Reinitialize the car park object from the "moondalup_config.json" file
re_car_park = CarPark.from_config("moondalup_config.json")

# create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(
    1,
    True,
    re_car_park
)

# create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(
    1,
    True,
    re_car_park
)

# create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(
    1,
    "Welcome to Moondalup",
    True
)
re_car_park.register(display)

# drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for _ in range(10):
    entry_sensor.detect_vehicle()

# drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for _ in range(2):
    exit_sensor.detect_vehicle()
