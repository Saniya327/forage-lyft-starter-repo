import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery
from carFactory import CarFactory
from engine import capulet_engine, sternman_engine, willoughby_engine

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from tyres.carrigan_tyre import Carrigan_Tyre
from tyres.octoprime_tyre import Octoprime_Tyre


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today,last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(today,last_service_date)
        self.assertFalse(battery.needs_service())


class TestSplinder(unittest.TestCase):
      def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SplinderBattery(today,last_service_date)
        self.assertTrue(battery.needs_service())

      def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SplinderBattery(today,last_service_date)
        self.assertFalse(battery.needs_service())

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 2999
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class testSternman(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        engine = sternman_engine(True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = sternman_engine(False)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestCarrigan(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        arr=[1,1,0.9,1]
        tyre = Carrigan_Tyre(arr)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        arr=[1,1,1,1]
        tyre = Carrigan_Tyre(arr)
        self.assertFalse(tyre.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        arr=[1,1,1,1]
        tyre = Octoprime_Tyre(arr)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        arr=[0.1,0.1,0.2,0.2]
        tyre = Carrigan_Tyre(arr)
        self.assertFalse(tyre.needs_service())



if __name__ == '__main__':
    unittest.main()
