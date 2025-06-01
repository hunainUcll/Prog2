class Queue:
    def __init__(self):
        self.current=[]

    def add(self,item):
        self.current.append(item)
    
    def next(self):
        a = self.current[0]
        self.current.pop(0)
        return a 
    
    def is_empty(self):
        if(len(self.current) == 0):
            return True
        else:
            return False










"""class Queue:

    def __init__(self):
        self.current = []

    def add(self,item):
        self.current.append(item)
    
    def is_empty(self):
        if len(self.current) == 0 : 
            return True
        else:
            return False
    
    def next(self): 
        answer = self.current[0]
        del self.current[0]
        return answer"""