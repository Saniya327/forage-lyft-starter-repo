from tyre import Tyre


class NubbinBattery(Tyre):
    def __init__(self,sensor_arr):
        self.sensor_arr=sensor_arr

    def needs_service(self):
        if sum(self.sensor_arr) >= 3:
            return True
        else:
            return False
