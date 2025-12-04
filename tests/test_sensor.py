import unittest
from car_park import CarPark
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)

    def test_init_entry(self):
        self.sensor = EntrySensor(1, True, self.car_park)
        self.assertEqual(self.sensor.car_park, self.car_park)
        self.assertEqual(self.sensor.id, 1)
        self.assertTrue(self.sensor.is_active)

    def test_detect_vehicle_entry(self):
        self.sensor = EntrySensor(1, True, self.car_park)
        initial_count = len(self.car_park.plates)
        self.sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count + 1)
        self.assertEqual(self.car_park.available_bays, 99)

    def test_init_exit(self):
        self.sensor = ExitSensor(2, True, self.car_park)
        self.assertEqual(self.sensor.car_park, self.car_park)
        self.assertEqual(self.sensor.id, 2)
        self.assertTrue(self.sensor.is_active)

    def test_detect_vehicle_exit(self):
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

        # No plates, should raise exception
        with self.assertRaises(ValueError):
            self.exit_sensor.detect_vehicle()

        # Add a car
        self.entry_sensor.detect_vehicle()

        # Should now detect fine on exit
        self.exit_sensor.detect_vehicle()