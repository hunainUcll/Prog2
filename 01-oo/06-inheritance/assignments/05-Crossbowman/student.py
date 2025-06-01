class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows
    
    def use_arrows(self,num):
        arrows = self.get_num_arrows()
        if num > arrows:
            raise   ValueError("Not enough arrows")        
        self.__num_arrows -= num

class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)
    
    def triple_shot(self, human):
        self.use_arrows(3)
        return human + " was shot by 3 crossbow bolts"





















"""class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        pass


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        pass

    def triple_shot(self, target):
        pass"""