import unittest
from sensor import Sensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)

    def test_init(self):
        self.sensor = Sensor(1, True, self.car_park)
        self.assertEqual(self.sensor.car_park, self.car_park)
        self.assertEqual(self.sensor.id, 1)
        self.assertTrue(self.sensor.is_active)

    def test_detect_vehicle(self):
        self.sensor.detect_vehicle()