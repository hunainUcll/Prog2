class CircularBuffer:
    def __init__(self,length):
        self.length = length
        self.list = []
    
    def add(self,value):
        self.list.append(value)
        while (len(self.list) > self.length):
            self.list.pop(0)

    def __getitem__(self,value):
        return self.list[value]
    
    def __len__(self):
        return len(self.list)






"""class CircularBuffer:
    def __init__(self,length):
        self.length = length
        self.list = []
    
    def add(self,char):
        self.list.append(char)
        while (len(self.list) > self.length):
            self.list.pop(0)
    
    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, index):
        return self.list[index]
    
"""
    

        