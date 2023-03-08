from tyre import Tyre


class Carrigan_Tyre(Tyre):
    def __init__(self,sensor_arr):
        self.sensor_arr=sensor_arr

    def needs_service(self):
        for i in self.sensor_arr:
            if i >= 0.9:
                return True
        return False
