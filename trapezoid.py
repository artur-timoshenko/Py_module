from structures import dot,angle,line
from quadrangle import quadrangle
from util_functions import are_parallel

class trapezoid(quadrangle):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
        if not self.check_isTrapezoid():
            raise ValueError("Задані точки не утворюють трапецію")
        self.figure_type = "Трапеція"
    
    def check_isTrapezoid(self):
        if (are_parallel(self.lineAB, self.lineCD) and not are_parallel(self.lineBC, self.lineDA)) \
                or (not are_parallel(self.lineAB, self.lineCD) and are_parallel(self.lineBC, self.lineDA)):
            return True
        return False
    def get_subtypes(self):
        return ["Чотирикутник", "Трапеція"]