from rhomb import rhomb

class square(rhomb):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
        self.figure_type = "Квадрат"
        if(not self.check_isRightAngles()):
            raise ValueError("Кути не прямі")
    
    def check_isRightAngles(self):
        if(self.angleA == self.angleB and self.angleB == self.angleC and self.angleC == self.angleD):
            return True
        return False
    def get_subtypes(self):
        return ["Чотирикутник", "Ромб", "Квадрат"]