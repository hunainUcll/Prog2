class BMICalculator:
    def __init__(self,weight_in_kg,height_in_m):
        self.weight = weight_in_kg
        self.height =height_in_m
    
    @property
    def bmi(self):
        return self.weight/(self.height**2)
    
    @property
    def category(self):
        bmi =self.bmi
        if bmi < 18.5 :
            return "underweight"
        elif bmi >= 18.5 and bmi <= 25:
            return "normal"
        else:
            return "overweight"









"""class BMICalculator:
    def __init__(self,weight_in_kg,height_in_m):
        self.weight = weight_in_kg
        self.height = height_in_m

    @property
    def bmi(self):
        return self.weight// (self.height**2)
    @property
    def category(self):
        bmi =  self.weight // (self.height**2)
        if bmi < 18.5:
            return "underweight"
        elif bmi > 18.5 and bmi < 25:
            return "normal"
        else:
            return "overweight"

calc = BMICalculator(weight_in_kg=80,height_in_m=1.80)

print(calc.bmi)
print(calc.category)"""