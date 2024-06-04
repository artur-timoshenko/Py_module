from quadrangle import quadrangle

class rhomb(quadrangle):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
        self.check_rhombus()
        self.figure_type = "Ромб"

    def check_rhombus(self):
        if self.AB_length != self.BC_length or self.BC_length != self.CD_length or self.CD_length != self.DA_length:
            raise ValueError("Сторони не рівні")
        self.size_length = self.AB_length
    def get_subtypes(self):
        return ["Чотирикутник"," Ромб"]
