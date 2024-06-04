from quadrangle import quadrangle
from util_functions import are_parallel
class rectangle(quadrangle):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
        self.check_isRightAngles()
        self.figure_type = "Прямокутник"

    def check_isRightAngles(self):
        if(self.angleA == self.angleB and self.angleB == self.angleC and self.angleC == self.angleD):
            return True
        return False
    def get_subtypes(self):
        return ["Чотирикутник, Прямокутник"]