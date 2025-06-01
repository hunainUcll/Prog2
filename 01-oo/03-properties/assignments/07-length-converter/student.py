
class LengthConverter:
    def __init__(self):
        # Initialize with 0 meters as default value
        self.__distance_in_meter = 0
    
    @property
    def meter(self):
        # Return the distance in meters
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self, value):
        # Convert the value to meters and store
        self.__distance_in_meter = value
    
    @property
    def feet(self):
        # Convert meters to feet (1 meter = 3.28084 feet)
        return self.__distance_in_meter * 3.28084
    
    @feet.setter
    def feet(self, value):
        # Convert feet to meters and store (1 foot = 0.3048 meters)
        self.__distance_in_meter = value * 0.3048
    
    @property
    def inch(self):
        # Convert meters to inches (1 meter = 39.3701 inches)
        return self.__distance_in_meter * 39.3701
    
    @inch.setter
    def inch(self, value):
        # Convert inches to meters and store (1 inch = 0.0254 meters)
        self.__distance_in_meter = value * 0.0254
