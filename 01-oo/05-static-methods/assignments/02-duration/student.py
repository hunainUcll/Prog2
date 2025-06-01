class Duration:
    def __init__(self,seconds):
        self.__seconds = seconds
    
    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__seconds//60
    
    @property
    def hours(self):
        return self.__seconds//3600
    
    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)
    
    @staticmethod 
    def from_minutes(minutes):
        return Duration(minutes * 60)
    
    @staticmethod
    def from_hours(hours):
        return Duration(hours*3600)







































"""class Duration:
    def __init__(self,second : int):
        self.__seconds = second
    
    @property
    def seconds(self) -> int:
        return self.__seconds

    @property
    def minutes(self) ->int:
        return self.__seconds // 60
    
    @property
    def hours(self) -> int:
        return self.__seconds // 3600
    
    @staticmethod
    def from_seconds(seconds) -> "Duration":
        return Duration(seconds)
    
    @staticmethod 
    def from_minutes(minutes) -> "Duration":
        return Duration(minutes * 60)
    
    @staticmethod
    def from_hours(hours) -> "Duration":
        return Duration(hours*3600)



# Example usage
duration = Duration.from_seconds(60)
print(duration.seconds)  # 60
print(duration.minutes)  # 1

duration = Duration.from_hours(1)
print(duration.minutes)  # 60
print(duration.seconds)  # 3600
"""