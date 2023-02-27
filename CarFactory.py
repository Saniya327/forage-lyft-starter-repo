from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        #capulet+splinder
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        battery = SplinderBattery(last_service_date)
        car = Car(engine,battery)
        print("calliope")
        print(car.battery.needs_service())
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        #willoughby+splinder
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        battery = SplinderBattery(last_service_date)
        car = Car(engine,battery)
        return car

    def create_palindrome(current_date, last_service_date,warning_light_is_on):
        #sternman+splinder
        engine = SternmanEngine(warning_light_is_on)
        battery = SplinderBattery(last_service_date)
        car = Car(engine,battery)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        #willoughby+nubbin
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(engine,battery)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        #capulet+nubbin
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(engine,battery)
        return car
