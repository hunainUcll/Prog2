# Write your code here

class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property 
    def seconds(self):
        return self.__seconds   
    
    @hours.setter
    def hours(self,value):
        if value > 23 or value < 0:
            raise ValueError("hours must be inbetween 0 and 23")
        self.__hours = value

    @minutes.setter
    def minutes(self,value):
        if value > 59 or value < 0:
            raise ValueError("minutes must be inbetween 0 and 59")
        self.__minutes = value

    @seconds.setter
    def seconds(self,value):
        if value>59 or value < 0:
            raise ValueError("seconds must be inbetween 0 and 59")    
        self.__seconds = value

    
        


































"""class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    @property
    def minutes(self):
        return self.__minutes
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self,value):
        self.__hours = value
    
    @minutes.setter
    def minutes(self,value):
        self.__minutes = value

    @seconds.setter
    def seconds(self,value):
        self.__seconds = value
        """

        