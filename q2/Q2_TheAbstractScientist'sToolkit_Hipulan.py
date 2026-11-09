from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading():
        pass


class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5 °C"

print("--- Lab Inventory System ---")
for sensor in [PHSensor()]:
    print(f"[pH Sensor] Reading: {sensor.get_reading()} (Neutral)")
for sensor in [TempSensor()]:
    print(f"[Temperature Sensor] Reading: {sensor.get_reading()}")
print(" ")
print("----------------------------")
