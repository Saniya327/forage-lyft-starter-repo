from abc import ABC
import datetime

from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date):
        self.time_limit = 4
        self.current_date = datetime.today().date()
        self.last_service_date=last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.time_limit)
        if service_threshold_date < self.current_date or self.engine_should_be_serviced():
            return True
        else:
            return False
