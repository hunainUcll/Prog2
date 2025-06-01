class Money:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    def __add__(self,other):
        if not other.currency == self.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount + other.amount,self.currency)

    def __sub__(self,other):
        if not other.currency == self.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount - other.amount , self.currency)
    
    def __mul__(self,value):
        return Money(self.amount * value, self.currency)
    
    



















"""class Money:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    def __add__(self,other):
            if(self.currency == other.currency):
                answer = self.amount + other.amount
                return  Money(answer,self.currency)
            else:
                raise RuntimeError('Mismatched currencies!')

    def __sub__(self,other):
            if(self.currency == other.currency):
                answer = self.amount - other.amount
                return  Money(answer,self.currency)
            else:
                raise RuntimeError('Mismatched currencies!')
    def __mul__(self,number):
         return Money(self.amount*number,self.currency)

  """


        



        