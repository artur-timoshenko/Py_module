from structures import dot,angle
from quadrangle import quadrangle
from trapezoid import trapezoid

class rectangular_trapezoid(trapezoid):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
        self.figure_type = "Прямокутна трапеція"
        if(not self.check_isRectangularTrapezoid()):
            raise ValueError("Задані точки не утворюють прямокутну трапецію")

    
    def check_isRectangularTrapezoid(self):
        if self.angleB == 90 and self.angleC == 90:
            return True
        elif self.angleC == 90 and self.angleD == 90:
            return True
        elif self.angleD == 90 and self.angleA == 90:
            return True
        elif self.angleA == 90 and self.angleB == 90:
            return True
        else:
            return False
    def get_subtypes(self):
        return ["Чотирикутник", "Трапеція", "Прямокутна трапеція"]