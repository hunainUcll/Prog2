class Human:
    def __init__(self,name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    
class Archer(Human):
    def __init__(self, name,arrows):
        super().__init__(name)
        self.__num_arrows = arrows

    def get_num_arrows(self):
        return self.__num_arrows
        

































"""class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        pass

    def get_num_arrows(self):
        return self.__num_arrows"""